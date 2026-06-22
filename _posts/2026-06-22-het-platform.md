---
title: "Het platform"
date: '2026-06-22T10:00:00+02:00'
author: Anne
layout: post
lang: nl
tags:
  - '2026'
  - 'architectuur'
  - 'maken'
---

Eerder, in [Techbedrijf](/2026/03/20/techbedrijf.html), gaf ik acht argumenten waarom de overheid platform engineering nodig heeft. Wat ik daar oversloeg, is uitleggen wat het eigenlijk ís. Ik gebruikte woorden als *self-service*, *golden paths* en *compliance als default*, alsof ze zichzelf verklaren. Een collega vroeg me laatst: ja, maar wát is het dan? Terechte vraag. Hier mijn poging het concreet te maken. En aan het eind kom ik bij het stuk dat me het meest bezighoudt. Want bij de overheid ziet een platform er anders uit dan bij een bedrijf. Juist dat deel ontbreekt nog.

## Het probleem

Software schrijven is het kleinste deel van software maken. Onder elke draaiende applicatie zit een onderbouw die niemand ziet zolang het werkt. De code moet ergens gebouwd worden, getest, verpakt en neergezet. Er is een netwerk nodig, een database, een kluis voor secrets, een certificaat, een domeinnaam. Het geheel moet gemonitord worden, want je wilt weten dat er iets stukgaat voordat een burger het merkt. Het moet beveiligd worden, en die beveiliging moet aantoonbaar zijn. En een nieuwe versie uitrollen mag de draaiende dienst niet platleggen. Veel werk, technisch, en het verandert constant.

Vroeger lag dat bij een aparte afdeling. Ontwikkelaars schreven code en gooiden die over de schutting naar beheer, dat de code in productie zette en draaiende hield. Dat had een bekende kwaal. De mensen die de code schreven voelden de pijn van slecht draaiende software niet, en de mensen die de pijn voelden konden de code niet veranderen. Verantwoordelijkheid en zeggenschap lagen op verschillende plekken. Traag, en bij elke storing wees iedereen naar de ander.

De beweging die daarop kwam, DevOps, loste dat op met één regel: het team dat iets bouwt, draait het ook. Wie de code schrijft staat 's nachts op als de boel omvalt. Hard, maar het zet de prikkel goed, want een team dat zijn eigen storingen oplost gaat vanzelf code schrijven die minder storingen geeft. De schutting verdween en de snelheid ging omhoog.

Alleen verschoof daarmee die hele onderbouw naar elk team afzonderlijk. Elk team moest nu zijn eigen pijplijn inrichten, zijn eigen monitoring opzetten, zijn eigen beveiliging regelen. Zelf kiezen uit tientallen gereedschappen die het niet had bedacht en zelden begreep. Een team van vijf dat een vergunningaanvraag bouwt, werd zo parttime expert in dingen die niets met vergunningen te maken hebben. Dat schaalt niet. Aandacht die naar de infrastructuur gaat, gaat niet naar het probleem waarvoor het team is aangenomen. En omdat ieder team het zelf inrichtte, deed ieder team het nét anders. Tien teams, tien manieren om uit te rollen, tien manieren om secrets te bewaren. Vaak niet eens uit eigenwijsheid, maar omdat een team simpelweg niet kon zien dat een ander het probleem al had opgelost. Dus bouwde dat team het zelf, nog een keer. Twee jaar later is het een moeras, waarin niemand meer weet waarom dit team deze keuze maakte en dat team die.

## De ingreep

Platform engineering pakt die onderbouw, maakt hem één keer goed, door een team dat er verstand van heeft, en zet hem klaar voor de teams die erbovenop bouwen. Geen afdeling die het werk weer overneemt, want dan heb je de schutting terug. Een gereedschap dat een ontwikkelaar zelf gebruikt, zonder een ticket in te dienen en te wachten, en zonder de complexiteit eronder te hoeven snappen.

In dat woordje zélf zit het verschil met het oude beheer. De ontwikkelaar blijft aan het stuur, maar bouwt niet meer alles zelf. De voorziening is er al, hij pakt die en gaat door met zijn eigenlijke werk. Vroeger was het: dien een verzoek in en wij doen het, op onze tijd. Nu is het: hier staat het, gebruik het wanneer je wilt, wij houden het goed. Hij drukt op de knop, het platformteam zorgt dat er iets deugdelijks achter zit.

Dat is in [Techbedrijf](/2026/03/20/techbedrijf.html) de multiplier: een team klikt op "nieuw project" en krijgt een repository met CI/CD, monitoring, beveiligingsscans en een uitrol naar een omgeving die aan de eisen voldoet. In minuten, waar het nu [93 dagen](/2025/03/07/hosting-in-slow-motion.html) kost. Maar het werkt alleen als teams de voorziening ook echt gaan gebruiken. Daar zit de kern van platform engineering, en die kern is een handvol ideeën die ik stuk voor stuk wil langslopen.

