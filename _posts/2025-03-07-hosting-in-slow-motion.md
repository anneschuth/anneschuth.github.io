---
title: "Hosting in slow motion"
date: '2025-03-07T09:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
---

Er is inmiddels een maand voorbij, niet een week. En ik word rechts en links ingehaald, door anderen die wel _week_
notes schrijven, zoals [Eelco](https://eelco.hotting.it/).
Ik heb allerlei excuses, zoals een week vakantie, en een [project Machine Law](/2025/01/25/machine-law.html) dat gaat
vliegen en dat mijn tijd, maar vooral mijn aandacht en
enthousiasme slurpt.
Maar het echte excuus is dat ik _dit_ verhaal wilde schrijven en dat ik steeds hoopte dat het daar tijd voor was. Dat is
nu nog steeds niet zo, maar dit verhaal kan niet langer wachten.

> Edit: het probleem dat ik hier beschrijft was kennelijk al bekend, [KPMG schreef een rapport](https://www.tweedekamer.nl/downloads/document?id=2025D01627) in opdracht van EZ.

## Hoe het begon

Dit verhaal begon vlak voor Sinterklaas vorig jaar.
Voor de [Algoritme Management Toolkit (AMT)](https://github.com/MinBZK/amt) hadden we toen een omgeving nodig om in
productie te draaien, want er kwam een pilot fase aan, met echte gebruikers en echt data.

We draaien tijdens het ontwikkelen de AMT op de infra van [Digilab](https://digilab.overheid.nl/).
Dat is voor ons een hele fijne omgeving geweest, zo was het in April 2024 een kwestie van _één_ berichtje in een
Mattermost kanaal:

![Digilab Cluster Aanvraag](/assets/digilab_aanvraag.png)

Minder dan **12 minuten later** kwam het bericht _"done!"_ en hadden we twee Kubernetes namespaces.
Precies wat we ook nu zoeken: twee namespaces met elk 4 cores, 4GB geheugen, en een persisted volume van 100GB. Het
stelt echt helemaal niets voor.

Helaas is de infra van Digilab niet geschikt voor productie: het heeft geen enkele SLA (want veel minder dan een
FTE aan ondersteuning) en het is niet geschikt voor productie data.
Voor de duidelijkheid, het aanvragen van een productie omgeving bij Digilab (als dit ondersteund zou worden) zou ook 12
minuten duren, simpelweg omdat alles geautomatiseerd is. En dat is met een _Mattermost_ chat interface, als dit een knop
zou zijn, dan zou dit praktisch naar 0 minuten gaan.

## Hoe het ook kan

Om te weten hoe de ervaring zou zijn bij een grote commerciële cloud boer, maakte ik aan wat we nodig hebben bij AWS.
Ik begon om 10:25 vanochtend met de aanmeld-flow van AWS. Ze hadden email, adres, telefoonnummer, mijn creditcard en een
afschrijving van 1USD nodig.

Maar na het aanmelden was het een kwestie van een cluster aanmaken bij _Amazon Elastic Kubernetes Service_.
Dat proces was heel eenvoudig, een paar kliks om default _IAM node-_ en _cluster roles_ aan te maken.

Om 10:33 zag ik dit blije nieuws:

![AWS EKS Success](/assets/aws_success.png)

Om 10:44 (19 minuten later) was het cluster _Active_ met 2 _c6g.large_ nodes (een maatje te klein als het gaat om cpus,
zag ik achteraf).

Kosten voor het juiste cluster formaat, inclusief CPU, geheugen, opslag en 2 backups per dag zou richting de 2K USD per
jaar gaan.

2 minuten later was het cluster en mijn AWS account weer verdwenen.

## De lat

Dit is dus waar de lat ligt:

- De tijd tussen start aanvragen en het draaien van een omgeving zou ergens **tussen de 12 en 19 minuten** moeten
  liggen, of in ieder geval die orde van grootte moeten hebben.
- De kosten ergens rond **2K USD per jaar** voor twee Kubernetes namespaces met elk 4 cores, 4GB geheugen, en een
  persisted volume van 100GB.

## Waarom commerciële cloud geen optie is

Het is in mijn ogen _nooit_ logisch geweest voor de overheid om te leunen op (Amerikaanse) commerciële clouds.
Maar met recent gebeurtenissen in de wereld is het steeds minder logisch om naar omgevingen zoals Azure, AWS, of GCS te
kijken. Zie ook de sterke stukken van [Bert Hubert](https://berthub.eu/) van de afgelopen weken over dit onderwerp:

* [Nee je kan niet meer je overheid en maatschappij verhuizen naar Amerikaanse servers](https://berthub.eu/articles/posts/nee-je-kan-niet-meer-je-overheid-bouwen-op-de-us/)
* [De cloud in soorten en maten](https://berthub.eu/articles/posts/cloud-in-soorten-en-maten/)
* [Naar de cloud nu je er nog mee wegkomt: is dat het?](https://berthub.eu/articles/posts/naar-de-cloud-nu-het-nog-kan-is-dat-het/)

## Het begin van de zoektocht

Dus zo begon, begin December 2024, onze zoektocht naar een omgeving waar we wel productie kunnen draaien.
In eerste instantie voor de [AMT](https://github.com/MinBZK/amt), maar in principe voor alle software die we maken vanuit
het [Rijks ICT Gilde](https://www.rijksorganisatieodi.nl/rijks-ict-gilde) en in productie willen brengen.

Op zoek naar een productie omgeving binnen de Nederlandse Overheid.
Op zoek, in feite, naar twee Kubernetes namespaces met elk 4 cores, 4GB geheugen, en een persisted volume van 100GB.
Nogmaals: het stelt helemaal niets voor.

Er zijn, zo blijkt, binnen de overheid eigenlijk maar een paar diensten binnen de overheid waar we hiervoor kunnen
aankloppen.
En uiteindelijk lijken onze opties beperkt tot slechts één dienst.
Dus die schreven we op **4 December** aan. Dit was het eerste mailtje van, wat we toen nog niet wisten, heel veel
mailtjes. **Zie onderaan een chronologisch overzicht.**

We verwachtten eigenlijk een relatief eenvoudig proces. Misschien zou het een paar dagen duren voordat we een reactie
kregen, of misschien zelfs een week of twee om alles in te richten. Maar we hadden geen idee dat we hiermee aan een reis
begonnen die maanden zou duren, tientallen e-mails zou vergen, uren aan vergaderingen zou kosten, en meerdere documenten
en beoordelingen zou vereisen. En dan hebben we het nog niet over de financiele kant.

Het was alsof we vroegen om een kopje koffie, maar in plaats daarvan werd ons verteld dat we eerst de geschiedenis van
koffie moesten documenteren, een uitgebreide analyse van verschillende koffiebonen moesten maken, en goedkeuring moesten
krijgen van zeven verschillende afdelingen voordat er ook maar één druppel water kon worden gekookt.

Het had zo simpel kunnen zijn. 12 minuten bij Digilab, 19 minuten bij AWS. Maar in plaats daarvan begon een odyssee door
de wereld van de overheidsinfrastructuur, een reis die we hier chronologisch zullen documenteren. Niet om iemand aan de
schandpaal te nagelen, maar om te laten zien hoe groot de afstand is tussen waar we staan en waar we moeten zijn als we
een soevereine, efficiënte digitale overheid willen zijn.

## De eerste weken - wachten op antwoord

Na ons eerste verzoek op **4 december 2024** bleef het vijf dagen stil. Geen reactie. Geen ontvangstbevestiging. We
hadden
natuurlijk rekening gehouden met de drukke Sinterklaasperiode, dus we stuurden op **9 december** een vriendelijke
herinnering: "Hey Medewerker2, heb je binnenkort tijd voor een korte meeting...?"

Dezelfde dag nog kregen we een reactie: "Dag Medewerker3, ik zal vandaag een uitnodiging sturen..." Een goed teken,
dachten we. Er kwam beweging in!

Op **16 december** werd er een mail doorgestuurd waarin onze vragen over dienstverlening werden besproken, en twee dagen
later, op **18 december**, hadden we onze eerste overleg. Vier medewerkers, dertig minuten - dat leek redelijk
efficiënt.

De volgende dag ontvingen we een opvolgende e-mail: "Hi Medewerker1, Medewerker4, dank voor ons gesprek gisteren..." We
hadden goede hoop. Het proces was in gang gezet. Nu was het wachten op de volgende stap.

## Het nieuwe jaar - de bureaucratie ontwaakt

Maar dan volgt er bijna een maand radiostilte. Geen updates, geen vragen, geen voortgang. Het was dan ook vakantie.
Op **15 januari 2025** voelen we ons genoodzaakt om zelf contact op te nemen: "Hi Medewerker2, hebben jullie
tijd gehad...?"

De dag erna komt er een geruststellend antwoord: "Dag Medewerker1, we zijn ermee bezig..." En vier dagen later volgt het
verzoek om data en tijden door te geven voor een nieuwe vergadering.

Na wat heen en weer gemaild over beschikbaarheid, ontvangen we op **22 januari** het nieuws dat er "interne
goedkeuring" is. Blijkbaar moest er eerst intern worden besproken of we überhaupt verder konden gaan met het proces.

Op **27 januari** volgt dan de "intake meeting". Een vergadering van anderhalf uur met vier mensen. Dat zijn
zes mensuren om te bespreken wat we nodig hebben: twee namespaces, elk 4 cores, 4GB geheugen, en 100GB opslag.

## Februari - de papierwinkel begint

De dag na de intake meeting ontvangen we een document: "Intake Architectuur v0.1.docx". Er wordt iets
concreets opgeleverd!

Op **29 januari** is er weer een meeting, een demonstratie deze keer. Twee uur, vier personen.
Dat zijn acht mensuren om te laten zien hoe hun omgeving werkt.

Eind januari en begin februari worden er wat e-mails uitgewisseld over het document. Er komt feedback, het document
wordt bijgewerkt, en ook wordt er security-expertise ingevlogen. Medewerker5, een security-expert, wordt erbij
betrokken.

Dan is het weer even stil. Medewerker4 is tot 10 februari afwezig, krijgen we te horen via een automatische reply.
Ondertussen delen we de security-feedback en voeren we een telefoongesprek met onze manager, die ons aanmoedigt: "Niet
opgeven".

Op **10 februari** is er weer een vergadering, een "afstemming meeting" deze keer. Een uur, drie personen. Weer drie
mensuren om te praten over... ja, waarover eigenlijk? Over het proces? Over de vraag wanneer we nu  die twee
namespaces krijgen?

## De laatste loodjes - of toch niet?

Halverwege februari begint het ongeduld toch echt toe te slaan. Op **17 februari** vragen we expliciet om een tijdpad: "
Hi Medewerker4, zou jij ons een tijdpad kunnen geven...". Twee dagen later volgt er nog een mail: "Hi Medewerker4, mogelijk
zijn er nog wat obstakels...".

Op **21 februari** bespreken we in een Mattermost-chat met onze manager of we moeten escaleren. We zijn nu al bijna drie
maanden bezig, en we hebben nog geen concrete datum wanneer we de omgeving kunnen verwachten.

We proberen telefonisch contact te leggen met twee contactpersonen bij de Hosting Provider, maar krijgen geen gehoor.
Later die dag worden we teruggebeld, en dan komt het verlossende woord: **het cluster komt in april!**
Waarschijnlijk de tweede helft. Dat is nog bijna twee maanden wachten, maar tenminste hebben we nu een indicatie.

De bevestiging komt ook per e-mail binnen: "Onze huidige inschatting van de planning: oplevering in april (tweede
helft)". We zijn inmiddels bijna 80 dagen verder sinds ons eerste verzoek.

## Terug naar af?

Maar dan, op **25 februari**, krijgen we plotseling vragen over de "omvang" van de applicatie. "We zijn bezig met de
kostenindicatie voor jullie aanvraag voor de omgeving." Maar wacht eens even... hadden we niet dat niet al in december
precies aangegeven wat we nodig hebben? En hadden we dat niet herhaald tijdens de intake eind januari?

We wijzen er op: "Ik was in de veronderstelling dat we dat al tijdens de intake vastgelegd hadden".

## Maart - De kostenindicatie

Op **4 maart 2025**, exact 90 dagen na ons eerste verzoek, krijgen we de kostenindicatie. "Hierbij ontvang je
de kostenindicatie voor de hosting van jullie Applicatie". Een mijlpaal!

Maar we hebben toch nog wat vragen over de kostenindicatie. De kosten liggen namelijk ruim 10x boven de lat.
En dat niet alleen, we worden gevraagd te betalen voor de uren die in dit proces gestoken zijn.

En zo zijn we op **7 maart 2025**, 93 dagen na ons eerste verzoek, nog steeds bezig met het beantwoorden van vragen, het
aanleveren van informatie, en het wachten op goedkeuringen. En de daadwerkelijke oplevering van onze omgeving? Die staat
gepland voor "april, waarschijnlijk tweede helft". Als alles meezit.

## De balans tot nu toe

Helemaal onderaan dit bericht staat een chronologische tijdlijn. Hier de samenvatting daarvan:

| **Categorie**               | **Aantal** | **Details**                                                     |
|-----------------------------|------------|-----------------------------------------------------------------|
| 👥 Meetings                 | 4          | 1x 30 min (4p), 1x 90 min (4p), 1x 120 min (4p), 1x 60 min (3p) |
| 👥 Mensuren                 | 19         | Totaal aantal uren besteed in meetings                          |
| 📨 Emails                   | 41         |                                                                 |
| 📞 Telefoon gesprekken      | 4          | 2x succesvol, 2x poging                                         |
| 💬 Chats                    | 1          |                                                                 |
| 📄 Documenten               | 3          | Origineel + feedback van intake, kostenindicatie                |
| ⏱️ Doorlooptijd tot vandaag | 93 dagen   | 4 dec 2024 - 7 maart 2025                                       |
| ⏱️ Verwachtte doorlooptijd  | 132 dagen  | 4 dec 2024 - 15 april 2025                                      |

## Wat dit betekent voor digitale soevereiniteit

Terwijl wij bezig waren met onze odyssee, schreef Bert Hubert zijn stukken over digitale soevereiniteit en waarom de
overheid niet afhankelijk zou moeten zijn van Amerikaanse cloudproviders. En ik ben het met hem eens, sterker nog, ik
ben er een groot voorstander van dat de overheid haar eigen infrastructuur beheert.

Maar als het opzetten van een simpele Kubernetes-omgeving meer dan drie maanden duurt en tientallen e-mails,
vergaderingen en documenten vergt, terwijl dezelfde omgeving in de commerciële cloud in 19 minuten kan worden opgezet,
dan is het geen wonder dat veel overheidsorganisaties toch voor de commerciële cloud kiezen.

De kloof tussen waar we staan en waar we moeten zijn is enorm. Als we echt een soevereine digitale overheid willen zijn,
moeten we niet alleen de technische capaciteit hebben om onze eigen infrastructuur te beheren, maar vooral ook de
organisatorische capaciteit om dat efficiënt te doen.

Want dit gaat niet over techniek. De technologie is er. Kubernetes is er. De hardware is er. Dit gaat over processen,
over bureaucratie, over de manier waarop we als overheid omgaan met ICT.

En terwijl wij wachten op onze omgeving, staan onze gebruikers ook te wachten. Gebruikers die met
onze [Algoritme Management Toolkit (AMT)](https://github.com/MinBZK/amt) aan de slag willen om hun algoritmes te
verantwoorden en transparanter te maken. Gebruikers die nu
nog langer moeten wachten omdat wij vastzitten in een proces dat 93+ dagen duurt in plaats van 19 minuten.

## Hoe dan wel

De lat ligt op 19 minuten. Laten we daar naartoe werken vanaf de ruim 190.000 minuten waar we straks half april op zitten.
Er is **ruimte voor een 10.000x speedup**. Juist omdat die ruimte groot is, heb ik er vertrouwen in dat we grote stappen 
kunnen zetten om dit beter te maken, zelfs met simpele ingrepen in het huidige proces. 
Maar beter nog, toewerkend naar een echt platform engineering organisatie, waar een Kubernetes namespace met een 
simpele druk op de knop geregeld is. We hebben de mensen en kennis om dit te doen! En daar draag ik met mijn ervaring bij Spotify graag aan bij!

> Edit: dit probleem was kennelijk al bekend,   [KPMG schreef een rapport](https://www.tweedekamer.nl/downloads/document?id=2025D01627) in opdracht van EZ.

## Tot slot

Ik wil benadrukken dat dit verhaal niet bedoeld is om individuele medewerkers aan de schandpaal te nagelen. De mensen
waarmee we hebben gewerkt doen hun best binnen het systeem waarin ze werken. Het probleem zit niet bij de mensen, maar
bij de processen en de organisatie.

## Chronologisch overzicht van onze zoektocht

| **Datum**    | **Type**    | **Beschrijving**                                                                                                                                                           |
|--------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4 dec 2024   | 📨 Email    | Medewerker1: "Hallo Medewerker2, Hierbij ..."                                                                                                              |
| 9 dec 2024   | 📨 Email    | Medewerker3: "Hey Medewerker2, Heb je binnenkort tijd voor een korte meeting..."                                                                                           |
| 9 dec 2024   | 📨 Email    | Medewerker2: "Dag Medewerker3, Ik zal vandaag een uitnodiging sturen..."                                                                                                   |
| 16 dec 2024  | 📨 Email    | Medewerker2: "FW: Vragen over dienstverlening"                                                                                                                             |
| 18 dec 2024  | 👥 Meeting  | Vragen over dienstverlening beantwoorden (30 min, 4p)                                                                                                                      |
| 19 dec 2024  | 📨 Email    | Medewerker2: "Hi Medewerker1, Medewerker4, Dank voor ons gesprek gisteren..."                                                                                              |
| 15 jan 2025  | 📨 Email    | Medewerker1: "Hi Medewerker2, Hebben jullie tijd gehad...?"                                                                                                                |
| 16 jan 2025  | 📨 Email    | Medewerker2: "Dag Medewerker1, We zijn ermee bezig..."                                                                                                                     |
| 20 jan 2025  | 📨 Email    | Medewerker2: "Dag Medewerker1, kan je opties voor datum en tijd sturen..."                                                                                                 |
| 21 jan 2025  | 📨 Email    | Medewerker1: "Ik weet nog niet zeker of ik er bij kan zijn..."                                                                                                             |
| 22 jan 2025  | 📨 Email    | Medewerker2: "Na onze interne goedkeuring..."                                                                                                                              |
| 27 jan 2025  | 👥 Meeting  | Intake meeting (90 min, 4p)                                                                                                                                                |
| 28 jan 2025  | 📨 Email    | Medewerker4: "Hoi Medewerker1, Medewerker3, Bijgaand eerste concept..."                                                                                                    |
| 28 jan 2025  | 📄 Document | Deelt: "Intake Architectuur v0.1.docx"                                                                                                                                     |
| 29 jan 2025  | 👥 Meeting  | Demo sessie (120 min, 4p)                                                                                                                                                  |
| 30 jan 2025  | 📨 Email    | Medewerker3: "Hey Medewerker4, Het ziet er goed uit..."                                                                                                                    |
| 30 jan 2025  | ✅ Feedback  | Geen belangrijke punten als aanvulling                                                                                                                                     |
| 30 jan 2025  | 📌 Notities | Opmerkingen over technische componenten                                                                                                                                    |
| 31 jan 2025  | 📨 Email    | Medewerker1 aan RIG manager: "fyi"                                                                                                                                         |
| 31 jan 2025  | 📨 Email    | Medewerker1: "Dank Medewerker4, Medewerker3, Ziet er goed uit!"                                                                                                            |
| 31 jan 2025  | 📋 Document | Document bijgewerkt met feedback                                                                                                                                           |
| 31 jan 2025  | 📄 Document | Deelt: "Intake Architectuur v0.1 - Feedback verwerkt.docx"                                                                                                                 |
| 31 jan 2025  | 🔄 Actie    | Document gedeeld met Medewerker5 (security expert)                                                                                                                         |
| 4 feb 2025   | 📨 Email    | Medewerker4: "Beste mailer, Ik ben tot 10 februari afwezig."                                                                                                               |
| 4 feb 2025   | 📨 Email    | Medewerker1: "Hi Medewerker4"                                                                                                                                              |
| 4 feb 2025   | 🔒 Security | Security feedback van Medewerker5 gedeeld                                                                                                                                  |
| 4 feb 2025   | 📨 Email    | Medewerker1 aan RIG manager: "Fyi"                                                                                                                                         |                                                                                                                                               |
| 5 feb 2025   | 📨 Email    | Medewerker3: "Hey Medewerker1, Over technische componenten..."                                                                                                             |
| 6 feb 2025   | 📞 Call     | Telefoongesprek met manager: "Niet opgeven"                                                                                                                                |
| 10 feb 2025  | 👥 Meeting  | Afstemming meeting (60 min, 3p)                                                                                                                                            |
| 17 feb 2025  | 📨 Email    | Medewerker1: "Hi Medewerker4, Zou jij ons een tijdpad kunnen geven..."                                                                                                     |
| 17 feb 2025  | 📨 Email    | Medewerker1: "Re: Afstemming Intake architectuur"                                                                                                                          |
| 19 feb 2025  | 📨 Email    | Medewerker1: "Hi Medewerker4, Mogelijk zijn er nog wat obstakels..."                                                                                                       |
| 21 feb 2025  | 💬 Chat     | Mattermost gesprek met RIG manager: "Moeten we escaleren?"                                                                                                                 |
| 21 feb 2025  | 📞 Call     | Poging tot telefonisch contact met Hosting Provider contactpersoon 1 (geen gehoor)                                                                                         |
| 21 feb 2025  | 📞 Call     | Poging tot telefonisch contact met Hosting Provider contactpersoon 2 (geen gehoor)                                                                                         |
| 21 feb 2025  | 📞 Call     | Hosting Provider belt terug: BEVESTIGING CLUSTER IN APRIL! (waarschijnlijk tweede helft)                                                                                   |
| 21 feb 2025  | 📨 Email    | Medewerker1: "FW: Afstemming intake architectuur"                                                                                                                          |
| 21 feb 2025  | 📨 Email    | Medewerker2: "RE: Afstemming intake architectuur" - Onze huidige inschatting van de planning: oplevering in april (tweede helft)                                           |
| 21 feb 2025  | 📨 Email    | Medewerker1: "FW: Afstemming intake architectuur"                                                                                                                          |
| 25 feb 2025  | 📨 Email    | Medewerker1: "RE: Omvang Applicatie" - Ik was in de veronderstelling dat we dat al tijdens de intake vastgelegd hadden                                                     |
| 25 feb 2025  | 📨 Email    | Medewerker2: "FW: Omvang Applicatie"                                                                                                                                       |
| 25 feb 2025  | 📨 Email    | Medewerker1: "RE: Omvang Applicatie" - Besproken de mail commerciële waarin we vorige maand CPU/Geheugen/Storage communiceerden                                            |
| 25 feb 2025  | 📨 Email    | Medewerker2: "RE: Omvang Applicatie" - Is dit niet wat we tijdens de intake...                                                                                             |
| 25 feb 2025  | 📨 Email    | Medewerker2: "Omvang Applicatie" - We zijn bezig met de kostenindicatie voor jullie aanvraag voor de omgeving                                                              |
| 25 feb 2025  | 📨 Email    | Medewerker1: "FW: Afstemming intake architectuur"                                                                                                                          |
| 25 feb 2025  | 📨 Email    | Medewerker1: "RE: Afstemming intake architectuur" - Als er manieren zijn de boel te versnellen horen we het graag                                                          |
| 4 maart 2025 | 📨 Email    | Medewerker1: "kostenindicatie hosting Applicatie" - Hierbij ontvang je de kostenindicatie voor de hosting van jullie Applicatie                                            |
| 4 maart 2025 | 📨 Email    | Medewerker2: "FW: kostenindicatie hosting Applicatie" - Opmerking: We hebben een kostenindicatie!                                                                          |
| 4 maart 2025 | 📨 Email    | Medewerker2: "RE: kostenindicatie hosting Applicatie" - Bedankt! Ik zal zorgen dat het bij ons de lijn in gaat                                                             |
| 6 maart 2025 | 📨 Email    | Medewerker1: "Informatie uitwisseling over Applicatie" - In ons interne besluitvormingsproces kwam de aanvraag voor hosting van Applicatie ook terecht bij onze security managers |
| 6 maart 2025 | 📨 Email    | Medewerker2: "RE: Informatie uitwisseling over Applicatie" - Natuurlijk, hier is de repository met meer informatie: github.com/Organisatie/applicatienaam                  |
| 6 maart 2025 | 📨 Email    | Medewerker2: "RE: Informatie uitwisseling over Applicatie" - Dank je wel!                                                                                                  |
| 6 maart 2025 | 📨 Email    | Medewerker1: "RE: kostenindicatie hosting Applicatie" - Beste collega, toch nog wat vragen over de kostenindicatie                                                         |
| 6 maart 2025 | 📨 Email    | Medewerker2: "RE: kostenindicatie hosting Applicatie" - Dag collega, Hierbij de antwoorden op jouw vragen                                                                  |
| 6 maart 2025 | 📨 Email    | Medewerker1: "FW: kostenindicatie hosting Applicatie" - Beste collega, wat vervolg vragen over de kostenindicatie                                                          |

**Legenda**

* 👥 - Meeting
* 📨 - Email
* 📄 - Document versie
* ✅ - Goedkeuring
* 📌 - Notities/Opmerkingen
* 🔒 - Security Review
* 🔄 - Actie
* 📋 - Document update
* 📞 - Telefoongesprek
* 💬 - Chat bericht