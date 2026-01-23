# Docs:

## Planleggingsfasen:

1. Gå gjennom Oppdragsbeskrivelse, og krav
2. Tegne Første versjon av datamodell (i lucidchart)
3. skisse en wireframe
4. Stack (Se [Begrunnelse av stack](#Begrunnelse av stack))

#### Under programmeringen og på avslutten:
- Github Projects (kanban) for oversikt over hva jeg holder på med og todo/backlog.  
- [Testbrukere.md] : Oversikt over testbrukere i prosjektet. Dette skal bare bli brukt lokalt, og de blir slettet før prod.

## Begrunnelse av stack
Flask og mariadb er det skulle blitt brukt, men jeg valgte i stedet Django og PostgreSQL.

Django har en innebygd ORM (Object-Relational-Mapping), der Python klasser (modeller) automatisk oversettes til SQL-tabeller. Samhandling med databasen kan derfor bli gjort via Python-kode istedenfor manuelle SQL-spørringer.

Django tilbyr også forms-klasser, noe som gjør oprretting og håndtering av forms-skjemaer enklere.

Dette passet bra til dette prosjektet, fordi det var en kort frist på innlevering og Django gir mye ferdig funksjonalitet (inkludert sikkerhet!) som sparer tid i utviklingsfasen. 

## Hvorfor kan ikke man velge rolle ved registrering?
Å la brukere bestemme om de kan være drift-bruker, er ikke sikkert! Da kan hvem som helst se alle saker. Bedre at de som har admin-rettigheter kan krysse av på hvem som er staff (i django sitt admin panel). 

## Hva jeg har lært: 
- Bruk av Django forms og Django models
- Lucidchart for Datamodell 
- Lært litt mer om Bootstrap 
- Pagination
- Parent-template for en mer ryddigere frontend.