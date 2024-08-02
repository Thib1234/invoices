import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from facturation.models import Facture
from ligneFacture.models import LigneFacture
from facturation.serializers import FactureSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from django.db.models import Sum
from django.db.models.functions import TruncDate
from django.utils import timezone
# from django.template.loader import render_to_string
# from weasyprint import HTML


class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).prefetch_related('lignefacture_set')

    @action(detail=False, methods=['get'])
    def recent(self, request):
        recent_invoices = self.get_queryset().order_by('-created_at')[:5]
        serializer = self.get_serializer(recent_invoices, many=True)
        return Response(serializer.data)
    @action(detail=False, methods=['get'])
    def total_amount_by_month(self, request):
    # Obtenez le premier et le dernier jour du mois courant
        now = timezone.now()
        start_of_month = now.replace(day=1)
        end_of_month = (start_of_month + timezone.timedelta(days=31)).replace(day=1) - timezone.timedelta(days=1)

        # Filtrer les données pour le mois courant
        totals_by_day = self.get_queryset().filter(date__range=[start_of_month, end_of_month]).annotate(day=TruncDate('date')).values('day').annotate(total_amount=Sum('montant_total')).order_by('day')

        # Calculer le montant total sur le mois
        total_amount_month = self.get_queryset().filter(date__range=[start_of_month, end_of_month]).aggregate(total_amount_month=Sum('montant_total'))

        return Response({'totals_by_day': totals_by_day, 'total_amount_month': total_amount_month})

def generate_invoice_pdf(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)
    lignes = LigneFacture.objects.filter(facture=facture)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="facture_{facture_id}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='CustomTitle', fontSize=16, leading=24, spaceAfter=12, alignment=1))
    styles.add(ParagraphStyle(name='CustomNormal', fontSize=10, leading=14))
    styles.add(ParagraphStyle(name='CustomTableTitle', fontSize=10, leading=14, spaceAfter=6, alignment=1))
    styles.add(ParagraphStyle(name='CustomTableBody', fontSize=9, leading=12, spaceAfter=6))


    elements = []

    header_data = [
        ['Entreprise XYZ', '', 'Facture'],
        ['Adresse Entreprise', '', f'Date : {datetime.date.today()}'],
        ['Code Postal, Ville', '', f'Facture n° : {facture.id}'],
        ['Téléphone : 0123456789', '', f'Client : {facture.client.nom}'],
        ['Email : contact@xyz.com', '', f'Adresse : {facture.client.adresse}'],
    ]
    table_header = Table(header_data, colWidths=[70 * mm, 50 * mm, 50 * mm])
    table_header.setStyle(TableStyle([
        ('SPAN', (0, 0), (1, 0)),
        ('SPAN', (0, 1), (1, 1)),
        ('SPAN', (0, 2), (1, 2)),
        ('SPAN', (0, 3), (1, 3)),
        ('SPAN', (0, 4), (1, 4)),
        ('ALIGN', (0, 0), (2, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 4), 'RIGHT'),
        ('VALIGN', (0, 0), (2, 0), 'MIDDLE'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ]))
    elements.append(table_header)
    elements.append(Spacer(1, 50))

    # Tableau des articles
    data = [['Description', 'Quantité', 'Prix Unitaire', 'Total']]
    montant_total = 0
    total_htva = 0
    montant_tva = 0

    for ligne in lignes:
        total_ligne = ligne.quantite * ligne.prix_unitaire
        data.append([ligne.description, ligne.quantite, f'{ligne.prix_unitaire:.2f}', f'{total_ligne:.2f}'])
        montant_total += total_ligne
    for i in range(10):
        data.append(['', '', '', ''])

    total_htva = montant_total
    montant_tva = float(total_htva) * 0.21  # Exemple de TVA à 20%
    total_ttc = float(total_htva) + montant_tva

    data.append(['', '', 'Montant Total', f'{montant_total:.2f}'])
    data.append(['', '', 'Total HTVA', f'{total_htva:.2f}'])
    data.append(['', '', 'Montant TVA', f'{montant_tva:.2f}'])
    data.append(['', '', 'Total TTC', f'{total_ttc:.2f}'])

    table = Table(data, colWidths=[doc.width/2.0, doc.width/6.0, doc.width/6.0, doc.width/6.0])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -5), 1, colors.black),  # Lignes de grille jusqu'à 5 lignes avant la fin
        ('GRID', (-2, -4), (-1, -1), 1, colors.black),  # Lignes de grille uniquement pour les colonnes 3 et 4 des dernières lignes
        ('ALIGN', (-1, 1), (-1, -1), 'RIGHT'),
        ('LINEABOVE', (2, -4), (-1, -4), 1, colors.black),  # Ligne au-dessus du Montant Total
        ('LINEABOVE', (2, -3), (-1, -3), 1, colors.black),  # Ligne au-dessus du Total HTVA
        ('LINEABOVE', (2, -2), (-1, -2), 1, colors.black),  # Ligne au-dessus du Montant TVA
        ('LINEABOVE', (2, -1), (-1, -1), 1, colors.black),  # Ligne au-dessus du Total TTC
        ('LINEBELOW', (2, -1), (-1, -1), 1, colors.black),  # Ligne en-dessous du Total TTC
    ]))
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Conditions de paiement
    conditions = Paragraph('Conditions de paiement : À régler sous 30 jours.', styles['Normal'])
    elements.append(conditions)

    # Remerciements
    remerciements = Paragraph('Merci pour votre achat !', styles['Normal'])
    elements.append(remerciements)

    # Génération du document
    doc.build(elements)
    return response
