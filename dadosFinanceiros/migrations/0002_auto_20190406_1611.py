# Generated by Django 2.1.7 on 2019-04-06 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dadosFinanceiros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adicionarpagamento',
            old_name='meioDePagamendo',
            new_name='meioDePagamento',
        ),
    ]
