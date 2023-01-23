from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings
from fc_classifiche_app.models import ClassificaGenerale

class Command(BaseCommand):
    help = 'refresh sqlite classifiche'


    def handle(self, *args, **options):
 
        classifiche_filename = settings.DATABASES['db_classifiche']['NAME']

        commands = [{ 
                'action':'attach database %s' % classifiche_filename, 
                'query': "ATTACH DATABASE '%s' AS rankdb " % classifiche_filename
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
insert into rankdb.classifica_per_lega select id, posizione,lega_id, nome_lega, squadra_id, nome_squadra, totale_punti from v_classifica_per_lega
"""
   },{ 'action':'populate classifica_politico on rackdb', 'query':
"""
insert into rankdb.classifica_politico select posizione, nome_politico, totale_punti from v_classifica_politico
"""
},{ 'action':'populate classifica_generale on rackdb', 'query':
"""
insert into rankdb.classifica_generale select posizione, squadra_id, nome_squadra, totale_punti from v_classifica_generale
"""
},{ 'action':'populate squadra_punti on rackdb', 'query':
"""
insert into rankdb.squadra_punti (squadra_id, squadra_name, politico_name, puntata_numero, puntata_data, punti) select squadra_id, squadra_name, politico_name, puntata_numero, puntata_data, punti from v_squadra_punti
"""
},{ 'action':'detach database rankdb', 'query': "DETACH DATABASE rankdb"
}]
        self.stdout.write(self.style.SUCCESS('Starting create Sqlite views'))
        self.stdout.write(self.style.SUCCESS('ClassificaGenerale count %s' % ClassificaGenerale.objects.count()))

        with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
  
        self.stdout.write(self.style.SUCCESS('ClassificaGenerale count %s' % ClassificaGenerale.objects.count()))
 
        self.stdout.write(self.style.SUCCESS('All Done'))