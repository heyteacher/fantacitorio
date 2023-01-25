# Generated by Django 4.1.5 on 2023-01-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_classifiche_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquadraPunti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('squadra_id', models.IntegerField()),
                ('squadra_name', models.CharField(max_length=200)),
                ('politico_name', models.CharField(max_length=200)),
                ('puntata_numero', models.IntegerField()),
                ('puntata_data', models.DateTimeField(auto_now_add=True)),
                ('punti', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'punti squadra',
                'db_table': 'squadra_punti',
            },
        ),
        migrations.AlterModelOptions(
            name='classificagenerale',
            options={'ordering': ('posizione',), 'verbose_name_plural': 'classifica generale'},
        ),
        migrations.AlterModelOptions(
            name='classificaperlega',
            options={'ordering': ('lega_id', 'posizione'), 'verbose_name_plural': 'classifica per lega'},
        ),
        migrations.AlterModelOptions(
            name='classificapolitico',
            options={'ordering': ('posizione',), 'verbose_name_plural': 'classifica politici'},
        ),
        migrations.AddIndex(
            model_name='squadrapunti',
            index=models.Index(fields=['squadra_id'], name='squadra_id_idx'),
        ),
    ]