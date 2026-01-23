# Docs:
## Innholdsfortegnelse
- [Planleggingsfasen](#planleggingsfasen)
- [Under utvikling og på avslutten](#under-utvikling-og-på-avslutten)
- [Begrunnelse av stack](#begrunnelse-av-stack)
- [Templates](#templates)
- [Datamodell](#datamodell)
- [Hvorfor kan man ikke velge rolle ved registrering?](#hvorfor-kan-man-ikke-velge-rolle-ved-registrering)
- [Hva jeg har lært](#hva-jeg-har-lært)

## Planleggingsfasen:

1. Gå gjennom Oppdragsbeskrivelse, og krav.
2. Tegne Første versjon av datamodell (i lucidchart).
3. Skissere en wireframe.
4. Stack (Se [Begrunnelse av stack](#Begrunnelse av stack)).

## Under utvikling og på avslutten:
- Github Projects (kanban) for oversikt over hva jeg holder på med og todo/backlog.  

## Begrunnelse av stack
Flask og mariadb er det som skulle bli brukt, men jeg valgte i stedet Django og PostgreSQL.

Django har en innebygd ORM (Object-Relational-Mapping), der Python klasser (modeller) automatisk oversettes til SQL-tabeller. Samhandling med databasen kan derfor bli gjort via Python-kode istedenfor manuelle SQL-spørringer.

Django tilbyr også forms-klasser, som gjør oppretting og håndtering av skjemaer enklere.

Dette passet bra til dette prosjektet, fordi det var en kort frist på innlevering og Django gir mye ferdig funksjonalitet (inkludert sikkerhet!) som sparer tid i utviklingsfasen. 

## Templates
Jeg valgte å håndtere tabellene for drift og vanlige brukere i samme template ([scrHome.html]). Ved bruk av Jinja og autentisering på server-siden, så kan jeg forsikre meg over at vanlige brukere ikke får tilgang til alle tickets. 

## Datamodell
Vedlagte datamodell viser hovedtabellene i systemet (Django oppretter automatisk egne tabeller). Deadline, Created_at, og Changed_at er også lagt til i tickets-modellen, for bedre funksjonalitet.

## Hvorfor kan man ikke velge rolle ved registrering?
Å la brukere bestemme om de kan være drift-bruker, er ikke sikkert! Da kan hvem som helst se alle saker. Bedre at de som har admin-rettigheter kan krysse av på hvem som er staff (i Django sitt admin panel). 

## Hva jeg har lært: 
- Bruk av Django forms og Django models
- Lucidchart for Datamodell 
- Lært litt mer om Bootstrap 
- Pagination
- Parent-template for en mer ryddigere frontend.
