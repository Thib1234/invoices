# Generated by Django 5.0.7 on 2024-08-05 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ligneFacture', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lignefacture',
            name='prix_unitaire',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='lignefacture',
            name='total_ligne',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='lignefacture',
            name='total_ligne_htva',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]