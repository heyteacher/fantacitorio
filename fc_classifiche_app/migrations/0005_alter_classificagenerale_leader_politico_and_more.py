# Generated by Django 4.1.5 on 2023-01-24 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fc_classifiche_app', '0004_classificagenerale_leader_politico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificagenerale',
            name='leader_politico',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_10',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_11',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_8',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='classificagenerale',
            name='politico_9',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
