# Generated by Django 4.1.3 on 2022-12-03 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0009_squadra_punti_alter_lega_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squadra',
            name='punti',
            field=models.IntegerField(default=0),
        ),
    ]