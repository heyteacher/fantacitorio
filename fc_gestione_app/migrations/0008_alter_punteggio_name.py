# Generated by Django 4.1.3 on 2022-12-03 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0007_alter_legasquadra_options_punteggio_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punteggio',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='nomimativo'),
        ),
    ]
