# Funksjoner

## Innlogging
- Registreringsside (Kan også sende forespørsel om å drift-arbeider)
- Innloggingsside
- Utlogging
- Sjekk at bruker er innlogget før tilgang til sider

## For vanlige brukere
- Side for å opprette ny ticket (tittel, beskrivelse)
- Side som viser oversikt over egne tickets
- Kan se status på egne tickets

## For drift-arbeidere
- Side som viser alle tickets i systemet
- Kan "ta" en ticket (tildele seg selv som behandler)
- Kan endre status på tickets (åpen/under arbeid/lukket)

## Teknisk
- Bruk av render_template for alle sider
- POST for å sende data (registrering, innlogging, nye tickets)
- GET for å vise siders

## Fint å ha - men ikke må:

### Drift-arbeider:
    - Påminnelse at en frist nærmer seg 
### Admin:
    - Førespørsler om å bli drift-arbeider blir sendt på mail til admin 