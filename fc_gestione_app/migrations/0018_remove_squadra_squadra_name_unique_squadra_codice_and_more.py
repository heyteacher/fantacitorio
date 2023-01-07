# Generated by Django 4.1.4 on 2022-12-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0017_alter_squadra_utente'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='squadra',
            name='squadra_name_unique',
        ),
        migrations.AddField(
            model_name='squadra',
            name='codice',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddConstraint(
            model_name='squadra',
            constraint=models.UniqueConstraint(fields=('name', 'leader_politico', 'number_1_politico', 'number_2_politico', 'number_3_politico', 'number_4_politico', 'number_5_politico', 'number_6_politico', 'number_7_politico', 'number_8_politico', 'number_9_politico', 'number_10_politico', 'number_11_politico'), name='squadra_unique'),
        ),
    ]