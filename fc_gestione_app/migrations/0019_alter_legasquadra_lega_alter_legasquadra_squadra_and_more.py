# Generated by Django 4.1.5 on 2023-01-06 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "fc_gestione_app",
            "0018_remove_squadra_squadra_name_unique_squadra_codice_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="legasquadra",
            name="lega",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="fc_gestione_app.lega"
            ),
        ),
        migrations.AlterField(
            model_name="legasquadra",
            name="squadra",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="fc_gestione_app.squadra",
            ),
        ),
        migrations.AlterField(
            model_name="politico",
            name="carica",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="fc_gestione_app.carica"
            ),
        ),
        migrations.AlterField(
            model_name="punteggio",
            name="politico",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="fc_gestione_app.politico",
            ),
        ),
        migrations.AlterField(
            model_name="punteggio",
            name="puntata",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="fc_gestione_app.puntata",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="leader_politico",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="leader",
                to="fc_gestione_app.politico",
                verbose_name="leader",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_10_politico",
            field=models.ForeignKey(
                db_column="10_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_10_politico",
                to="fc_gestione_app.politico",
                verbose_name="10° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_11_politico",
            field=models.ForeignKey(
                db_column="11_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_11_politico",
                to="fc_gestione_app.politico",
                verbose_name="11° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_1_politico",
            field=models.ForeignKey(
                db_column="1_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_1_politico",
                to="fc_gestione_app.politico",
                verbose_name="1° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_2_politico",
            field=models.ForeignKey(
                db_column="2_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_2_politico",
                to="fc_gestione_app.politico",
                verbose_name="2° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_3_politico",
            field=models.ForeignKey(
                db_column="3_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_3_politico",
                to="fc_gestione_app.politico",
                verbose_name="3° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_4_politico",
            field=models.ForeignKey(
                db_column="4_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_4_politico",
                to="fc_gestione_app.politico",
                verbose_name="4° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_5_politico",
            field=models.ForeignKey(
                db_column="5_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_5_politico",
                to="fc_gestione_app.politico",
                verbose_name="5° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_6_politico",
            field=models.ForeignKey(
                db_column="6_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_6_politico",
                to="fc_gestione_app.politico",
                verbose_name="6° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_7_politico",
            field=models.ForeignKey(
                db_column="7_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_7_politico",
                to="fc_gestione_app.politico",
                verbose_name="7° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_8_politico",
            field=models.ForeignKey(
                db_column="8_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_8_politico",
                to="fc_gestione_app.politico",
                verbose_name="8° politico",
            ),
        ),
        migrations.AlterField(
            model_name="squadra",
            name="number_9_politico",
            field=models.ForeignKey(
                db_column="9_politico_id",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="number_9_politico",
                to="fc_gestione_app.politico",
                verbose_name="9° politico",
            ),
        ),
    ]