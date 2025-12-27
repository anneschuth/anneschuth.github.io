---
title: "Wanneer bouwen, wanneer kopen"
date: '2025-12-02T11:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
---


[Vorige week vrijdag](/2025/11/28/makelaar-of-maker.html) schreef ik in de trein terug vanuit Berlijn over de spanning
tussen makelaar en maker. Maar wanneer moet je nu eigenlijk zelf bouwen, en wanneer kopen of uitbesteden? We hebben een
taal nodig om dat gesprek te voeren.

> Update 27 december: ik schreef een vervolg: [AI erodeert](/2025/12/27/ai-erodeert.html). Wat als de Wardley Map hoogte had? En wat doet AI met dat landschap?

## Wardley Maps

[Simon Wardley](https://blog.gardeviance.org/) ontwikkelde een visuele methode om dit soort strategische beslissingen te
nemen: Wardley Maps. Het idee komt voort uit frustratie met traditionele strategietools. SWOT-analyses en
businessplannen zien er professioneel uit, maar missen vaak context. Ze vertellen je niet *waar* je bent en *waarheen*
je beweegt.

Een Wardley Map is een landkaart voor je organisatie. Net als een geografische kaart heeft hij een anker (de gebruiker
bovenaan), posities (waar staan je componenten) en beweging (hoe evolueren ze over tijd).

**De horizontale as** laat zien hoe volwassen een technologie is:

- **Genesis**: nieuw, experimenteel, onzeker. Niemand weet nog precies hoe het werkt.
- **Custom**: in ontwikkeling, nog geen standaard. Je bouwt het zelf omdat er geen alternatief is.
- **Product**: volwassen, meerdere aanbieders. Je kunt kiezen uit opties.
- **Commodity**: gestandaardiseerd, utility. Het is een nutsvoorziening, zoals elektriciteit.

Alles beweegt van links naar rechts. Wat vandaag genesis is, wordt morgen custom, dan product, dan commodity. Dit is
geen keuze maar een natuurwet van technologie.

**De verticale as** laat zien hoe zichtbaar een component is voor de eindgebruiker. Bovenaan staat wat de burger direct
ziet, onderaan de onzichtbare infrastructuur.

De **lijnen** tussen componenten tonen afhankelijkheden: wat heeft wat nodig om te werken? Dit maakt de waardeketen
zichtbaar.

## De beslisregel

De vuistregel is eenvoudig:

- **Links op de kaart = bouwen**. Je weet nog niet precies wat je wilt. Je hebt de kennis nodig om te begrijpen wat
  mogelijk is. Uitbesteden leidt tot specificaties die niet kloppen.
- **Rechts op de kaart = inkopen of uitbesteden**. Het is commodity. Geen differentiatie. Zelf bouwen is verspilling.

De fout die organisaties maken: alles behandelen zoals het bij hun cultuur past. Bouwers bouwen alles, ook commodities.
Kopers kopen alles, ook genesis componenten die nog niemand goed begrijpt.

## Bouwen is beleid maken

Bij genesis gaat het dieper dan "er is nog geen product om te kopen". Het bouwproces en het denkproces zijn
onlosmakelijk verbonden. Je ontdekt wat je wilt door te bouwen. De specificatie ontstaat tijdens het maken.

Bij een commodity weet je precies wat je nodig hebt. Stroom, opslag, rekenkracht. Je kunt het specificeren en inkopen.
Bij genesis weet je dat niet. Je kunt geen aanbesteding schrijven voor iets dat je nog niet begrijpt.

Voor de overheid betekent dit: bij componenten als RegelRecht of proactieve dienstverlening kun je niet een
aanbesteding schrijven en het over de schutting gooien. Engineers en beleidsmakers moeten [samen
optrekken](/2025/10/21/praten.html#wat-dit-betekent-voor-de-overheid). Het bouwen IS het beleidsproces. Software maken =
beleid maken.

## Nederlandse overheidsbouwblokken

Hoe ziet dit er concreet uit? De kaart hieronder toont een perspectief van de Nederlandse overheid als geheel. Niet
vanuit een individuele organisatie, maar vanuit ons allemaal samen.

![Evolutie van links naar rechts. Budget van rechts naar links.](/assets/wardley-map-overheid.png)

De standaard Wardley terminologie (bouw/koop/outsource) past net niet goed op de overheid. Je kunt DigiD niet "kopen"; er is geen markt. Logius, de leverancier, is onderdeel van de Rijksoverheid. Dus heb ik de labels aangepast.

**Genesis (EXPERIMENTEER)**: Proactieve dienstverlening, [RegelRecht](https://minbzk.github.io/regelrecht/). Dit zijn
dingen die we nog aan het uitvinden zijn. Hier moeten we zelf kennis opbouwen.

**Custom (ONTWIKKEL)**: [OpenZaak](https://openzaak.org/), [NL Design System](https://nldesignsystem.nl/),
[Haven](https://haven.commonground.nl/), FSC/NLX, [Haal Centraal](https://vng-realisatie.github.io/Haal-Centraal/).
Componenten die overheden samen ontwikkelen. Nog geen standaard, maar wel gedeelde kennis.

**Product (STANDAARD)**: DigiD, MijnOverheid, eHerkenning, Basisregistraties. Centrale voorzieningen uit
de [Generieke Digitale Infrastructuur](https://www.digitaleoverheid.nl/mido/generieke-digitale-infrastructuur-gdi/) die
we als overheid zelf hebben gebouwd en gestandaardiseerd.

**Commodity (MARKT)**: Cloud, SMS, Betalen. Echte commodities die we van de markt halen. Maar ook hier staan
Diginetwerk en PKIoverheid: commodities die we zelf hebben gebouwd. Had de markt dit kunnen leveren? Misschien, maar we
kozen voor eigen regie.

## Is commodity wel commodity voor een overheid?

Maar de simpele regel "commodity = outsource" mist iets, zeker voor een overheid. Cloud is technisch een commodity,
standaard, inwisselbaar. Maar is dat wel zo voor de overheid?

Overheden zijn geen kleine afnemers. Een ministerie of zelfs gemeente heeft geen twee VMs nodig, maar complete
infrastructuur. De hypervisorlaag die bij publieke cloud de multi-tenancy mogelijk maakt is voor grote afnemers
onnodige overhead. Met voldoende schaal kun je eigen bare-metal infrastructuur draaien.

Daar komen de specifieke eisen bij. BIO, AVG, datalocatie, DigiD-koppelingen, Diginetwerk-aansluiting. Dit zijn geen
standaard clouddiensten die je bij elke provider krijgt. [Haven](https://haven.commonground.nl/) op eigen hardware is
technisch haalbaar voor organisaties met de juiste schaal en kennis.

En dan zijn er de strategische vragen rond **digitale soevereiniteit**:

- **Exitstrategie**: kun je eraf als het moet? ([1 cloud is geen cloud](/2025/11/28/makelaar-of-maker.html#1-cloud-is-geen-cloud))
- **Datalocatie**: waar staan je gegevens en onder welk recht?
- **Leveranciersafhankelijkheid**: hoeveel moeite kost het om te wisselen?

Dit verklaart initiatieven als [openDesk](https://www.opendesk.eu/) en
[ZenDiS](https://www.zendis.de/) in Duitsland. Technisch gezien zijn kantoorautomatisering en cloud commodities.
Strategisch gezien wil je er misschien toch meer controle over.

De kaart vertelt je *wat* iets technisch is. Maar de beslisregel is asymmetrisch: links op de kaart *moet* je zelf
bouwen, er is geen alternatief. Rechts op de kaart *kun* je uitbesteden, maar dat betekent niet dat je het *moet*. Juist
daar spelen soevereiniteitsoverwegingen.

## Verder lezen

- [Introductievideo door Simon Wardley](https://www.youtube.com/watch?v=L3wgzl2iUR4) (als je één ding bekijkt, dit)
- [Wardley Maps](https://learnwardleymapping.com/)
- [Simon Wardley's blog](https://blog.gardeviance.org/)
