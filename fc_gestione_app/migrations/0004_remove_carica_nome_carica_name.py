# Generated by Django 4.1.3 on 2022-11-30 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0003_alter_squadra_utente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carica',
            name='nome',
        ),
        migrations.AddField(
            model_name='carica',
            name='name',
            field=models.CharField(default=1, max_length=50, unique=True, verbose_name='nome'),
            preserve_default=False,
        ),
    ]
