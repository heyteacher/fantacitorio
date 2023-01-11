from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates Postgres materialized views, related procedure and related triggers'

    def handle(self, *args, **options):
      commands = [{ 'action':'drop materialized view v_classifica_per_lega', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS v_classifica_per_lega
"""
        },{ 'action':'drop materialized view v_classifica_generale', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS v_classifica_generale CASCADE
"""
        },{ 'action':'drop view materialized v_classifica_politico', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS v_classifica_politico
"""
        },{ 'action':'create view materialized v_classifica_generale', 'query':
"""
CREATE MATERIALIZED VIEW public.v_classifica_generale
TABLESPACE pg_default
AS
 SELECT row_number() OVER (ORDER BY 1::integer) AS posizione,
    classifica_squadre.squadra_id,
    classifica_squadre.squadra_name,
    classifica_squadre.totale_punti
   FROM ( SELECT squadra.id AS squadra_id,
            squadra.name AS squadra_name,
            (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra.leader_politico_id = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."1_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."2_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."3_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."4_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."5_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."6_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."7_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."8_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."9_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."10_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."11_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) AS totale_punti
           FROM squadra
          ORDER BY ((( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra.leader_politico_id = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."1_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."2_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."3_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."4_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."5_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."6_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."7_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."8_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."9_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."10_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone))) + (( SELECT COALESCE(sum(punteggio.punti), 0::bigint) AS "coalesce"
                   FROM punteggio
                     JOIN puntata ON punteggio.puntata_id = puntata.id
                  WHERE squadra."11_politico_id" = punteggio.politico_id AND squadra.creato_il <= (puntata.data + '21:15:00'::time without time zone)))) DESC) classifica_squadre
WITH DATA"""
        },{ 'action':'create view materialized v_classifica_per_lega', 'query':
"""
CREATE MATERIALIZED VIEW public.v_classifica_per_lega
TABLESPACE pg_default
AS
 SELECT row_number() OVER (ORDER BY 1::integer) AS id,
    row_number() OVER (PARTITION BY lega_squadra.lega_id ORDER BY v_classifica_generale.totale_punti DESC) AS posizione,
    lega_squadra.lega_id,
    v_classifica_generale.squadra_id,
    v_classifica_generale.totale_punti
   FROM v_classifica_generale
     JOIN lega_squadra ON v_classifica_generale.squadra_id = lega_squadra.squadra_id
WITH DATA
"""
        },{ 'action':'create view materialized v_classifica_politico', 'query':
"""
CREATE MATERIALIZED VIEW public.v_classifica_politico
TABLESPACE pg_default
AS
 SELECT row_number() OVER (ORDER BY 1::integer) AS posizione,
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
WITH DATA
"""
        },{ 'action':'create procedure refresh_mat_view', 'query':
"""
CREATE OR REPLACE PROCEDURE public.refresh_mat_views(
	)
LANGUAGE 'sql'
AS $BODY$
REFRESH MATERIALIZED VIEW v_classifica_generale;
REFRESH MATERIALIZED VIEW v_classifica_per_lega;
REFRESH MATERIALIZED VIEW v_classifica_politico;
$BODY$
"""
        },{ 'action':'create function refresh_mat_view', 'query':
"""
CREATE OR REPLACE FUNCTION public.refresh_mat_view()
    RETURNS trigger
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE NOT LEAKPROOF
AS $BODY$
begin
    REFRESH MATERIALIZED VIEW v_classifica_generale;
    REFRESH MATERIALIZED VIEW v_classifica_per_lega;
    REFRESH MATERIALIZED VIEW v_classifica_politico;
    return null;
end 
$BODY$
"""
        },{ 'action':'create trigger refresh_mat_view on punteggio', 'query':
"""
CREATE OR REPLACE TRIGGER refresh_mat_view
    AFTER INSERT OR DELETE OR TRUNCATE OR UPDATE 
    ON public.punteggio
    FOR EACH STATEMENT
    EXECUTE FUNCTION public.refresh_mat_view();
"""
        },{ 'action':'create trigger refresh_mat_view on lega_squadra', 'query':
"""
CREATE OR REPLACE TRIGGER refresh_mat_view
    AFTER INSERT OR DELETE OR TRUNCATE OR UPDATE 
    ON public.lega_squadra
    FOR EACH STATEMENT
    EXECUTE FUNCTION public.refresh_mat_view();
"""
        },{ 'action':'create trigger refresh_mat_view on lega', 'query':
"""
CREATE OR REPLACE TRIGGER refresh_mat_view
    AFTER INSERT OR DELETE OR TRUNCATE OR UPDATE 
    ON public.lega
    FOR EACH STATEMENT
    EXECUTE FUNCTION public.refresh_mat_view();
"""
}]
      self.stdout.write(self.style.SUCCESS('Starting create Postgres materialized views, related procedure and related triggers'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))