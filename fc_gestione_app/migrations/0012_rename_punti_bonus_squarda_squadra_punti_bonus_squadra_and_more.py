# Generated by Django 4.1.3 on 2022-12-05 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fc_gestione_app', '0011_rename_punti_squadra_punti_bonus_squarda_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squadra',
            old_name='punti_bonus_squarda',
            new_name='punti_bonus_squadra',
        ),
        migrations.AlterField(
            model_name='squadra',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_10_politico',
            field=models.ForeignKey(db_column='10_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_10_politico', to='fc_gestione_app.politico', verbose_name='10° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_11_politico',
            field=models.ForeignKey(db_column='11_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_11_politico', to='fc_gestione_app.politico', verbose_name='11° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_1_politico',
            field=models.ForeignKey(db_column='1_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_1_politico', to='fc_gestione_app.politico', verbose_name='1° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_2_politico',
            field=models.ForeignKey(db_column='2_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_2_politico', to='fc_gestione_app.politico', verbose_name='2° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_3_politico',
            field=models.ForeignKey(db_column='3_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_3_politico', to='fc_gestione_app.politico', verbose_name='3° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_4_politico',
            field=models.ForeignKey(db_column='4_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_4_politico', to='fc_gestione_app.politico', verbose_name='4° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_5_politico',
            field=models.ForeignKey(db_column='5_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_5_politico', to='fc_gestione_app.politico', verbose_name='5° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_6_politico',
            field=models.ForeignKey(db_column='6_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_6_politico', to='fc_gestione_app.politico', verbose_name='6° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_7_politico',
            field=models.ForeignKey(db_column='7_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_7_politico', to='fc_gestione_app.politico', verbose_name='7° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_8_politico',
            field=models.ForeignKey(db_column='8_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_8_politico', to='fc_gestione_app.politico', verbose_name='8° politico'),
        ),
        migrations.AlterField(
            model_name='squadra',
            name='number_9_politico',
            field=models.ForeignKey(db_column='9_politico_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='number_9_politico', to='fc_gestione_app.politico', verbose_name='9° politico'),
        ),
    ]
