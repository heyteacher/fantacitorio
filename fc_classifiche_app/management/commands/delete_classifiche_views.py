from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates classifiche views'

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
   },{ 'action':'drop view v_punteggio_puntata', 'query':
"""
DROP VIEW IF EXISTS v_punteggio_puntata
"""
}]
        self.stdout.write(self.style.SUCCESS('Starting delete classifiche views'))
        with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
        self.stdout.write(self.style.SUCCESS('All Done'))