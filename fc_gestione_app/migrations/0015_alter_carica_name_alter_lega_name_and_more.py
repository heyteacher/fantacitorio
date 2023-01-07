# Generated by Django 4.1.4 on 2022-12-27 19:13

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0014_carica_aggiornato_id_carica_creato_il_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carica',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='lega',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='politico',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nomimativo'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='leader_politico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='leader', to='fc_gestione_app.politico', verbose_name='leader'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='name',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AddConstraint(
            model_name='carica',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='carica_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='lega',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='lega_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='politico',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('name'), name='politico_name_unique'),
        ),
        migrations.AddConstraint(
            model_name='squadra',
            constraint=models.UniqueConstraint(models.F('name'), name='squadra_name_unique'),
        ),
    ]