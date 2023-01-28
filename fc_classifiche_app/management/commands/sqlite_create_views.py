from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates Sqlite3 views'

    def handle(self, *args, **options):
        commands = [{ 'action':'drop view v_classifica_per_lega', 'query':
"""
DROP VIEW IF EXISTS  v_classifica_per_lega
"""
        },{ 'action':'drop view v_classifica_generale', 'query':
"""
DROP VIEW IF EXISTS  v_classifica_generale
"""
        },{ 'action':'drop view v_classifica_politico', 'query':
"""
DROP VIEW IF EXISTS v_classifica_politico
"""
        },{ 'action':'drop view v_squadra_punti', 'query':
"""
DROP VIEW IF EXISTS v_squadra_punti
"""
   },{ 'action':'create view v_classifica_generale', 'query':
"""
CREATE VIEW v_classifica_generale
AS
SELECT 
    row_number() OVER ( ORDER BY totale_punti DESC) as posizione ,
    classifica_squadre.squadra_id,
    classifica_squadre.squadra_codice as codice_squadra,
    classifica_squadre.squadra_name as nome_squadra,
    classifica_squadre.creato_il,
    classifica_squadre.totale_punti,
    classifica_squadre.leader_politico,
    classifica_squadre.politico_1,
    classifica_squadre.politico_2,
    classifica_squadre.politico_3,
    classifica_squadre.politico_4,
    classifica_squadre.politico_5,
    classifica_squadre.politico_6,
    classifica_squadre.politico_7,
    classifica_squadre.politico_8,
    classifica_squadre.politico_9,
    classifica_squadre.politico_10,
    classifica_squadre.politico_11,
    classifica_squadre.fanfani
   FROM ( SELECT squadra.id AS squadra_id,
            squadra.codice AS squadra_codice,
            squadra.name AS squadra_name,
            creato_il,
            (select name from politico where id = squadra.leader_politico_id) as leader_politico,
            (select name from politico where id = squadra."1_politico_id") as politico_1,
            (select name from politico where id = squadra."2_politico_id") as politico_2,
            (select name from politico where id = squadra."3_politico_id") as politico_3,
            (select name from politico where id = squadra."4_politico_id") as politico_4,
            (select name from politico where id = squadra."5_politico_id") as politico_5,
            (select name from politico where id = squadra."6_politico_id") as politico_6,
            (select name from politico where id = squadra."7_politico_id") as politico_7,
            (select name from politico where id = squadra."8_politico_id") as politico_8,
            (select name from politico where id = squadra."9_politico_id") as politico_9,
            (select name from politico where id = squadra."10_politico_id") as politico_10,
            (select name from politico where id = squadra."11_politico_id") as politico_11,
            (COALESCE((select fanfani from politico where id = squadra.leader_politico_id),0) +
             COALESCE((select fanfani from politico where id = squadra."1_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."2_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."3_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."4_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."5_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."6_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."7_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."8_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."9_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."10_politico_id"),0) +
             COALESCE((select fanfani from politico where id = squadra."11_politico_id"),0)) as fanfani,
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
"""
   },{ 'action':'create view v_classifica_per_lega', 'query':
"""
CREATE VIEW v_classifica_per_lega
AS
 SELECT row_number() OVER (ORDER BY totale_punti DESC) AS id,
    row_number() OVER (PARTITION BY lega_squadra.lega_id ORDER BY v_classifica_generale.totale_punti DESC) AS posizione,
    lega_squadra.lega_id,
    lega.name as nome_lega,
    v_classifica_generale.squadra_id,
    v_classifica_generale.nome_squadra,
    v_classifica_generale.totale_punti
   FROM v_classifica_generale
     JOIN lega_squadra ON v_classifica_generale.squadra_id = lega_squadra.squadra_id
     JOIN lega ON lega_squadra.lega_id = lega.id
   ORDER BY lega_squadra.lega_id, row_number() OVER (PARTITION BY lega_squadra.lega_id ORDER BY v_classifica_generale.totale_punti DESC)
"""
   },{ 'action':'create view v_classifica_politico', 'query':
"""
CREATE VIEW v_classifica_politico
AS
 SELECT row_number() OVER (ORDER BY totale_punti desc) AS posizione,
    classifica_politico.politico_name as nome_politico,
    classifica_politico.totale_punti
   FROM ( SELECT politico.id AS politico_id,
            politico.name AS politico_name,
            sum(punteggio.punti) AS totale_punti
           FROM politico
             JOIN punteggio ON punteggio.politico_id = politico.id
          GROUP BY politico.id, politico.name
          ORDER BY (sum(punteggio.punti)) DESC) classifica_politico
"""
   },{ 'action':'create view v_squadra_punti', 'query':
"""
CREATE VIEW v_squadra_punti
AS
select squadra_id, squadra_name, politico_name, puntata_numero, puntata_data, punti 
FROM (
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra.leader_politico_id = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."1_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."2_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."3_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."4_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."5_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."6_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."7_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."8_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."9_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."10_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON punteggio.puntata_id = puntata.id
AND squadra."11_politico_id" = punteggio.politico_id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
JOIN puntata ON punteggio.puntata_id = puntata.id
) ORDER BY squadra_name, puntata_numero, politico_name
"""
}]
        self.stdout.write(self.style.SUCCESS('Starting create Sqlite views'))

        with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])

        self.stdout.write(self.style.SUCCESS('All Done'))