## Het gebaande pad

Het belangrijkste idee is het gebaande pad, bij Spotify een [*golden path*](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem/) genoemd. Dat is de aanbevolen, ondersteunde manier om iets te bouwen. Aanbevolen, niet verplicht. De weg die geplaveid is, met goede borden, waarvan je weet dat hij je op je bestemming brengt, en waar iemand klaarstaat als je vastloopt.

Het idee staat of valt met dat je eraf mag. Doe je dat, dan draag je voortaan zelf de last die het platform anders droeg. Je richt je eigen monitoring in, regelt je eigen beveiliging, lost je eigen storingen op, zonder de hulp die op het pad vanzelf meekomt. Het platform houdt je niet met dwang op de weg. Het maakt de weg zo goed dat je er uit jezelf op blijft.

Dat klinkt als een detail en dat is het niet. Dwang lokt ontwijking uit. Verplicht teams tot deze ene manier, en een deel gaat eromheen werken, vaak waar je het niet ziet, en dan heb je de versnippering terug plus een handhavingsprobleem erbovenop. Is de goede manier ook de makkelijkste, dan kiezen teams die uit zichzelf, simpelweg omdat de rest meer werk is. Aantrekkingskracht houdt het langer vol dan een regel. Ze sluit aan op wat een team toch al wil.

Een goed gebaand pad doet meer dan een nieuw project opzetten. Daar trappen veel platforms in: ze automatiseren het begin, van leeg scherm naar werkende repository, en laten de rest van het leven van de applicatie links liggen. Maar software wordt één keer opgezet en daarna jaren onderhouden, aangepast, uitgerold, bij de overheid soms decennia. De meeste pijn zit niet op dag één. Die zit op dag vijftig, en op dag vijftienhonderd. De paden die ertoe doen zijn dus de dingen die je telkens weer doet en die tijd vreten: een nieuwe versie uitrollen, een dependency bijwerken, een storing uitpluizen, een audit doorstaan.

## Een product, geen voorschrift

Niemand is verplicht het platform te gebruiken. Dus moet je dat gebruik verdienen. Dat dwingt je om het te behandelen als een product dat mensen vrij kunnen kiezen of links laten liggen, en niet als infrastructuur die je van bovenaf oplegt.

Een product heeft gebruikers, geen mensen die nu eenmaal moeten. Er is een eigenaar die erop wordt afgerekend of mensen het fijn vinden. Het wordt beter door naar die gebruikers te luisteren, niet doordat de bouwers hun zin doordrijven. En iemand houdt bij of het gebruikt wordt. Wordt het genegeerd, dan heeft het platformteam iets verkeerd gedaan. De schuld ligt niet bij de gebruiker die de waarde niet inziet. Dat voelt ongemakkelijk voor een organisatie die gewend is interne voorzieningen op te leggen, en het is precies wat een platform laat slagen.

