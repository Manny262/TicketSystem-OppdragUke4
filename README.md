# TicketSystem-OppdragUke4
## Beskrivelse:
Oppdrag uke 4: Utvikle første versjon ticketsystem for et lite IT-selskap (på fire dager).

## Installasjonsveiledning

### Forutsetninger
- Python 3.13.9 installert (eller nyere)
- Git installert 

### 1. Clone prosjektet fra GitHub

**HTTPS**
```bash
git clone https://github.com/Manny262/TicketSystem-OppdragUke4.git
```

**SSH**
```bash
git clone git@github.com:Manny262/TicketSystem-OppdragUke4.git

```

### 2. Opprett et virtuelt miljø

start med å cd inn i PROJECT_TICKETSYSTEM:

```bash 
cd TicketSystem-OppdragUke4\PROJECT_TICKETSYSTEM
```

**Windows:**
```bash
py-m venv venv
venv\Scripts\activate
```


**Mac/Linux:**
```bash
py -m venv venv
source venv\bin\activate
```
(Noen pc-er tilatter ikke bruk av "py", bruk python eller python3)

### 3. Installer nødvendige pakker

```bash
pip install -r requirements.txt
```
asgiref==3.11.0
beautifulsoup4==4.14.3
Django==4.2.27
django-bootstrap-v5==1.0.11
psycopg2-binary==2.9.11
python-decouple==3.8
soupsieve==2.8.3
sqlparse==0.5.5
typing_extensions==4.15.0
tzdata==2025.3

### 4. Sett opp databasen
#### 4.1 Opprett PostgreSQL database

Åpne PostgreSQL (pgAdmin) og opprett en database med navn  `ProjectTicketSystem`

#### 4.2 Konfigurer database tilkobling

Åpne filen `PROJECT_TICKETSYSTEM\example-env` og oppdater verdiene til dine egne. 
Endre navn : `example-env` -> `.env`

#### 4.3 Kjør migrasjoner

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Opprett superbruker (Hvis man vil ha tilgang til admin-panelet), 

```bash
python manage.py createsuperuser
```

Følg instruksjonene i terminalen for å opprette en admin-bruker.

### 6. Start utviklingsserveren

```bash
python manage.py runserver
```
### 7. Tilgang til admin panel

Gå til **http://dinIP:/admin/** og logg inn med superbruker-kontoen du opprettet i steg 5.

### Kobling fra andre enheter

Gå til `PROJECT_TICKETSYSTEM\PROJECT_TICKETSYSTEM\settings.py`.
Finn:
```py
ALLOWED_HOSTS = [
    'localhost', 'din-ip-adresse']
```

Erstatt `'din-ip-adresse'` med din IP-adresse (f.eks. `'192.168.1.100'`). 

For å tillate alle IP-adresser under utvikling (ikke anbefalt i produksjon):
```python
ALLOWED_HOSTS = ['*']
```


#### Finne IP-adresse

**Windows:**
```bash
ipconfig
```
Se etter "IPv4 Address".

**Mac:**
```bash
ifconfig
```
Eller gå til System Preferences → Network og se IP-adressen til din aktive tilkobling.

**Linux:**
```bash
ip a
```
