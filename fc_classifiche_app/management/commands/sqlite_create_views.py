from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates Sqlite3 views'

    def handle(self, *args, **options):
        queries = [
"""
DROP VIEW IF EXISTS  v_classifica_per_lega
""",
"""
DROP VIEW IF EXISTS  v_classifica_generale
""",
"""
DROP VIEW IF EXISTS v_classifica_politico
""",
"""
CREATE VIEW v_classifica_generale
AS
SELECT 
    row_number() OVER ( ORDER BY totale_punti DESC) as posizione ,
    classifica_squadre.squadra_id,
    classifica_squadre.squadra_name,
    classifica_squadre.totale_punti
   FROM ( SELECT squadra.id AS squadra_id,
            squadra.name AS squadra_name,
            (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra.leader_politico_id = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."1_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."2_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."3_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."4_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."5_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."6_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."7_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."8_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."9_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."10_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."11_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) AS totale_punti
           FROM squadra
          ORDER BY ((( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra.leader_politico_id = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."1_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."2_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."3_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."4_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."5_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."6_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."7_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."8_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."9_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."10_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data))) + (( SELECT COALESCE(sum(punteggio.punti), 0) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."11_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data)))) DESC) classifica_squadre
""",
"""
CREATE VIEW v_classifica_per_lega
AS
 SELECT row_number() OVER (ORDER BY totale_punti DESC) AS id,
    row_number() OVER (PARTITION BY lega_squadra.lega_id ORDER BY v_classifica_generale.totale_punti DESC) AS posizione,
    lega_squadra.lega_id,
    v_classifica_generale.squadra_id,
    v_classifica_generale.totale_punti
   FROM v_classifica_generale
     JOIN lega_squadra ON v_classifica_generale.squadra_id = lega_squadra.squadra_id
""",
"""
CREATE VIEW v_classifica_politico
AS
 SELECT row_number() OVER (ORDER BY totale_punti desc) AS posizione,
    classifica_politico.politico_id,
    classifica_politico.politico_name,
    classifica_politico.totale_punti
   FROM ( SELECT politico.id AS politico_id,
            politico.name AS politico_name,
            sum(punteggio.punti) AS totale_punti
           FROM politico
             JOIN punteggio ON punteggio.politico_id = politico.id
          GROUP BY politico.id, politico.name
          ORDER BY (sum(punteggio.punti)) DESC) classifica_politico
"""
]
        self.stdout.write(self.style.SUCCESS('Starting create Sqlite views'))

        with connection.cursor() as cursor:
         for query in queries:
               self.stdout.write(self.style.NOTICE('EXECUTE: %s' % query))
               cursor.execute(query)

        self.stdout.write(self.style.SUCCESS('All Done'))