Dat bijhouden is geen bijzaak. Er is een gangbare meetlat voor of softwarelevering goed loopt, in dit veld bekend als de [DORA-metrieken](https://dora.dev/guides/dora-metrics-four-keys/): hoe vaak je uitrolt, hoe lang een wijziging erover doet om in productie te staan, hoe vaak een uitrol misgaat, en hoe snel je weer overeind krabbelt als er iets stuk is. Een platform dat deugt, verbetert die cijfers voor de teams die het gebruiken. Deugt het niet, dan zie je dat in de cijfers, in plaats van erover te moeten kibbelen in een stuurgroep.

## Waar je niet vanaf mag

Je mag van het gebaande pad af, maar niet overal. Op sommige plekken staat een vangrail. Beveiliging volgens de [BIO](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/) is geen vrijblijvende suggestie waar je omheen mag werken, en [toegankelijkheid](/2026/02/20/skills.html) voor mensen met een beperking is geen smaakkwestie. Daar staat een vangrail, geen bordje.

Maar pas op dat je niet overal vangrails neerzet. Een platform dat de hele weg afzet verstikt juist de teams die het wilde helpen, en dan ben je terug bij dwang en ontwijking. De kunst zit hem in de verdeling: wat echt niet ter discussie staat wordt vangrail, de aanbevolen route wordt het gebaande pad, en de rest laat je aan de gebruiker. Dat bedoelde ik in [Techbedrijf](/2026/03/20/techbedrijf.html) met compliance als default en standaarden in code. Geen memo die zegt "gebruik TLS 1.3", maar een platform waarop TLS 1.3 gewoon aanstaat.

## Een portaal is geen platform

Hier komt vaak de tegenwerping: zoiets hebben we toch al? Kijk naar [developer.overheid.nl](https://developer.overheid.nl/), met zijn kennisbank, registers van API's, standaarden, tutorials en tooling. Dat is er, en het is goed gemaakt en breed bruikbaar. Maar het is een portaal, en een portaal en een platform zijn twee verschillende dingen.

Het verschil zit in wat je er doet. Een portaal lees je. Je zoekt er iets op, je vindt een uitstekende tutorial over hoe je een API bouwt, je pakt er een linter en draait die in je eigen omgeving. Een platform ís die omgeving. Het is niet de plek waar staat hóe je iets moet doen, het is de plek waar je het dóet: je code staat er, je pijplijn draait er, je rolt je software er naar productie uit. Het verschil tussen een kookboek en een keuken, en je wilt ze allebei.

En dat verschil zit hem niet alleen in de techniek, maar in de prikkel. Naar een portaal moet je toe, uit jezelf, omdat je iets wilt opzoeken. Ik werk in dit veld en ik kom er zelf bijna nooit. Niet omdat het tekortschiet, maar omdat ik er op een gewone werkdag niets te dóen heb. Een platform heeft dat probleem niet, want je kunt er niet omheen. Je werkt er nu eenmaal doorheen, dus je bent er, elke dag, of je nu zin hebt of niet. Een portaal vecht om je aandacht. Een platform heeft haar al, omdat het in je werk zit ingebakken. Het gevaar zit dan ook niet in het portaal, maar in de gedachte dat je er al bent zodra het er staat.

## En voor de overheid ligt het net anders

Tot hier geldt het verhaal voor elke grote organisatie die veel software maakt. Een bank, een verzekeraar, een groot techbedrijf: allemaal hebben ze die onzichtbare onderbouw, allemaal kennen ze de versnippering, en allemaal hebben ze baat bij een gebaand pad. Bij de overheid komt er iets bij dat de hele vorm van het platform verandert.

Een bedrijf is één organisatie. Aan het eind van een discussie hakt een directie de knoop door, en als die zegt dat iedereen het gebaande pad gebruikt, dan gebeurt dat. De overheid is geen organisatie maar een verzameling ervan, elk met een eigen wettelijke taak, een eigen bewindspersoon, een eigen tempo. De Belastingdienst neemt geen orders aan van een centrale ICT-club, hoe goed die club ook is. Eén centraal platform optuigen en het iedereen opleggen: dat herhaalt een patroon dat we vaak genoeg hebben gezien. Een dure voorziening, vanuit het centrum bedacht zonder dat de gebruikers meededen. En de uitvoeringsorganisaties bouwen er uiteindelijk stilletjes omheen. Zelden hapert de techniek. Het hapert aan draagvlak, en draagvlak laat zich niet afdwingen.

Dan maar niets bouwen en alleen [regie voeren](/2025/11/28/makelaar-of-maker.html)? Nee, want regie zonder een werkende voorziening is weer een memo zonder iets erachter. Het moet allebei kunnen. Een uitvoeringsorganisatie zonder eigen engineeringcapaciteit moet bovenop het platform kunnen bouwen. En een organisatie die haar eigen infrastructuur draait, en daar goede redenen voor heeft, moet kunnen aansluiten zonder die infrastructuur op te geven. Een klein waterschap met één dienst heeft baat bij een kant-en-klare omgeving. De Belastingdienst geeft zijn productie aan niemand uit handen. De winst zit niet in wie de onderlaag bezit, maar in het feit dat beide werelden op hetzelfde platform terechtkunnen. Koppelen zonder alles op één hoop te gooien.

Er liggen al wat losse stukken. [Haven](https://haven.commonground.nl/) standaardiseert een deel van de hosting, [FSC](https://fsc-standaard.nl/) regelt veilige koppelingen tussen organisaties. Nuttig, maar het is een handvol bouwstenen waar er tientallen nodig zijn, en ze zijn los van elkaar ontstaan, met eigen aannames, en passen nog niet op elkaar. Wat ontbreekt is niet nog een steen. Het is om te beginnen vindbaarheid, discoverability: één plek waar een ontwikkelaar kan zien wat er al is, wie het beheert, of het iets voor hem is, en hoe hij het gebruikt. Zonder dat blijft precies het probleem bestaan waar dit stuk mee begon, dat je niet kunt vinden wat een ander al heeft gebouwd en het dus opnieuw doet. En bovenop die vindbaarheid komt de rest: de gebaande paden, de vangrails, de meting, de federatie. Bij elkaar is dat platform engineering. En dat is het stuk dat bij de overheid nog gebouwd moet worden.
