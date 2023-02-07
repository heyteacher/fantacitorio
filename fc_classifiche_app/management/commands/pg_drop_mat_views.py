from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Drop postgresql materialized views'

    def handle(self, *args, **options):
      commands = [{ 'action':'drop materialized view classifica_per_lega', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS classifica_per_lega
"""
        },{ 'action':'drop materialized view classifica_generale', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS classifica_generale CASCADE
"""
        },{ 'action':'drop materialized view classifica_politico', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS classifica_politico
"""
        },{ 'action':'drop materialized view squadra_punti', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS squadra_punti
"""
        },{ 'action':'drop sequence squadra_punti_id_seq', 'query':
"""
DROP SEQUENCE if EXISTS squadra_punti_id_seq;
"""
        },{ 'action':'drop materialized view punteggio_puntata', 'query':
"""
DROP MATERIALIZED VIEW IF EXISTS punteggio_puntata
"""
        },{ 'action':'drop sequence punteggio_puntata_id_seq', 'query':
"""
DROP SEQUENCE if EXISTS punteggio_puntata_id_seq;
"""
        }]
      self.stdout.write(self.style.SUCCESS('Starting drop postgresql materialized views'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))