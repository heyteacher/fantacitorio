from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates classifiche views'

    def handle(self, *args, **options):
        commands = [ 
        { 'action':'drop view v_classifica_per_lega', 'query':
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
   },{ 'action':'drop view v_punteggio_puntata', 'query':
"""
DROP VIEW IF EXISTS v_punteggio_puntata
"""
},{ 'action':'create view v_classifica_politico', 'query':
"""
CREATE VIEW v_classifica_politico
AS
 SELECT row_number() OVER (ORDER BY totale_punti desc) AS posizione,
    classifica_politico.site_id,
    classifica_politico.politico_name as nome_politico,
    classifica_politico.totale_punti,
    classifica_politico.politico_id
   FROM ( SELECT politico.id AS politico_id,
            politico.site_id,
            politico.name AS politico_name,
            sum(punteggio.punti) AS totale_punti
           FROM politico
             JOIN punteggio ON punteggio.politico_id = politico.id
          GROUP BY politico.id, politico.name
        ) classifica_politico
"""
   },{ 'action':'create view v_squadra_punti', 'query':
"""
CREATE VIEW v_squadra_punti
AS
select squadra_id, site_id, squadra_name, politico_name, puntata_numero, puntata_data, punti, politico_id 
FROM (
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra.leader_politico_id = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."1_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."2_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."3_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."4_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."5_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."6_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."7_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."8_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."9_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."10_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
UNION
SELECT
  squadra.id AS squadra_id,
  squadra.site_id,
  squadra.name AS squadra_name,
  squadra.creato_il,
  punteggio.punti,
  punteggio.politico_id,
  politico.name as politico_name,
  puntata.numero as puntata_numero,
  puntata.data as puntata_data
FROM squadra 
JOIN punteggio ON squadra."11_politico_id" = punteggio.politico_id
JOIN puntata ON punteggio.puntata_id = puntata.id AND squadra.creato_il <= puntata.data
JOIN politico ON punteggio.politico_id = politico.id
) squadra_punti
"""
   },{ 'action':'create view v_classifica_generale', 'query':
"""
CREATE VIEW v_classifica_generale
AS
SELECT 
    row_number() OVER ( ORDER BY totale_punti DESC) as posizione,
    classifica_squadre.squadra_id,
    classifica_squadre.site_id,
    classifica_squadre.squadra_codice as codice_squadra,
    classifica_squadre.squadra_name as nome_squadra,
    classifica_squadre.creato_il,
    classifica_squadre.totale_punti,
    classifica_squadre.leader_politico,
    classifica_squadre.leader_politico_id,
    classifica_squadre.politico_1,
    classifica_squadre."1_politico_id",
    classifica_squadre.politico_2,
    classifica_squadre."2_politico_id",
    classifica_squadre.politico_3,
    classifica_squadre."3_politico_id",
    classifica_squadre.politico_4,
    classifica_squadre."4_politico_id",
    classifica_squadre.politico_5,
    classifica_squadre."5_politico_id",
    classifica_squadre.politico_6,
    classifica_squadre."6_politico_id",
    classifica_squadre.politico_7,
    classifica_squadre."7_politico_id",
    classifica_squadre.politico_8,
    classifica_squadre."8_politico_id",
    classifica_squadre.politico_9,
    classifica_squadre."9_politico_id",
    classifica_squadre.politico_10,
    classifica_squadre."10_politico_id",
    classifica_squadre.politico_11,
    classifica_squadre."11_politico_id",
    classifica_squadre.fanfani
   FROM ( SELECT squadra.id AS squadra_id,
            squadra.site_id, 
            squadra.codice AS squadra_codice,
            squadra.name AS squadra_name,
            creato_il,
            (select name from politico where id = squadra.leader_politico_id) as leader_politico,
            squadra.leader_politico_id,
            (select name from politico where id = squadra."1_politico_id") as politico_1,
            squadra."1_politico_id",
            (select name from politico where id = squadra."2_politico_id") as politico_2,
            squadra."2_politico_id",
            (select name from politico where id = squadra."3_politico_id") as politico_3,
            squadra."3_politico_id",
            (select name from politico where id = squadra."4_politico_id") as politico_4,
            squadra."4_politico_id",
            (select name from politico where id = squadra."5_politico_id") as politico_5,
            squadra."5_politico_id",
            (select name from politico where id = squadra."6_politico_id") as politico_6,
            squadra."6_politico_id",
            (select name from politico where id = squadra."7_politico_id") as politico_7,
            squadra."7_politico_id",
            (select name from politico where id = squadra."8_politico_id") as politico_8,
            squadra."8_politico_id",
            (select name from politico where id = squadra."9_politico_id") as politico_9,
            squadra."9_politico_id",
            (select name from politico where id = squadra."10_politico_id") as politico_10,
            squadra."10_politico_id",
            (select name from politico where id = squadra."11_politico_id") as politico_11,
            squadra."11_politico_id",
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
          ) classifica_squadre
"""
   },{ 'action':'create view v_classifica_per_lega', 'query':
"""
CREATE VIEW v_classifica_per_lega
AS
 SELECT row_number() OVER (ORDER BY totale_punti DESC) AS id,
    row_number() OVER (PARTITION BY lega_squadra.lega_id ORDER BY v_classifica_generale.totale_punti DESC) AS posizione,
    lega_squadra.lega_id,
    lega.site_id,
    lega.name as nome_lega,
    v_classifica_generale.squadra_id,
    v_classifica_generale.nome_squadra,
    v_classifica_generale.totale_punti
   FROM v_classifica_generale
     JOIN lega_squadra ON v_classifica_generale.squadra_id = lega_squadra.squadra_id
     JOIN lega ON lega_squadra.lega_id = lega.id
"""
   },{ 'action':'create view v_punteggio_puntata', 'query':
"""
CREATE VIEW v_punteggio_puntata
AS
SELECT puntata.numero as puntata_numero, puntata."data" as puntata_data, puntata.site_id, politico."name" as politico_name, punteggio.punti, punteggio.creato_il 
FROM punteggio
INNER JOIN puntata ON puntata.id = punteggio.puntata_id
JOIN politico ON punteggio.politico_id = politico.id
"""
}]
        self.stdout.write(self.style.SUCCESS('Starting create classifiche views'))
        with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
        self.stdout.write(self.style.SUCCESS('All Done'))