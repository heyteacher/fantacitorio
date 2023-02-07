from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates postgresql materialized views'

    def handle(self, *args, **options):
      commands = [{ 'action':'create materialized view classifica_generale', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_generale
TABLESPACE pg_default
AS
 select posizione, squadra_id, codice_squadra, nome_squadra, creato_il, totale_punti, leader_politico, politico_1, politico_2, politico_3, politico_4, 
  politico_5, politico_6, politico_7, politico_8, politico_9, politico_10, politico_11, fanfani from v_classifica_generale
WITH DATA
"""
        },{ 'action':'create view materialized classifica_per_lega', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_per_lega
TABLESPACE pg_default
AS
select id, posizione,lega_id, nome_lega, squadra_id, nome_squadra, totale_punti from v_classifica_per_lega
WITH DATA
"""
        },{ 'action':'create materialized view classifica_politico', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_politico
TABLESPACE pg_default
AS
select posizione, nome_politico, totale_punti from v_classifica_politico
WITH DATA
"""
        },{ 'action':'create sequence squadra_punti_id_seq', 'query':
"""
CREATE SEQUENCE squadra_punti_id_seq START 1;
"""
        },{ 'action':'create materialized view squadra_punti', 'query':
"""
CREATE MATERIALIZED VIEW public.squadra_punti
TABLESPACE pg_default
AS
select nextval('squadra_punti_id_seq') as id, squadra_id, squadra_name, politico_name, puntata_numero, puntata_data, punti FROM v_squadra_punti
WITH DATA
"""
        },{ 'action':'create sequence punteggio_puntata_id_seq', 'query':
"""
CREATE SEQUENCE punteggio_puntata_id_seq START 1;
"""
        },{ 'action':'create materialized view punteggio_puntata', 'query':
"""
CREATE MATERIALIZED VIEW public.punteggio_puntata
TABLESPACE pg_default
AS
select nextval('punteggio_puntata_id_seq') as id, puntata_numero, puntata_data, politico_name, punti, creato_il FROM v_punteggio_puntata
WITH DATA
"""
}]
      self.stdout.write(self.style.SUCCESS('Starting create postgresql materialized views'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))