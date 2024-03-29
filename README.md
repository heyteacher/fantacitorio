
# Fantacitorio in _Django_ su AWS con _Zappa_ (2022-2023)

[![GitHub license](https://img.shields.io/github/license/heyteacher/fantacitorio)](https://github.com//fantacitorio/blob/master/LICENSE) 
[![GitHub commit](https://img.shields.io/github/last-commit/heyteacher/fantacitorio)](https://github.com/heyteacher/fantacitorio/commits/main) 
[![Django versions](https://img.shields.io/badge/Django_versions-4.0_4.1_4.2_-blue)](https://github.com/django/django) 
[![Python versions](https://img.shields.io/badge/Python_versions-3.7_3.8_3.9-yellow)](https://www.python.org/downloads/release/python-390/)

Sito web [Classifiche Fantacitorio](https://classifiche-fantacitorio.adessospiana.it) nato dai `Google Sheet` gestiti da [@rosyilcapo](https://twitter.com/rosyilcapo)  per gestire i dati in un database SQL ed visualizzare le classifiche (generale, per lega, politici, punteggi). 

In particolare la base dati è stata creata partendo dal `Google Sheet` [* Fantacitorio 2022 - classifica generale PROVVISORIA](https://docs.google.com/spreadsheets/d/19RcqYZYyrCdjMHyFA2bcChaxnd7JIuzjXxYbKNRN3jM/edit?pli=1#gid=0).

__Fantacitorio__ è un _fanta game_ ideato dalla trasmissione __Propaganda Live__ di __La7__ nel 2021. 

Info disponibili:

- [Regolamento](https://www.la7.it/propagandalive/video/fantacitorio-16-02-2022-423442)
- [Monologo di __Valerio Aprea__](https://www.la7.it/embedded/la7?w=640&h=360&tid=player&content=423442)

Il sito web realizzato dai sorgenti di questo progetto GitHub è raggiungibile al seguente indirizzo: https://classifiche-fantacitorio.adessospiana.it 

## Struttura del sito

Il progetto è composto da:

- un sito pubblico dove sono visualizzate la `classifica generale`, le `classifiche per lega`, la `classifica politico` ed i `punteggi`. 

  Inoltre, cliccando su una squadra, è mostrato il suo `dettaglio` costituito dalla `formazione`, i `fanfani` utilizzati, il posizionamento in classifica generale e nelle leghe nonchè i `punteggi` acquisiti dai politici in formazione.

- un'area riservata di `amministrazione` protetta da autenticazione, per gestire, importare, esportare i contenuti:
  - `cariche`
  - `politici`
  - `squadre`
  - `leghe`
  - `associazioni lega-squadra`
  - `punteggi`
  - `puntate`

## Demo Area Riservata

E' disponibile una demo dell'area riservata nell'ambiente di stage https://stage-classifiche-fantacitorio.adessospiana.it/admin autenticandosi con le credenziali:

- __login__: `fantautente`
- __password__: `fantacitorio`


## Area Developer

In questa sezione viene descritto nel dettaglio lo sviluppo, il popolamento del database e il deploy sul cloud AWS. Prerequisito per approcciare questa sezione è di avere una conoscenza almeno base dei seguenti strumenti:

- il linguaggio di programmazione `Python`
- il framework `Django`
- il framework `Zappa`
- il database `CockroachDb` (PostgreSql) e `sqlite`
- il cloud `AWS` (`Amazon Web Services`) e nello specifico:
  - `AWS S3`: l'object storage di AWS
  - `AWS Api Gateway`
  - `AWS Lambda` l'infrastruttura `Serverless/FaaS` (`Function as a Service`)
  - `AWS RDS` il servizio cloud dei DBMS 
  - `AWS CloudFront` la `CDN` (`Content Delivery Network`) di AWS
  - `AWS Route53` il servizio di gestione `DNS` dei domini in  AWS
  - `AWS Certificate` il servizio per creare certificati SSL validi

### Il progetto Django

Il progetto è basato sul framework `Django` caricato sul Cloud AWS tramite `Zappa`. La lista dei `package python` utilizzati dal progetto sono:

- [django](https://github.com/django/django): storico framework CMS in `python` che, tra i tanti, ha dato i natali ad `Instagram`

- [zappa](https://github.com/zappa/Zappa): tool per il rilascio `serverless` su cloud AWS

- [django_s3_storage](https://github.com/etianen/django-s3-storage): modulo django per la gestione dalle risorse statiche su `AWS S3`

- [django-dynamodb-cache](https://github.com/xncbf/django-dynamodb-cache): bachend cache django per `AWS DynamoDB`

- [django-tables2](https://github.com/jieter/django-tables2): modulo django che implementa una datagrid avanzata

- [django-filter](https://github.com/carltongibson/django-filter): modulo django che implementa filtri avanzati 

- [django-bootstrap5](https://github.com/zostera/django-bootstrap5): modulo django per utilizzare `bootstrap 3` nei template

- [django-import-export](ttps://github.com/django-import-export/django-import-export): modulo Django per importazione ed espostazione dei dati

- [django-admin-autocomplete-filter](https://github.com/farhan0581/django-admin-autocomplete-filter): modulo Django che implementa i filtri autocomplete nell'admin

- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar): modulo Django mostra metriche delle query, template utilizzati, messaggi di log, variabili di sistema, insomma tutto ciò che serve per fare debugging e tuning del sistema

#### Backend

Django supporta diversi backend:

- supporto ufficiale per `MariaDB`, `MySQL`, `Oracle` e `PostgreSQL` (di conseguenza supporta `AWS RDS PostgreSQL` e `AWS Aurora`)

- backend di terze parti `CockroachDB`, `Firebird`, `Google Cloud Spanner`, `Microsoft SQL Server`, `Snowflake`, `TiDB`, `YugabyteDB`

Per i dettaglio fare rifermimento alla documentaziond del [Backend Django](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)

Questo progetto utilizza come database di principale per la gestione dei contenuti dalla sezione riservata [CockroachDB](https://cockroachlabs.cloud) un servizio serverless basato su `PostgreSQL`, mentre per le classifiche e la parte pubblicà è utilizzato il backend Sqlite su `AWS S3`. Di seguito i moduli Django:

- [django-cockroachdb](https://github.com/cockroachdb/django-cockroachdb): backend database django per `CockroachDB`

- [psycopg2](https://github.com/psycopg/psycopg2): sorgenti driver di `PostgreSQL` per `python`

- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): binary del driver di `PostgreSQL` per `python`

- [django-s3-sqlite](https://github.com/FlipperPA/django-s3-sqlite): backend database django per `sqlite` su `AWS S3`

### Struttura 

La struttura del progetto è costituita da un Django `project` a due Django `app`:

- `fc_project`: il project che contiene i `settings` e `url resolver`  
- `fc_gestione_app`: app dedicata alla gestione delle squadre, le leghe i politici, le puntate e i punteggi tramite l'`admin` di Django
- `fc_classifiche_app`: app per la generazione/visualizzazione delle classifiche

### Prerequisiti

- `Linux` o `WSL` su `Windows` 
- `python3.9` (è attualmente la versione massima supportata dalla `AWS Lambda` in python. Attenzione `python3.10` attualmente non è supportato da `AWS Lambda`)

### Setup ed esecuzione in locale

L'ambiente in locale è necessario sia per lo sviluppo dell'applicazione che per il deploy su `AWS`. Di seguito le istruzioni per configurare l'ambiente locale:

- creazione del virtualenv che ospiterà Django in locale
  ```
  sudo apt install virtualenv
  virtualenv  venv --python python3.9 --pip 23.1.2
  ```

- rinominare `zappa_settings.json.template` in `zappa_settings.json`. 
Nella sezione `local` contiene già le impostazioni per utilizzare il database locale `sqlite3` mentre bisogna creare un database di stage su su [Cockroach Labs](https://www.cockroachlabs.com/) e impostare le credenziali 

- Attivazione del virtualenv creato
  ```
  source venv/bin/activate
  ```

- Installazione di Django e delle dipendenze contenute in requirements.txt
  ```
  pip install -r requirements.txt
  ```

- generazione delle tabelle di sistema della applicazione fc_gestione_app. Si utilizza il `database routing` per gestire il database di principale e quello delle classifiche. Per il database classifiche si esegue una migrazione fake in quanto la tabelle sono generate tramite il comando di refresh classifiche
  ```
  python manage.py migrate fc_gestione_app --database default
  python manage.py migrate fc_classifiche_app --fake 
  ```

- creazione super utente da utilizzare per autenticarsi al sito (es: `admin`)
  ```
  python manage.py createsuperuser --username <SUPER UTENTE>
  ```

- caricamento dei dati (`fixture`) aggiornati all'ultima puntata
  ```
  python manage.py loaddata fc_gestione_app
  ```

- generazione delle viste e refresh dei dati di fc_classifiche_app 
  ```
  python manage.py create_classifiche_views
  python manage.py sqlite_refresh_classifiche
  ```

- esecuzione in locale di Django
  ```
  python manage.py runserver
  ```

- accedere a http://localhost:8000, saranno mostrate le classifiche, mentre par accedere all'`admin` cliccare sulla rotellina in alto a destra, quindi autenticarsi tramite il super user creato

### Dump dei dati e creazione della fixture di fc_gestione_app

Per generare una `fixture` del database e per migrarlo presso un nuovo ambiente si utilizza il comando Django `dumpdata`

```
python manage.py dumpdata fc_gestione_app -o fc_gestione_app/fixtures/fc_gestione_app.json.bz2
```

Per caricare la `fixture` utilizzare il comando load data (in automatico cerca le fixture dentro l'app0)

```
python manage.py loaddata fc_gestione_app
```

Le `fixture` sono agnostiche rispetto al database utilizzato, quindi possono essere utilizzate per migrare i data verso qualsiasi backend supportato da Django.

## architettura su AWS

`Zappa` è lo strumento che permette di deployare `Django` , gestendo ambienti separati, ad esempip `stage` e `production`. 

Nel dettaglio l'architettura del sito sul Cloud:

- Django distribuito sul cloud `AWS` in modalità  

- __CDN__: `AWS Cloudfront` è il punto di ingresso dalla applicazione. Si occupa della distribuzione dei contenuti effettuando il routing delle richieste verso la parte statica `S3` oppure `Django` servito dalle `AWS Api Gateway`

- __DNS__: gestito da `AWS Route53` e certificati di dominio HTTPS generati e gestiti da `AWS Certificate` e configurati sia sul `AWS Cloudfront` che `AWS Api Gateway`    

- __Django__: servito in modalità serverless da `Zappa` che effettua il deploy di Django sul cloud `AWS` mediante servizi `serverless` tramite `AWS Lambda` e `AWS Api Gateway` 

- __Database__: l'architettura sia per l'ambiente di  `stage` che `production` ricalca quella dell'ambiente di sviluppo `local`
 
 
  - database `default`: servito esternamente da `CockroachDB` 

  - database `classifiche`: database `sqlite` caricato in un `AWS S3 bucket` e acceduto dalla `AWS Lambda` (dove è installato `Django`) per le letture e le scritture, tramite il pacchetto `django-s3-sqlite`
 
- __Cache__: la Cache `Django` attiva su backed `AWS DynamoDB` sia per le `session` che la `pagine` tramite il pacchetto `django-dynamodb-cache`


Di seguito lo schema architturale su AWS

![Schema architetturale su AWS ](./images/fantacitorio_architecture_schema.png)


### deploy ambiente di stage

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

1. generazione delle tabelle di sistema della applicazione `fc_gestione_app` e `fc_classifiche_app`
   ```
   zappa manage stage migrate fc_gestione_app "--database default"
   zappa manage stage migrate fc_classifiche_app "--database db_classifiche --fake"
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

1. creazione delle viste per popolare in database classifiche
   ```
   zappa manage stage create_classifiche_views
   ```

1. refresh delle classifiche con la creazione e popolamento del database classifiche 
   ```
   zappa manage stage sqlite_refresh_classifiche
   ```

### certificato HTTPS e dominio 

Al termine del deploy e update `zappa` mostra l'endopoint esposto sulle `AWS API Gateway` del nostro ambiente, che risulta già navigabile accedendo ad un URL tipo:
```
https://<STRINGA-RANDOM>.execute-api.<AWS Region>.amazonaws.com/stage
```

Se si ha a disposizione un dominio gestito su `AWS Route53`, è possibile generare un certificato valido HTTPS sul nostro dominio. I certificati creati `AWS Certificate` possono essere utilizzati nelle risorse `AWS` sono gratis e `AWS` si occupa di rinnorarli in automatico dopo la scadenza annuale.

Quindi dopo aver generato e validato il certificato HTTPS sul dominio, si copia il suo `ARN` dentro `zappa_setting.json` nel campo `"certificate_arn"` e si valorizza il dominio nel campo `domain`. Tramite il comando:

```
zappa certify stage
```

Questo comando di `Zappa` si occupa di:

1. creare un `Custom Domain` mappandolo allo stage delle `AWS API Gateway` 
1. associa il certificato HTTPS il cui `ARN` è configurato nei settings 
1. creare le entry sul DNS del dominio `AWS Route53` che puntano alle `AWS API Gateway` del nostro ambiente

Al termine dell'esecuzione il comando mostra l'URL in HTTP del nostro domino che punta all'ambiente deployato: `https://miodominio.com`

### AWS CloudFront

`CloudFront` è la CDN (`Content Delivery Network`) di `AWS` per ottimizzare la distribuzione dei contenuti utilizzando i `CloudFront Edge` ossia mirror dei contenuti distribuiti in modo capillare nel mondo minimizzando latenza e massimizzando la velocità di fornitura dei contenuti agli utenti finali.

`CloudFront` inoltre gestisce anche come fornire i contenuti in base a dove sono localizzati nelle `Origin` ossia le applicazioni o i contenuti esporti. Nel caso particolare di un progetto Django, a fronte di una richiesta di una pagine, `CloudFront` interroga:

- le `AWS API Gateway` per i contenuti dinamici, ossia le pagine generate da Django
- l' `AWS S3 Bucket` per i contenuti statici di Django (immagini, CSS, JavaScript)

La configurazione di `CloudFront` per le applicazioni `Django` deployate con `zappa` è particolare e ha richiesto diversi tentativi prima di arrivare ad una soluzione soddisfacente:

1. definito il dominio `fc-project-api-stage.adessospiana.it` per le `AWS API Gateway` che ospitano la  `AWS Lambda` di `Django`, configurando `zappa_setting.json` ed eseguento `zappa certify stage`

1. creato la distribution `CloudFront` con le due origin:
   * l'origin Custon `fc-project-api-stage.adessospiana.it`
   * l'origin S3 `fc-zappa-static` 

1. configurati i `beaviour` ossia le regole di distribuzione come segue:
   * tutte le richieste `/static/*` sono indirizzate all'origin `fc-zappa-static` 
   * tutto il resto `Default (*)` viene indirizzato alla origin custon `fc-project-api-stage.adessospiana.it` 

1. Per il `beaviour`  `Default (*)` la cache è disabilitata e vengono trasmessi tutti li `HTTP Header` eccetto l'Header `Host`. Di seguito la configurazione del `beaviour` 
   
   ![Configurazione AWS CloudFront del beaviour Default (*) ](./images/cloudfront_default_beaviour_config.png)

### reporting errore 

Dato che nell'ambiente AWS `settings.DEBUG` è `False`, gli amministratori ricevono gli errori server (errori `500`) via email tramite la configurazione del server `SMTP` e la configurazione di `settings.ADMINS`, array di tuple `(nome,email)`

Mentre errori `404` sono notificate agli indirizzi specificati in `settings.MANAGERS`. Prima è necessario aggiungere ai `settings.MIDDLEWARE` `django.middleware.common.BrokenLinkEmailsMiddleware`. Da notare che vengono notificati solo gli errori 404 con `Refers` valorizzato con un url del sito, quindi sono notificate le pagine non trovate clicando i link presenti nel sito. Se generiamo l'errore modificando a mano l'url del browser, otterremo un errore `404` ma non verrà inviata ai managers alcuna mail.

### personalizzazione pagine di errore

Sempre nell'ambiente AWS gli errori 400 403 404 e 500 sono indirizzate su pagine specifiche personalizzata, rispettivamente:

* `templates/400.html` richiesta non valida
* `templates/403.html` richiesta non autorizzata
* `templates/404.html` pagina non trovata
* `templates/500.html` errore server

## deploy ambiente di produzione

L'ambiente di produzione ribattezzato `zappa_settings.json` ribatezzato `production` ha la stessa architettura di `stage` solo una diversa instanza dei backend, CloudFront, Zappa, certificati e nome a dominio. 

Di seguito le sequenza del comandi da eseguire dopo aver configurato la sezione `production` del file `zappa_settings.json`:

```
zappa deploy production
zappa certify production
zappa manage production "migrate fc_classifiche_app --fake"
zappa manage production migrate
zappa manage production createcachetable
zappa invoke production "from django.contrib.auth.models import User; User.objects.create_superuser('<SUPER USER>', '', '<PASSWORD>')" --raw
zappa manage production loaddata fc_gestione_app
zappa manage production create_classifiche_views
zappa manage production refresh_classifiche
```

## Creazione progetto Django

In questa sezione è mostrata la genesi del progetto descrivendo i comandi utilizzati per crearlo e il modo in cui è stata disegnata la base dati.

Di seguito i comandi iniziali con cui sono stati creati il progetto e le due app django:

```
django-admin startproject fc_project .
django-admin startapp fc_gestione_app
django-admin startapp fc_classifiche_app
```

Per comodità il database principale `fc_gestione_app` è stato creato graficamente con `PgAdmin ERD` poi generato nel postgres locale. 

Di seguito gli schema ER generati con `python manage.py graph_models`, comando di `django-extension`:

* `fc_gestione_app`: generato con `python manage.py graph_models fc_gestione_app -o images/fc_gestione_app__model.png`
![graph model fc_gestione_app](./images/fc_gestione_app_model.png)

* `fc_classifiche_app` generato con `python manage.py graph_models fc_classifiche_app -o images/fc_classifiche_app__model.png`
![graph model fc_classifiche_app](./images/fc_classifiche_app_model.png)

Quindi i models di Django sono stati creati tramite il comando `inspectdb` che genera i models partendo da un database esistente

```
python manage.py inspectdb > fc_gestione_app/models.py
```

I models Django di `fc_classifiche_app` sono stati creati manualmente sulle tre viste materializzate per `PostgreSQL` e tre tabelle per `Sqlite`

La configurazione inziale di `Zappa` è stata generata eseguendo il comando `zappa init` __eseguito dentro il virtualenv del progetto__. In questo modo riconosce l'ambiente Django installato nel virtualenv e crea il file `zappa_setting.json` tramite un wizard. 

## Per Contribuire

Puoi contribuire:

* aprendo una [segnalazione](https://github.com/heyteacher/fantacitorio/issues/new) per
  * segnalare malfunzionamenti
  * suggerire nuove funzionalità

* eseguendo un `fork` del progetto e contribuendo allo sviluppo.
