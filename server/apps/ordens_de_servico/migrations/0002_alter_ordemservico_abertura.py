# Generated by Django 4.2.20 on 2025-04-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordens_de_servico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='abertura',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
