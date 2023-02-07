from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates triggers, function and procedure which refresh Postgres materialized views'

    def handle(self, *args, **options):
      commands = [{ 'action':'create procedure refresh_mat_view', 'query':
"""
CREATE OR REPLACE PROCEDURE public.refresh_mat_views(
	)
LANGUAGE 'sql'
AS $BODY$
REFRESH MATERIALIZED VIEW classifica_generale;
REFRESH MATERIALIZED VIEW classifica_per_lega;
REFRESH MATERIALIZED VIEW classifica_politico;
REFRESH MATERIALIZED VIEW squadra_punti;
REFRESH MATERIALIZED VIEW punteggio_puntata;
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
    REFRESH MATERIALIZED VIEW classifica_generale;
    REFRESH MATERIALIZED VIEW classifica_per_lega;
    REFRESH MATERIALIZED VIEW classifica_politico;
    REFRESH MATERIALIZED VIEW squadra_punti;
    REFRESH MATERIALIZED VIEW punteggio_puntata;
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
      self.stdout.write(self.style.SUCCESS('Starting create triggers, function and procedure which refresh Postgres materialized views'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))