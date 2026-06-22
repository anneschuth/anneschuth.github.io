---
title: "De standaard"
date: '2026-06-23T10:00:00+02:00'
author: Anne
layout: post
lang: nl
tags:
  - '2026'
  - 'architectuur'
  - 'maken'
---

[Gisteren](/2026/06/22/het-platform.html) eindigde ik met een opdracht en geen oplossing. Een overheidsplatform kan niet één centraal ding zijn dat je iedereen oplegt, want de overheid is geen organisatie maar een verzameling ervan. Het moet koppelen zonder alles op één hoop te gooien. En de eerste steen die ontbreekt is vindbaarheid: één plek waar je ziet wat er al is. Mooi, maar hóe dan? Een collega die het stuk las stelde precies die vraag, en ik bleef het antwoord schuldig.

Hier mijn poging. Het korte antwoord is dat je niet nog een platform bouwt. Je bouwt een afspraak. Een standaard die regelt hoe de losse platforms van al die organisaties elkaar kunnen vinden, zonder dat er één baas boven hangt die bepaalt hoe ze er vanbinnen uitzien.

## De spanning

In [Techbedrijf](/2026/03/20/techbedrijf.html) schreef ik dat een platform niet draait op goodwill. Het heeft mandaat nodig, en structurele financiering, en een organisatie die ervoor verantwoordelijk is. DigiD werkt omdat Logius het beheert met budget en een helder mandaat. Een overheidsbreed platform heeft datzelfde nodig.

Gisteren schreef ik het tegenovergestelde. Eén centraal platform optuigen en het iedereen opleggen herhaalt een patroon dat zelden goed afloopt. De Belastingdienst neemt geen orders aan van een centrale ICT-club, hoe goed die club ook is.

Allebei waar, en het lijkt elkaar uit te sluiten. Je hebt een sterke regie nodig, en je mag niets opleggen. De uitweg zit in de vraag wáár dat mandaat op slaat. Niet op de infrastructuur van elke organisatie, maar op de afspraak ertussen. Je verplicht niemand een bepaald platform te draaien. Je verplicht ze om vindbaar te zijn op één manier. Logius beheert het protocol en de dunne index, en daaronder houdt iedereen zijn eigen huis. Dat is een veel kleinere claim dan een centraal platform, en juist daarom haalbaar.

## Hetzelfde patroon, telkens weer

Het aardige is dat dit probleem niet nieuw is. Autonome partijen die elkaar moeten vinden zonder dat er een baas boven zit: het internet zelf doet niet anders, en een rij systemen heeft het opgelost. Als je ze naast elkaar legt, doen ze alle drie hetzelfde.

Eén, centraliseer alleen het allerdunste laagje. Een naamruimte zodat namen uniek zijn, en een verwijzer die zegt waar iets te vinden is. Meer niet. DNS werkt zo: een centrale wortel garandeert dat `belastingdienst.nl` van niemand anders is, en wijst door naar de servers van de Belastingdienst, die daarna hun eigen gang gaan.

Twee, laat de inhoud bij de eigenaar. De beschrijving van wat een organisatie aanbiedt, de adressen, de sleutels: dat staat bij die organisatie zelf, niet in een centrale database. De verwijzer weet alleen wáár het staat, niet wát erin staat.

Drie, regel vertrouwen met handtekeningen, niet met een poortwachter. Je gelooft een beschrijving omdat de eigenaar haar heeft ondertekend en jij die handtekening kunt controleren, niet omdat een centrale partij heeft gezegd dat het goed zit.

