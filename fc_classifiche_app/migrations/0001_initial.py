# Generated by Django 4.1.3 on 2022-12-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassificaGenerale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posizione', models.IntegerField()),
                ('totale_punti', models.IntegerField()),
            ],
            options={
                'db_table': 'v_classifica_generale',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassificaPerLega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posizione', models.IntegerField()),
                ('totale_punti', models.IntegerField()),
            ],
            options={
                'db_table': 'v_classifica_politico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClassificaPolitico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posizione', models.IntegerField()),
                ('totale_punti', models.IntegerField()),
            ],
            options={
                'db_table': 'v_classifica_politico',
                'managed': False,
            },
        ),
    ]
