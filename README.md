
# Progetto Web Fantacitorio 

Progetto web __Fantacitorio__ creata partendo dai fogli di calcolo creati e gestiti da https://twitter.com/rosyilcapo, in particolare la base dati è stata creata partendo dalla __classifica generale provvisoria__ https://docs.google.com/spreadsheets/d/19RcqYZYyrCdjMHyFA2bcChaxnd7JIuzjXxYbKNRN3jM/edit?pli=1#gid=0

Fantacitorio è un _fanta game_ inventato dalla trasmissione __Propaganda Live__ di __La7__ nel 2021. 

Info disponibili:

- Regolamento: https://www.la7.it/propagandalive/video/fantacitorio-16-02-2022-423442
- Monologo di __Valerio Aprea__: https://www.la7.it/embedded/la7?w=640&h=360&tid=player&content=423442

# Demo

Una demo del progetto è disponibile su AWS al seguente indirizzo:

https://ivkxyxrgkd.execute-api.eu-west-1.amazonaws.com/stage

le credenziali in sola lettura:

- login: fantautente
- password: fantacitorio

# Per Sviluppatori

Il sito (`project Django`) è organizzato in due sezioni (`app Django`):

- `GESTIONE` add dedicata alla gestione delle squadre, le leghe i politici, le puntate e i punteggi
- `CLASSIFICA` app per la visualizzazione delle classifiche

##  Installazione ed esecuzione in locale

Per lo sviluppo e l'utilizzo in locale, si utilizza per comodità `sqlite3`.

- creazione del virtualenv che ospiterà Django in locale
  ```
  sudo apt get virtualenv
  sudo apt install virtualenv
  virtualenv  venv --python python3.9 --pip 22.3.1
  source ve/bin/activate
  ```

- rinominare `zappa_settings.json.template` in `zappa_settings.json`. Nella sezione dev contiene già le impostazioni per utilizzare il database locale `sqlite3`

- Attivazione del virtualenv creato
  ```
  source ve/bin/activate
  ```

- Installazione di Django e delle dipendenze richieste
  ```
  pip install -r requirements-txt
  ```

- generazione delle tabelle di sistema della applicazione fc_gestione_app
  ```
  python manage.py migrate
  ```

- caricamento dei dati aggiornati alla 6 puntata di propaganda
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

- accedere a http://localhost:8000 e autenticarsi tramite il super user creato

### Dump dei dati e creazione della fixture di fc_gestione_app

```
python manage.py dumpdata fc_gestione_app -o fc_gestione_app/fixtures/fc_gestione_app.json.bz2
```

## Rilascio in produzione  su AWS con Zappa

L'ambiente di produzione è rilasciato nel cloud `AWS` tramite `zappa` su una instanza `AWS RDS` di `postgres`.

Prima è necessario creare il database la `VPC`

### Deploy su AWS

- dopo aver creato il database RDS e la VPC, configurare zappa per il proprio ambiente AWS edidando la sezione `production` del file`zappa_settings.json`

- deployare l'applicazione nel cloud
  ```
  zappa deploy production
  ```
  Al termine del deploy, viene visualizzato l' URL del sito rilasciato.
   
- creazione del tabelle nel database
  ```
  zappa manage production migrate
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

Naturalmente il database `AWS RDS postgres` e la `VPC` vanno cancellate manualmente da AWS.

## Rilascio in ambiente di stage

L'ambiente di stage di AWS utilizza il database sqlite3 caricati in un bucket e acceduto da Django per le letture e le scritture, quindi è un utilizzabile per la produzione ma per demo e test.

Dopo aver configurato la sezione `stage` di `zappa_settings.json` si rilascia su AWS con il seguente comando

```
zappa deploy stage
```


# Appendice: come è fatto il progetto in Django

Il progetto Django è denominato `fc_project` e, come sopra esposto, è costituito da 2 app Django denominate in:

- `fc_gestione_app` 
- `fc_classifica_app` 

di seguito i comandi con cui sono stati creati:

```
django-admin startproject fc_project .
django-admin startapp fc_gestione_app
django-admin startapp fc_classifiche_app
```

Inizialmente il database di `fc_gestione_app` è stato creato graficamente con `PgAdmin` poi generato nel postgres locale. 

Quindi i models di Django sono stati creati tramite `reverse engineering` con il comand `inspectdb`

```
python manage.py inspectdb > fc_gestione_app/models.py
```

I models Django di `fc_classifiche_app` sono stati creati a mano sulle tre viste materializzate e non gestite da Django (vedi nei models `managed=False`)

La configurazione inziale di `Zappa` è stata generata eseguendo il comando `zappa init` che riconosce l'ambiente Django in locale e crea il file `zappa_setting.json` tramite un wizard di domande. 
