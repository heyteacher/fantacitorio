from django.db import connection
from django.core.management.base import BaseCommand
from django.conf import settings
from fc_classifiche_app.models import ClassificaGenerale, PunteggioPuntata
from fc_gestione_app.models import Punteggio,Squadra
from django.core.mail import send_mail
import os

class Command(BaseCommand):
    help = 'refresh sqlite classifiche'

    def add_arguments(self, parser):
   
        # Named (optional) arguments
        parser.add_argument(
            '--force',
            action='store_true',
            help='force refresh',
        )

    def handle(self, *args, **options):
 
        classifiche_filename = settings.DATABASES['db_classifiche']['NAME']

        commands = [{ 
                'action':'attach database %s' % classifiche_filename, 
                'query': "ATTACH DATABASE '%s' AS rankdb " % classifiche_filename
        },{ 'action':'drop classifica_generale on rankdb', 'query':
"""
drop table if exists rankdb.classifica_generale
"""
        },{ 'action':'create classifica_politico on rankdb', 'query':
"""
CREATE TABLE rankdb.classifica_generale ("posizione" integer NOT NULL PRIMARY KEY, "nome_squadra" varchar(200) NOT NULL, "totale_punti" integer NOT NULL, "squadra_id" integer NOT NULL, "site_id" integer NOT NULL, "leader_politico" varchar(100) NULL, "politico_1" varchar(100) NULL, "politico_10" varchar(100) NULL, "politico_11" varchar(100) NULL, "politico_2" varchar(100) NULL, "politico_3" varchar(100) NULL, "politico_4" varchar(100) NULL, "politico_5" varchar(100) NULL, "politico_6" varchar(100) NULL, "politico_7" varchar(100) NULL, "politico_8" varchar(100) NULL, "politico_9" varchar(100) NULL, "creato_il" datetime NULL, "fanfani" integer NOT NULL, "codice_squadra" varchar(20) NULL, "totale_leader_politico" integer NOT NULL, "totale_politico_1" integer NOT NULL, "totale_politico_10" integer NOT NULL, "totale_politico_11" integer NOT NULL, "totale_politico_2" integer NOT NULL, "totale_politico_3" integer NOT NULL, "totale_politico_4" integer NOT NULL, "totale_politico_5" integer NOT NULL, "totale_politico_6" integer NOT NULL, "totale_politico_7" integer NOT NULL, "totale_politico_8" integer NOT NULL, "totale_politico_9" integer NOT NULL)
"""
        },{ 'action':'create index classifica_generale_totale_punti_idx', 'query':
"""
CREATE INDEX rankdb.classifica_generale_totale_punti_idx ON classifica_generale (totale_punti DESC)
"""
        },{ 'action':'create index classifica_generale_squadra_id_idx', 'query':
"""
CREATE INDEX rankdb.classifica_generale_squadra_id_idx ON classifica_generale (totale_punti ASC)
"""
        },{ 'action':'drop classifica_politico on rankdb', 'query':
"""
drop table if exists rankdb.classifica_politico
"""
        },{ 'action':'create classifica_politico on ran', 'query':
"""
CREATE TABLE rankdb.classifica_politico ("posizione" integer NOT NULL PRIMARY KEY, "site_id" integer NOT NULL, "nome_politico" varchar(200) NOT NULL, "totale_punti" integer NOT NULL)
"""
        },{ 'action':'create index classifica_politico_totale_punti_idx', 'query':
"""
CREATE INDEX rankdb.classifica_politico_totale_punti_idx ON classifica_politico (totale_punti DESC)
"""
        },{ 'action':'drop classifica_per_lega on rankdb', 'query':
"""
drop table  if exists rankdb.classifica_per_lega
"""
        },{ 'action':'create classifica_per_lega on rankdb', 'query':
"""
CREATE TABLE rankdb.classifica_per_lega ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "posizione" integer NOT NULL, "lega_id" integer NOT NULL, "site_id" integer NOT NULL, "nome_lega" varchar(100) NOT NULL, "nome_squadra" varchar(200) NOT NULL, "totale_punti" integer NOT NULL, "squadra_id" integer NOT NULL)
"""
        },{ 'action':'create index classifica_per_lega_lega_id_totale_punti_idx', 'query':
"""
CREATE INDEX rankdb.classifica_per_lega_lega_id_totale_punti_idx ON classifica_per_lega (lega_id ASC, totale_punti DESC)
"""
        },{ 'action':'drop squadra_punti on rankdb', 'query':
"""
drop table  if exists rankdb.squadra_punti
"""
        },{ 'action':'create squadra_punti on rankdb', 'query':
"""
CREATE TABLE rankdb.squadra_punti (
	"id"	integer NOT NULL,
	"squadra_id"	integer NOT NULL,
	"squadra_name"	varchar(200) NOT NULL,
	"politico_id"	INTEGER NOT NULL,
	"politico_name"	varchar(200) NOT NULL,
	"puntata_numero"	integer NOT NULL,
	"puntata_data"	datetime NOT NULL,
	"punti"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
"""
       },{ 'action':'create squadra_punti_squadra_id_politico_id_idx', 'query':
"""
CREATE INDEX rankdb.squadra_punti_squadra_politico_idx ON squadra_punti (squadra_id ASC, politico_id ASC)
"""
        },{ 'action':'drop punteggio_puntata on rankdb', 'query':
"""
drop table if exists rankdb.punteggio_puntata
"""
        },{ 'action':'create punteggio_puntata on rankdb', 'query':
"""
CREATE TABLE rankdb.punteggio_puntata ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "puntata_numero" integer NOT NULL, "puntata_data" datetime NOT NULL, "site_id" integer NOT NULL, "politico_name" varchar(200) NOT NULL, "punti" integer NOT NULL, "creato_il" datetime NOT NULL)
"""
        },{ 'action':'populate classifica_per_lega on rankdb', 'query':
"""
insert into rankdb.classifica_per_lega (id, posizione,lega_id, site_id, nome_lega, squadra_id, nome_squadra, totale_punti) select id, posizione,lega_id, site_id,nome_lega, squadra_id, nome_squadra, totale_punti from v_classifica_per_lega
"""
        },{ 'action':'populate classifica_politico on rankdb', 'query':
"""
insert into rankdb.classifica_politico (posizione, site_id, nome_politico, totale_punti) select posizione, site_id, nome_politico, totale_punti from v_classifica_politico
"""
        },{ 'action':'populate squadra_punti on rankdb', 'query':
"""
insert into rankdb.squadra_punti (squadra_id, squadra_name, politico_id, politico_name, puntata_numero, puntata_data, punti) select squadra_id, squadra_name, politico_id,politico_name, puntata_numero, puntata_data, punti from v_squadra_punti
"""
        },{ 'action':'populate punteggio_puntata on rankdb', 'query':
"""
insert into rankdb.punteggio_puntata (puntata_numero, puntata_data, site_id, politico_name, punti, creato_il) select puntata_numero, puntata_data, site_id, politico_name, punti, v_punteggio_puntata.creato_il from v_punteggio_puntata
"""
        },{ 'action':'populate classifica_generale on rankdb', 'query':
"""
insert into rankdb.classifica_generale (posizione, squadra_id, site_id, codice_squadra, nome_squadra, creato_il, totale_punti, 
leader_politico, totale_leader_politico, 
politico_1, totale_politico_1, 
politico_2, totale_politico_2, 
politico_3, totale_politico_3, 
politico_4, totale_politico_4, 
politico_5, totale_politico_5, 
politico_6, totale_politico_6, 
politico_7, totale_politico_7, 
politico_8, totale_politico_8, 
politico_9, totale_politico_9, 
politico_10, totale_politico_10, 
politico_11, totale_politico_11,
fanfani) 
  select posizione, squadra_id, site_id, codice_squadra, nome_squadra, creato_il, totale_punti, 
  leader_politico, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = leader_politico_id),0), 
  politico_1, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "1_politico_id"),0),
  politico_2, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "2_politico_id"),0), 
  politico_3, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "3_politico_id"),0),
  politico_4, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "4_politico_id"),0), 
  politico_5, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "5_politico_id"),0),
  politico_6, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "6_politico_id"),0),
  politico_7, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "7_politico_id"),0),
  politico_8, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "8_politico_id"),0),
  politico_9, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "9_politico_id"),0),
  politico_10, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "10_politico_id"),0),
  politico_11, 
  COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "11_politico_id"),0), 
  fanfani from v_classifica_generale
"""
        },{ 'action':'detach database rankdb', 'query': "DETACH DATABASE rankdb"
}]
  
        try:
                punteggioPuntataCount = PunteggioPuntata.objects.count()
                classificaGeneraleCount = ClassificaGenerale.objects.count()
                squadraCount = Squadra.objects.count()
                punteggioCount = Punteggio.objects.count()
        except:
                punteggioPuntataCount = 0
                classificaGeneraleCount = 0
                squadraCount = 0
                punteggioCount = 0

        if not options['force'] and classificaGeneraleCount == squadraCount and punteggioPuntataCount == punteggioCount:
                self.stdout.write(self.style.SUCCESS('Skip refresh sqlite classifiche: force %s, ClassificaGenerale %s, Squadre %s, PunteggiPuntata %s, Punteggi %s' % (
                        options['force'],
                        classificaGeneraleCount,
                        squadraCount,
                        punteggioPuntataCount,
                        punteggioCount
                        )
                ))
        else:
                self.stdout.write(self.style.SUCCESS('Refresh sqlite classifiche: force %s, ClassificaGenerale %s, Squadre %s, PunteggiPuntata %s, Punteggi %s' % (
                        options['force'],
                        classificaGeneraleCount,
                        squadraCount,
                        punteggioPuntataCount,
                        punteggioCount
                        )
                ))
                with connection.cursor() as cursor:
                        for command in commands:
                                self.stdout.write(self.style.NOTICE(command['action']))    
                                cursor.execute(command['query'])
                self.stdout.write(self.style.SUCCESS('All Done'))

        send_mail(
                '[%s] Refresh sqlite classifiche' % (os.environ.get('STAGE'),),
                'force:\t\t%s\nClassificaGenerale:\t\t%s\nSquadre:\t%s\nPunteggiPuntata:\t\t%s\nPunteggi:\t%s' % (
                        options['force'],
                        classificaGeneraleCount,
                        squadraCount,
                        punteggioPuntataCount,
                        punteggioCount
                ),
                os.environ.get('DEFAULT_FROM_EMAIL'),
                [os.environ.get('EMAIL_MANAGER_EMAIL')]
        )
