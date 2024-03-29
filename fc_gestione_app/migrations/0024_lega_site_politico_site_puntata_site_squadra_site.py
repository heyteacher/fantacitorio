# Generated by Django 4.2.2 on 2023-06-16 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('fc_gestione_app', '0023_null_user_squadra'),
    ]

    operations = [
        migrations.AddField(
            model_name='lega',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='politico',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='puntata',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='squadra',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
            preserve_default=False,
        ),
    ]
