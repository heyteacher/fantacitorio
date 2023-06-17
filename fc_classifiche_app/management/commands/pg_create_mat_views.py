from django.db import connection
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Creates postgresql materialized views'

    def handle(self, *args, **options):
      commands = [
        { 'action':'drop materialized view classifica_per_lega', 'query':
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
        },{ 'action':'create sequence squadra_punti_id_seq', 'query':
"""
CREATE SEQUENCE squadra_punti_id_seq START 1;
"""
        },{ 'action':'create materialized view squadra_punti', 'query':
"""
CREATE MATERIALIZED VIEW public.squadra_punti
AS
select nextval('squadra_punti_id_seq') as id, squadra_id, site_id, squadra_name, politico_id, politico_name, puntata_numero, puntata_data, punti FROM v_squadra_punti
WITH DATA
"""
        },{ 'action':'create index squadra_punti_squadra_id_politico_id_idx', 'query':
"""
CREATE INDEX squadra_punti_squadra_id_politico_id_idx
    ON public.squadra_punti USING btree
    (squadra_id ASC , politico_id ASC )
"""
        },{ 'action':'create index classifica_politico_totale_punti_idx', 'query':
"""

CREATE INDEX squadra_punti_punti_idx
    ON public.squadra_punti USING btree
    (punti DESC)
"""
        },{ 'action':'create sequence punteggio_puntata_id_seq', 'query':
"""
CREATE SEQUENCE punteggio_puntata_id_seq START 1;
"""
        },{ 'action':'create materialized view punteggio_puntata', 'query':
"""
CREATE MATERIALIZED VIEW public.punteggio_puntata
AS
select nextval('punteggio_puntata_id_seq') as id, puntata_numero, puntata_data, site_id, politico_name, punti, creato_il FROM v_punteggio_puntata
WITH DATA
"""
        },{ 'action':'create index view punteggio_puntata', 'query':
"""
CREATE INDEX punteggio_puntata_creato_id_idx
    ON public.punteggio_puntata USING btree
    (creato_il DESC)
"""
        },{ 'action':'create materialized view classifica_politico', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_politico
AS
select posizione, politico_id, site_id, nome_politico, totale_punti from v_classifica_politico
WITH DATA
"""
        },{ 'action':'create index on classifica_politico_politico_id_idx', 'query':
"""
CREATE INDEX classifica_politico_politico_id_idx
    ON public.classifica_politico USING btree
    (politico_id ASC)
"""
        },{ 'action':'create materialized view classifica_generale', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_generale
AS
 select posizione, squadra_id, site_id, codice_squadra, nome_squadra, creato_il, totale_punti, 
 leader_politico, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = leader_politico_id),0) as totale_leader_politico, 
 politico_1, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "1_politico_id"),0) as totale_politico_1,
 politico_2, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "2_politico_id"),0) as totale_politico_2,
 politico_3, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "3_politico_id"),0) as totale_politico_3,
 politico_4, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "4_politico_id"),0) as totale_politico_4,
 politico_5, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "5_politico_id"),0) as totale_politico_5,
 politico_6,
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "6_politico_id"),0) as totale_politico_6,
 politico_7, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "7_politico_id"),0) as totale_politico_7,
 politico_8, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "8_politico_id"),0) as totale_politico_8,
 politico_9, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "9_politico_id"),0) as totale_politico_9,
 politico_10, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "10_politico_id"),0) as totale_politico_10,
 politico_11, 
 COALESCE((select sum(punti) from squadra_punti where squadra_punti.squadra_id = v_classifica_generale.squadra_id AND politico_id = "11_politico_id"),0) as totale_politico_11,
 fanfani from v_classifica_generale
WITH DATA
"""
        },{ 'action':'create index classifica_generale_totale_punti_idx', 'query':
"""
CREATE INDEX classifica_generale_totale_punti_idx
    ON public.classifica_generale USING btree
    (totale_punti DESC)
"""
        },{ 'action':'create index classifica_generale_squadra_id_idx', 'query':
"""
CREATE INDEX classifica_generale_squadra_id_idx
    ON public.classifica_generale USING btree
    (totale_punti ASC)
"""
        },{ 'action':'create view materialized classifica_per_lega', 'query':
"""
CREATE MATERIALIZED VIEW public.classifica_per_lega
AS
select id, posizione,lega_id, site_id, nome_lega, squadra_id, nome_squadra, totale_punti from v_classifica_per_lega
WITH DATA
"""
        },{ 'action':'create index classifica_per_lega_lega_id_totale_punti_idx', 'query':
"""
CREATE INDEX classifica_per_lega_lega_id_totale_punti_idx
    ON public.classifica_per_lega USING btree
    (lega_id ASC, totale_punti DESC)
"""
}]
      self.stdout.write(self.style.SUCCESS('Starting create postgresql materialized views'))
      with connection.cursor() as cursor:
         for command in commands:
            self.stdout.write(self.style.NOTICE(command['action']))
            cursor.execute(command['query'])
      self.stdout.write(self.style.SUCCESS('All Done'))