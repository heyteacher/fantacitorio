from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'drop triggers, procedure, function which refresh Postgres materialized'

    def handle(self, *args, **options):
      commands = [{ 'action':'drop procedure refresh_mat_view', 'query':
"""
DROP PROCEDURE IF EXISTS public.refresh_mat_views
"""
        },{ 'action':'drop trigger refresh_mat_view on punteggio', 'query':
"""
DROP TRIGGER IF EXISTS refresh_mat_view ON public.punteggio;
"""
        },{ 'action':'drop trigger refresh_mat_view on lega_squadra', 'query':
"""
DROP TRIGGER IF EXISTS refresh_mat_view ON public.lega_squadra;
"""
        },{ 'action':'drop trigger refresh_mat_view on lega', 'query':
"""
DROP TRIGGER IF EXISTS refresh_mat_view ON public.lega;
"""
        },{ 'action':'drop function refresh_mat_view', 'query':
"""
DROP FUNCTION IF EXISTS public.refresh_mat_view
"""
}]
      self.stdout.write(self.style.SUCCESS('Starting drop triggers, function and procedure which refresh Postgres materialized views'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))