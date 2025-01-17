# Generated by Django 5.0.7 on 2024-08-02 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('statut', models.CharField(max_length=20)),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_htva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('montant_tva', models.DecimalField(decimal_places=2, max_digits=5)),
                ('send', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
