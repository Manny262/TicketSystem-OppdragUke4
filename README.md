# TicketSystem-OppdragUke4
## Innholdsfortegnelse
- [Beskrivelse](#beskrivelse)
- [Installasjonsveiledning](#installasjonsveiledning)
    - [Forutsetninger](#forutsetninger)
    - [1. Clone prosjektet fra GitHub](#1-clone-prosjektet-fra-github)
    - [2. Opprett et virtuelt miljø](#2-opprett-et-virtuelt-miljø)
    - [3. Installer nødvendige pakker](#3-installer-nødvendige-pakker)
    - [4. Sett opp databasen](#4-sett-opp-databasen)
    - [5. Opprett superbruker](#5-opprett-superbruker-hvis-man-vil-ha-tilgang-til-admin-panelet)
    - [6. Start utviklingsserveren](#6-start-utviklingsserveren)
    - [7. Tilgang til admin panel](#7-tilgang-til-admin-panel)
    - [Kobling fra andre enheter](#kobling-fra-andre-enheter)

## Beskrivelse:
Dette er et oppdrag for uke 4, 2026: utvikle første versjon av et ticketsystem for et lite IT-selskap (på fire dager).Følg installasjonsinstruksjonene under for å sette opp prosjektet lokalt.


## Installasjonsveiledning

### Forutsetninger
- Python 3.13.9 installert (eller nyere)
- Git installert 
- pgAdmin4 installert
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
py -m venv venv
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

### 4. Sett opp databasen
#### 4.1 Opprett PostgreSQL database

Åpne PostgreSQL (pgAdmin) og opprett en database med navn `ProjectTicketSystem`

#### 4.2 Secret key 
Åpne terminalen og kopier output: 
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
#### 4.3 Konfigurer database tilkobling

Åpne filen `PROJECT_TICKETSYSTEM\example-env` og oppdater verdiene til dine egne. 
Endre navn : `example-env` -> `.env`



#### 4.4 Kjør migrasjoner

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
