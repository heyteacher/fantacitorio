
# Progetto Web Fantacitorio 

[![GitHub license](https://img.shields.io/github/license/heyteacher/fantacitorio)](https://github.com//fantacitorio/blob/master/LICENSE) [![GitHub commit](https://img.shields.io/github/last-commit/heyteacher/fantacitorio)](https://github.com/heyteacher//fantacitorio/commits/main)

Progetto web __Fantacitorio__ nato dai `Google Sheet` gestiti da [@rosyilcapo](https://twitter.com/rosyilcapo)  per strutturare i dati in un database SQL ed visualizzare le classifiche (generale, per lega, politici). 

In particolare la base dati è stata creata partendo dal `Google Sheet` [* Fantacitorio 2022 - classifica generale PROVVISORIA](https://docs.google.com/spreadsheets/d/19RcqYZYyrCdjMHyFA2bcChaxnd7JIuzjXxYbKNRN3jM/edit?pli=1#gid=0).

__Fantacitorio__ è un _fanta game_ ideato dalla trasmissione __Propaganda Live__ di __La7__ nel 2021. 

Info disponibili:

- [Regolamento](https://www.la7.it/propagandalive/video/fantacitorio-16-02-2022-423442)
- [Monologo di __Valerio Aprea__](https://www.la7.it/embedded/la7?w=640&h=360&tid=player&content=423442)

Il progetto è composto da:

- una sezione pubblica dove sono visualizzate `classifica generale`, le `classifiche per lega`, e la `classifica politico`
- un'area di amministrazione protetta per la gestione dei contenuti:
  - `cariche`
  - `politici`
  - `squadre`
  - `leghe`
  - `associazioni lega-squadra`
  - `punteggi`
  - `puntate`

## Demo

Una demo del progetto è disponibile sul Cloud AWS al seguente indirizzo:

 https://classifiche-fantacitorio.adessospiana.it

le credenziali in sola lettura per accedere all' `admin` per la gestione dei contenuti per:

- __login__: ``fantautente``
- __password__: ``fantacitorio``

## Per gli sviluppatori

### librerie, dipendenze

Il progetto è basato sul framework `Django` con l'aggiunta dei seguenti moduli/backeng/tool python:

- `zappa`: tool per il rilascio stateless su cloud AWS
- `django`: storico framework CMS in `python` che, tra i tanti, ha dato i natali ad `Instagram`
- `django-s3-sqlite`: backend database django per `sqlite` su `AWS S3`
- `django_s3_storage`: modulo django per la gestione dalle risorse statiche su `AWS S3`
- `django-dynamodb-cache`: bachend cache django per `AWS DynamoDB`
- `django-tables2`: modulo django che implementa una datadrid avanzata
- `django-filter`: modulo django che implementa filtri avanzati 
- `django-bootstrap3`: modulo django per utilizzare `bootstrap 3` nei template
- `django-import-export`: modulo Django per importazione ed espostazione dei dati
- `django-admin-autocomplete-filter`: modulo Django che implementa i filtri autocomplete nell'admin

L'ambiente di produzione il database `sqlite` è sostituito con `PostgreSql` quindi i package `django-s3-sqlite` è sostituito con i driver python di `PostgreSql`:

- `psycopg2` 
- `psycopg2-binary` 

### struttura 

La struttura del progetto è la seguente:

- `_fc_project__`: il project Django:
- `fc_gestione_app`: app Django dedicata alla gestione delle squadre, le leghe i politici, le puntate e i punteggi tramite l'`admin` di Django
- `fc_classifiche_app`: app Django per la generazione/visualizzazione delle classifiche

### Prerequisiti

- Linux o WSL su Windows e forse anche Windows (non testato)
- python3.9 (è attualmente la versione massima supportata dalla `AWS Lambda` in python)

### setup ambiente locale

- creazione del virtualenv che ospiterà Django in locale
  ```
  sudo apt install virtualenv
  virtualenv  venv --python python3.9 --pip 22.3.1
  ```

- rinominare `zappa_settings.json.template` in `zappa_settings.json`. Nella sezione dev contiene già le impostazioni per utilizzare il database locale `sqlite3`

- Attivazione del virtualenv creato
  ```
  source venv/bin/activate
  ```

- Installazione di Django e delle dipendenze contenute in requirente.txt
  ```
  pip install -r requirements.txt
  ```

- generazione delle tabelle di sistema della applicazione fc_gestione_app e fc_classifiche_app
  ```
  python manage.py migrate fc_gestione_app --database default
  python manage.py migrate fc_classifiche_app --database db_classifiche 
  ```

- creazione super utente da utilizzare per autenticarsi al sito (es: `admin`)
  ```
  python manage.py createsuperuser --username <SUPER UTENTE>
  ```

- caricamento dei dati aggiornati alla 6° puntata di propaganda
  ```
  python manage.py loaddata fc_gestione_app
  ```

- generazione delle viste e refresh dei dati di fc_classifiche_app 
  ```
  python manage.py sqlite_create_views
  python manage.py sqlite_refresh_classifiche
  ```

- esecuzione in locale
  ```
  python manage.py runserver
  ```

- accedere a http://localhost:8000, saranno mostrate le classifiche, mentre par accedere all'`admin` cliccare sulla rotellina in alto a destra, quindi autenticarsi tramite il super user creato

### Dump dei dati e creazione della fixture di fc_gestione_app

Per generare una `fixture` del database per migrarlo presso un nuovo ambiente si utilizza il comando Django `dumpdata`

```
python manage.py dumpdata fc_gestione_app -o fc_gestione_app/fixtures/fc_gestione_app.json.bz2
```

Per caricare la `fixture` utilizzare il comando load data (in automatico cerca le fixture dentro l'app0)

```
python manage.py loaddata fc_gestione_app
```

Le `fixture` sono agnostiche rispetto al database utilizzato, quindi possono essere utilizzate per migrare i data verso qualsiasi database supportato da Django.

### Rilascio in stage

La configurazione dell'ambiente di stage su cloud 'AWS' è la sequente:

- Django distribuito sul cloud `AWS` in modalità `serverless` tramite `AWS Lambda` e `AWS Api gateway` tramite `zappa`

- 2 database `sqlite` (`gestione` e `classifiche`) caricati in un `AWS S3 bucket` e acceduto dalla `AWS Lambda` di Django per le letture e le scritture, tramite il pacchetto `django-s3-sqlite`.

- `cache Django` attiva su backed `AWS DynamoDB` per le `session` e la `pagine` tramite il pacchetto `django-dynamodb-cache`

- file statici forniti da un `AWS S3 bucket`, built-in `Django`

- `AWS event` schedulato ogni ora per aggiornamento del database classifiche partendo dai dati del database gestione.

Il razionale di avere due database distinti, uno per la gestione dei dati e uno per le classifiche è  separare completamente `presentation` dei dati (database classifiche) dalla `administration` dei dati (database gestione):

- il database classifiche è readonly aggiornato ogni ora ottimizzato per la visualizzazione (join risolti, poche tabelle di grandi dimensione non in 3° forma normale). Quando viene consultato dalla lambda viene scaricato da S3 ma non sovrascritto in quanto mai modificato. Quindi può essere acceduto concorrentemente ed è il database della parte pubblica del sito.

- il datatanse di gestione (che è il default) è il classico database in 3° forma normale gestito tramite la `Admin` di `Django` ossia un `CRUD`. Durante le modifiche, viene scaricato da S3, modificato tramite query di INSERT, UPDATE, DELETE e ricaricato su S3. Non supporta accessi concorrenti. E' il database della parte privata di amministrazione del sito, acceduta dall'amministratore per aggiornare i dati.

Il vantaggio di questa configurazione è che utilizza risorse AWS il cui costo è calcolato esclusivamente a consumo e non utilizza risorse AWS a canone come i classici database relazionali (`AWS RDS` con `PostgreSQL`, `Oracle`, `MariaDB`, `MySql`, `Sql Server` ) 

Paradossalmente, se nessuno accede al sito, l'infrastuttura non ha costo.

La configurazione di `Zappa` per il rilascio su AWS è nella  sezione `stage` di `zappa_settings.json`

Come pre-requisito è necessario un account AWS personale con le chiavi configurate in locale per l'accesso all'infartruttura. Di seguito i comandi `Zappa` per il rilascio dell'ambiente di stage: 

1. deploy dell'ambiente (solo la prima volta)
   ```
   zappa deploy stage
   ```
   per aggiornare l'ambiente le volte successive
   ```
   zappa update stage
   ```
   Al termine dell'esecuzione di `deploy` e `update`, se non vi sono errori, viene mostrato il URL del sito rilasciato all'interno della proprio cloud AWS.

1. generazione delle tabelle di sistema della applicazione fc_gestione_app
   ```
   zappa manage stage migrate fc_classifiche_app "--database db_classifiche"
   zappa manage stage migrate
   ```

1. creazione dell'utente superuser di amministrazione
   ```
   zappa invoke stage "from django.contrib.auth.models import User; User.objects.     create_superuser('<SUPER USER>', '', '<PASSWORD>')" --raw
   ```

1. la prima volta: creazione della tabella di caching `AWS DynamoDB`  
   ```
    zappa manage stage createcachetable 
   ```

1. la prima volta: caricamento dei dati presenti nella fixture di fc_gestiona_app 
   ```
   zappa manage stage loaddata fc_gestione_app
   ```

1. creazione delle viste classifiche
   ```
   zappa manage stage sqlite_create_views
   ```

1. primo refresh delle classifiche (comando poi eseguito ogni ora dal `AWS Event`)
   ```
   zappa manage stage sqlite_refresh_views
   ```


### Rilascio in produzione  su AWS con Zappa

L'ambiente di produzione, a differenza dell'ambiente di stage, utilizza come database una instanza `AWS RDS` di `PostgreSql`.

1. configurare la sezione `production` del file`zappa_settings.json`

1. deployare l'applicazione nel cloud
  ```
  zappa deploy production
  zappa manage production migrate
  zappa manage production createcachetable
  zappa invoke production "from django.contrib.auth.models import User; User.objects.     create_superuser('<SUPER USER>', '', '<PASSWORD>')" --raw
  zappa manage production loaddata fc_gestione_app
  zappa manage production pg_create_views
  zappa manage production pg_refresh_classifiche
  ```

### aggiornamento progetto su AWS 

Una volta deployato, il progetto può essere aggiornato applicando le modifiche locali al progetto con il comando `update`. Ad esempio, per l'ambiente di produzione:

```
zappa update production
```

### Cancellazione del progetto su AWS

Per cancellare completamente l'applicazione su AWS, utilizzare il comando di `undeploy`. Ad esempio, per l'ambiente di produzione:

```
zappa undeploy production
```

Il database di produzione `AWS RDS PostgreSql` ed gli `AWS S3 bucket` vanno cancellati manualmente da AWS in quanto non gestiti da `Zappa`

## Comandi creazione progetto Django

Di seguito i comandi iniziali con cui sono stati creati:

```
django-admin startproject fc_project .
django-admin startapp fc_gestione_app
django-admin startapp fc_classifiche_app
```

Inizialmente il database di `fc_gestione_app` è stato creato graficamente con `PgAdmin ERD` poi generato nel postgres locale. 

Di seguito lo schema ER generato da PgAdmin ERD:

![Schema ER generato da PgAdmin ERD](./images/fantacitorio_dbschema.png)

Quindi i models di Django sono stati creati tramite `reverse engineering` con il comando `inspectdb`

```
python manage.py inspectdb > fc_gestione_app/models.py
```

I models Django di `fc_classifiche_app` sono stati creati manualmente sulle tre viste materializzate e non gestite da Django (vedi nei models `managed=False`)

La configurazione inziale di `Zappa` è stata generata eseguendo il comando `zappa init` __eseguito dentro il virtualenv del progetto__. In questo modo riconosce l'ambiente Django installato nel virtualenv e crea il file `zappa_setting.json` tramite un wizard. 

## Per Contribuire

puoi contribuire:

* eseguendo un `fork` del progetto e contribuendo allo sviluppo 
* segnalando malfunzionamenti
* suggerendo nuove funzionalità

Aprendo una [segnalazione](https://github.com/heyteacher/fantacitorio/issues/new).