Het scherpste voorbeeld waar de overheid al middenin zit is [Peppol](https://peppol.org/), het netwerk voor elektronische facturen. Het werkt met een vier-hoekenmodel: jij stuurt naar jouw verzendpunt, dat stuurt naar het ontvangstpunt van de ander, dat levert af. Niemand legt een lijn met iedereen. Het vinden gaat in tweeën. Er is één centrale verwijzer, technisch gewoon DNS, die op de vraag "waar staat de informatie van deze organisatie?" een adres teruggeeft. Op dat adres staat de rest: welke documenten de organisatie aankan, via welk punt, met welke ondertekening. Die informatie staat verspreid over honderden zulke adressen, elk beheerd door wie het aangaat. De centrale verwijzer is piepklein en weet bijna niets. Wil je naar een ander verzendpunt, dan verhuis je, zonder dat je opnieuw aangemeld hoeft te worden. Geen lock-in.

Dichter bij huis doet [FSC](https://fsc-standaard.nl/) hetzelfde voor koppelingen tussen overheidsorganisaties. Daarover zo meer, want ik heb het gisteren tekortgedaan.

## Wat er al ligt

Want gisteren noemde ik FSC een los bouwsteentje, en dat klopt niet. FSC heeft een Directory: een onderdeel waar organisaties zich aanmelden en hun diensten publiceren, zodat een ander kan zien wie wat aanbiedt en hoe je verbinding legt. Dat is geen voorportaal van federatieve vindbaarheid. Dat ís het, voor diensten tussen organisaties. De standaard staat sinds eind 2024 op [versie 1.0.0](https://gitdocumentatie.logius.nl/publicatie/fsc/core/1.0.0/), wordt door Logius beheerd, en is op weg naar de lijst van standaarden die je moet toepassen of uitleggen waarom niet. De plumbing voor "koppelen zonder centraliseren" ligt er dus grotendeels. Wat eroverheen ontbreekt is een catalogus die verder reikt dan koppelvlakken.

En vindbaarheid is ook niet helemaal afwezig, wat ik gisteren te stellig bracht. [developer.overheid.nl](https://developer.overheid.nl/) heeft een API-register, inmiddels honderden API's van bijna honderd organisaties. Interessanter nog: dat register is net overgestapt van handmatig aanmelden naar oogsten. Organisaties kwamen niet uit zichzelf langs, dus haalt het register de beschrijvingen nu zelf op bij de bron. Datzelfde gebeurt al jaren voor datasets, waar data.overheid.nl de catalogi van honderden organisaties oogst en doorgeeft aan de Europese variant. En het [Federatief Datastelsel](https://federatief.datastelsel.nl/) heeft die vorm expliciet gekozen: elke aanbieder beschrijft zijn eigen spullen bij de bron, met een dunne centrale catalogus erbovenop.

Dat is goed nieuws, want het betekent dat de overheid het patroon van hierboven al draait. Alleen voor data en API's, niet voor de bredere voorzieningen van een platform. Er is geen catalogus waarin je een draaiende dienst, een gebaand pad of een herbruikbare bouwsteen terugvindt, met wie hem beheert en of hij bij jou past. En er staat niets over zulke vindbaarheid op de lijst van Forum Standaardisatie. Dat is het gat, smaller en harder dan "er is niets".

## De keuzes

Stel je bouwt die standaard. Dan zijn er een paar echte keuzes, en ik heb wel een voorkeur maar geen zekerheid.

De eerste gaat over hoe een organisatie zichzelf kenbaar maakt. Twee smaken. Of elke organisatie zet een machineleesbaar bestand op een vaste, voorspelbare plek op haar eigen domein, zodat een index dat kan ophalen. Het internet doet dit al overal: de manier waarop je inlogt met een account van elders, of waar je een `security.txt` vindt, werkt zo, en sinds vorig jaar bestaat er zelfs [een afspraak](https://www.rfc-editor.org/rfc/rfc9727.html) specifiek voor het kenbaar maken van API's op zo'n vaste plek. Of je gaat de oogst-route, zoals de datawereld met haar catalogi. Mijn voorkeur is allebei tegelijk: laat organisaties zichzelf beschrijven op een vaste plek, en laat een dunne index dat periodiek oogsten. Dat is precies de vorm die het Federatief Datastelsel al kiest, dus je sluit aan in plaats van iets nieuws te beginnen. In Begane Grond, de [klikbare schets](https://bg.rijks.app/) van zo'n platform die ik aan het maken ben, ziet dat eruit als een software-catalogus waar je van persoon naar team naar applicatie naar draaiende instance doorklikt. Dat is precies wat je over organisaties heen vindbaar wilt maken.

De tweede keuze gaat over vertrouwen, en daar zit een schuifregelaar. Aan de zuinige kant: een ondertekende beschrijving op een geverifieerd overheidsdomein, en je gelooft hem omdat de handtekening en het domein kloppen. Aan de rijke kant: een keten van ondertekende verklaringen waarin een ministerie instaat voor zijn uitvoeringsorganisaties, met centraal beleid dat naar beneden afdwingt wat niet ter discussie staat. Die rijke variant bestaat, heet [OpenID Federation](https://openid.net/specs/openid-federation-1_0.html), en is precies wat de Europese identiteitswallet aan het kiezen is, dus je werkt mee in plaats van eromheen. Daarmee kun je conformiteit aan de BIO of aan toegankelijkheid als een controleerbaar, intrekbaar keurmerk in de beschrijving zetten. Begin zuinig, bouw richting de keten als je de keten nodig hebt. In Begane Grond zie je waar dat heen wijst: artefacten met een SBOM en een handtekening, scorecards die per dienst tonen of de vangrails staan. De handtekening is geen sluitstuk maar het fundament onder hergebruik. Je durft de bouwsteen van een ander pas te draaien als je kunt nagaan waar hij vandaan komt.

Onder dat alles ligt nog een laag die ik hier laat liggen: hoe een voorziening er technisch uitziet zodra je hem gevonden hebt. De kortste samenvatting is dat je een capability aanbiedt als een API met een versie, en dat de implementatie eronder van de eigenaar blijft. Daar valt veel over te zeggen, en het is een andere laag dan de vindbaarheid waar dit stuk over gaat. Een waarschuwing hoort er wel bij. De verleiding is groot om te eisen dat iedereen dezelfde techniek draait, en dan ben je terug bij het opleggen waar gisteren tegen waarschuwde. De afspraak gaat over het koppelvlak, niet over de keuken erachter.

## Twee manieren om het te verprutsen

De systemen die werken laten ook zien hoe het misgaat. De eerste fout is een centrale partij in het werkende pad zetten. Een marktplaats waar al het verkeer doorheen moet, die de sleutels beheert en de index bezit. Dat schaalt prima tot de dag dat die partij wordt overgenomen of de stekker eruit trekt, en dan ligt iedereen plat. De verwijzer moet dun zijn en buiten het verkeer staan. De data blijft federatief.

De tweede fout is vindbaarheid als bijzaak behandelen. De fediverse, het netwerk van onafhankelijke sociale servers, federeert technisch prima maar je vindt er nauwelijks iets terug, omdat niemand de index vooraf heeft ontworpen. Een standaard waarvan vindbaarheid de hele bestaansreden is, moet die index vanaf dag één meenemen. Anders krijg je losse beschrijvingen die niemand bij elkaar harkt, en blijf je opnieuw bouwen wat een ander al heeft, precies het moeras waar dit hele verhaal mee begon.

## Waar het landt

Dus geen centraal platform, maar een dunne afspraak met een sterke eigenaar. Logius-vorm: mandaat en budget voor het protocol en de index, en verder houdt elke organisatie haar eigen infrastructuur. De Belastingdienst geeft niets uit handen. Een klein waterschap sluit aan met een vinkje. Beide staan in dezelfde catalogus.

Of zoiets gaat lukken weet ik niet. Een goede standaard is nog geen draagvlak, en draagvlak laat zich niet afdwingen, dat schreef ik gisteren al. Maar de stukken liggen er, en ze liggen dichter bij elkaar dan ik gisteren deed voorkomen. FSC voor het koppelen, het Federatief Datastelsel voor de oogst-vorm, de handtekeningen uit de toeleveringsketen, een register dat net is gaan oogsten. Begane Grond is mijn manier om te laten zien hoe die stukken in elkaar zouden grijpen: een schets aan de muur, geen product, niets dat draait en niets dat door iemand is vastgesteld. Maar wel iets om naar te wijzen en ruzie over te maken.

Wat ontbreekt is niet nog een steen. Het is de afspraak over hoe de stenen op elkaar passen. Die afspraak is de standaard, en die moet nog gemaakt worden.
