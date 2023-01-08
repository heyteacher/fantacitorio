
# Progetto Web Fantacitorio 

[![GitHub license](https://img.shields.io/github/license/heyteacher/fantacitorio)](https://github.com//fantacitorio/blob/master/LICENSE) [![GitHub commit](https://img.shields.io/github/last-commit/heyteacher/fantacitorio)](https://github.com/heyteacher//fantacitorio/commits/main)

Progetto web __Fantacitorio__ nato dai `Google Sheet` gestiti da [@rosyilcapo](https://twitter.com/rosyilcapo)  per strutturare i dati in un database SQL ed automatizzare i calcoli delle classifiche. 

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

 https://fc-project-stage.adessospiana.it

le credenziali in sola lettura per accedere all' `admin` per la gestione dei contenuti: per:

- __login__: ``fantautente``
- __password__: ``fantacitorio``

## Per gli sviluppatori

Il progetto è basato sul framework `Django` con l'aggiunta dei seguenti moduli/backeng/tool python:

- `zappa`: tool per il rilascio stateless su cloud AWS
- `django-s3-sqlite`: backend database django per `sqlite` su `AWS S3`
- `django_s3_storage`: modulo django per la gestione dalle risorse statiche su `AWS S3`
- `django-dynamodb-cache`: bachend cache django per `AWS DynamoDB`
- `django-tables2`: modulo django che implementa una datadrid avanzata
- `django-filter`: modulo django che implementa filtri avanzati 
- `django-bootstrap3`: modulo django per utilizzare `bootstrap 3` nei template
- `django-import-export`: modulo Django per importazione ed espostazione dei dati
- `django-admin-autocomplete-filter`: modulo Django che implementa i filtri autocomplete nell'admin

La struttura del progetto:

- `_fc_project__`: il project Django:
- `fc_gestione_app`: app Django dedicata alla gestione delle squadre, le leghe i politici, le puntate e i punteggi
- `fc_classifiche_app`: app Django per la generazione/visualizzazione delle classifiche

### Prerequisiti

- Linux o WSL si Windows
- python3.9

### setup ambiente locale

- creazione del virtualenv che ospiterà Django in locale
  ```
  sudo apt install virtualenv
  virtualenv  venv --python python3.9 --pip 22.3.1
  ```

- rinominare `zappa_settings.json.template` in `zappa_settings.json`. Nella sezione dev contiene già le impostazioni per utilizzare il database locale `sqlite3`

- Attivazione del virtualenv creato
  ```
  source ve/bin/activate
  ```

- Installazione di Django e delle dipendenze contenute in requirente.txt
  ```
  pip install -r requirements.txt
  ```

- generazione delle tabelle di sistema della applicazione fc_gestione_app
  ```
  python manage.py migrate
  ```

- creazione della tabella cache DynamoDB
  ```
  python manage.py createcachetable
  ```

- caricamento dei dati aggiornati alla 6° puntata di propaganda
  ```
  python manage.py loaddata fc_gestione_app
  ```

- generazione delle viste dell'applicazione fc_classifiche_app
  ```
  python manage.py sqlite_create_views
  ```

- creazione super utente da utilizzare per autenticarsi al sito (es: `admin`)

  ```
  python manage.py createsuperuser --username <SUPER UTENTE>
  ```

- esecuzione in locale
  ```
  python manage.py runserver
  ```

- accedere a http://localhost:8000. Cliccare su `Admin` e autenticarsi tramite il super user creato

Per lo sviluppo in locale, è stato utilizzato `sqlite3` come database.

### Dump dei dati e creazione della fixture di fc_gestione_app

Per generare un dump del database per migrarlo presso un nuovo ambiente si utilizza il comando Django `dumpdata`

```
python manage.py dumpdata fc_gestione_app -o fc_gestione_app/fixtures/fc_gestione_app.json.bz2
```

### Rilascio in produzione  su AWS con Zappa

L'ambiente di produzione è rilasciato nel cloud `AWS` tramite `zappa` su una instanza `AWS RDS` di `PostgreSql`.

### Deploy su AWS

- dopo aver creato il database AWS RDS, configurare zappa per il proprio ambiente AWS edidando la sezione `production` del file`zappa_settings.json`

- deployare l'applicazione nel cloud
  ```
  zappa deploy production
  ```
  Al termine del deploy, viene visualizzato l' URL del sito rilasciato.
   
- creazione del tabelle nel database
  ```
  zappa manage production migrate
  ```

- creazione della tabella cache DynamoDB
  ```
  zappa manage production createcachetable
  ```

- creazione del super utente Django
  ```
  zappa invoke production "from django.contrib.auth.models import User; User.objects.     create_superuser('<SUPER USER>', '', '<PASSWORD>')" --raw
  ```

- caricamento dei dati iniziali del database
  ```
  zappa manage production loaddata fc_gestione_app
  ```

- creazione delle viste materializzate, i trigger e le procedure delle classifiche
  ```
  zappa manage production pg_create_mat_views
  ```

- refresh delle viste materializzate per popolarle
  ```
  zappa manage production pg_refresh_mat_views
  ```

### aggiornamento progetto su AWS 

Una volta deployato, se si effettuano modifiche in locale, il progetto può essere aggiornato con `update`
```
zappa update production
```

### Cancellazione del progetto su AWS

Per cancellare completamente l'applicazione utilizzare il seguente comando:

```
zappa undeploy production
```

Naturalmente il database `AWS RDS PostgreSql` vanno cancellate manualmente da AWS.

### Rilascio in ambiente di stage

L'ambiente di stage di AWS utilizza il database sqlite3 caricati in un bucket e acceduto da Django per le letture e le scritture, quindi è un utilizzabile per gli ambienti di `stage` e `local` ma non per la `production`

Dopo aver configurato la sezione `stage` di `zappa_settings.json` si rilascia su AWS con il seguente comando


```
zappa deploy stage
zappa manage stage migrate
zappa manage stage createcachetable
zappa invoke stage "from django.contrib.auth.models import User; User.objects.     create_superuser('<SUPER USER>', '', '<PASSWORD>')" --raw
zappa manage stage loaddata fc_gestione_app
zappa manage stage sqlite_create_views
```

## Comandi creazione progetto Django

Di seguito i comandi iniziali con cui sono stati creati:

```
django-admin startproject fc_project .
django-admin startapp fc_gestione_app
django-admin startapp fc_classifiche_app
```

Inizialmente il database di `fc_gestione_app` è stato creato graficamente con `PgAdmin ERD` poi generato nel postgres locale. Di seguito lo schema ER generato da PgAdmin ERD.

![Schema ER generato da PgAdmin ERD](./images/fantacitorio_dbschema.png)

Quindi i models di Django sono stati creati tramite `reverse engineering` con il comando `inspectdb`

```
python manage.py inspectdb > fc_gestione_app/models.py
```

I models Django di `fc_classifiche_app` sono stati creati a mano sulle tre viste materializzate e non gestite da Django (vedi nei models `managed=False`)

La configurazione inziale di `Zappa` è stata generata eseguendo il comando `zappa init` __eseguito dentro il virtualenv del progetto__. In questo modo riconosce l'ambiente Django installato nel virtualenv e crea il file `zappa_setting.json` tramite un wizard. 

## Per Contribuire

puoi contribuire:

* eseguendo un `fork` del progetto e contribuendo allo sviluppo 
*segnalando malfunzionamenti
* suggerendo nuove funzionalità

Aprendo una [segnalazione](https://github.com/heyteacher/fantacitorio/issues/new).
