from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Creates Sqlite3 views'

    def handle(self, *args, **options):
        commands = [{ 'action':'attach database classifiche', 'query':
"""
ATTACH DATABASE './rankdb.sqlite3' AS rankdb
"""
        },{ 'action':'clean classifica_generale on rackdb', 'query':
"""
delete from rankdb.classifica_generale
"""
        },{ 'action':'clean classifica_politico on rackdb', 'query':
"""
delete from rankdb.classifica_politico
"""
        },{ 'action':'clean classifica_per_lega on rackdb', 'query':
"""
delete from rankdb.classifica_per_lega
"""
   },{ 'action':'populate classifica_per_lega on rackdb', 'query':
"""
insert into rankdb.classifica_per_lega select id, posizione,lega_id, nome_lega, nome_squadra, totale_punti from v_classifica_per_lega
"""
   },{ 'action':'populate classifica_politico on rackdb', 'query':
"""
insert into rankdb.classifica_politico select posizione, nome_politico, totale_punti from v_classifica_politico
"""
},{ 'action':'populate classifica_generale on rackdb', 'query':
"""
insert into rankdb.classifica_generale select posizione, nome_squadra, totale_punti from v_classifica_generale
"""
},{ 'action':'detach database rankdb', 'query':
"""
DETACH DATABASE rankdb
"""
}]
        self.stdout.write(self.style.SUCCESS('Starting create Sqlite views'))

        with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])

        self.stdout.write(self.style.SUCCESS('All Done'))