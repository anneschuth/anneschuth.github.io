---
title: "Linked Data Considered Harmful"
date: '2025-10-23T09:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
  - 'linked-data'
  - 'semantisch-web'
  - 'architectuur'
---

Deze week was het weer raak. Of we niet Linked Data konden gebruiken. En dan moet ik uitleggen waarom dat een slecht
idee is. Hier een poging dat op papier te krijgen.

## Het Fundamentele Probleem: Granulariteit

Luisterend
naar [Demis Hassabis in de Lex Fridman podcast](https://pocketcasts.com/podcast/lex-fridman-podcast/78c58610-9061-0136-7b92-27f978dac4db/475-demis-hassabis-future-of-ai-simulating-reality-physics-and-video-games/ba47aece-4f20-44ab-b9aa-197ead7ca7e4)
realiseerde ik me waarom het mis gaat met linked data. Het is makkelijk om de verkeerde granulariteit te kiezen voor de
dingen die je wilt modelleren.

Hassabis legt uit: "You got to make a decision when you're modeling any natural system, what is the cutoff level of the
granularity that you're going to model it to? And then it captures the dynamics that you're interested in. So probably
for a cell I would hope that would be the protein level, and that one wouldn't have to go down to the atomic level."

Precies. Als je een cel modelleert, stop je op het niveau van eiwitten. Je hoeft niet door naar het atomaire niveau. Je
kiest de granulariteit die de dynamiek vastlegt waarin je geïnteresseerd bent.

Linked data doet het omgekeerde. Het verleidt je om alles tot op het meest granulaire niveau te modelleren. Elke
property, elke relatie, elk detail moet een URI krijgen, moet semantisch gedefinieerd worden. Het is modelleren op
atomair niveau terwijl je geïnteresseerd bent in dynamiek op celniveau.

Het resultaat? Systemen die zo gedetailleerd zijn dat ze onbruikbaar worden. Ontologieën die zo verfijnd zijn dat
niemand ze begrijpt. Discussies over nuances die er praktisch niet toe doen.

Eerst even flashbacks naar mijn tijd aan de universiteit, toen Tim Berners-Lee's visie van het Semantische Web werd
onderwezen. Machines die het web begrijpen, automatische integratie, intelligente agents.
Ik weet eerlijk gezegd niet of ik daar ooit echt enthousiast over was. Het idee is natuurlijk elegant, maar al best snel
was duidelijk dat dit nooit iets zou worden. Net zoals klassieke "expert systemen" - theoretisch mooi, praktisch een
doodlopende weg.

Twintig jaar later is die conclusie alleen maar harder geworden. Niet alleen omdat ik cynisch ben geworden, maar
omdat ik te vaak heb gezien wat er gebeurt wanneer mensen deze technologieën proberen te gebruiken. De papieren tijger
van linked data ziet er prachtig uit in vergaderzalen, maar valt uit elkaar zodra je hem in productie probeert te
brengen.

## De Linked Data Rabbit Hole

Het begint altijd onschuldig. Iemand zegt: "We moeten onze data beter delen tussen systemen. Laten we linked data
gebruiken!" Het klinkt logisch. Semantische standaarden, universele identifiers, ontologieën. De theorie is
verleidelijk.

Dan begint het werk. Je moet URIs bedenken voor alles. Je moet kiezen uit tientallen ontologieën, of erger nog, je eigen
ontologie maken. Je moet RDF/XML of Turtle leren, syntaxes die zelfs ervaren programmeurs als onleesbaar ervaren. Je
moet een SPARQL endpoint opzetten en hopen dat de performance acceptabel is (spoiler: dat is het meestal niet).

En dan begint het échte probleem: mensen gaan elk atoom in de wereld modelleren. Is een persoon een Agent of een Person?
Is een organisatie een legalEntity of een CorporateBody? Wat is het verschil tussen een Document en een
InformationResource? De discussies zijn eindeloos. Het modelleren houdt nooit op. Er is altijd nóg een edge case, nóg
een subtiliteit die gemodelleerd moet worden.

De grote illusie is dat linked data domein-overstijgend zou zijn. "Als we het goed modelleren," zegt men, "kunnen we
dezelfde ontologie gebruiken voor zorg, onderwijs, én belastingen!" Het klinkt mooi. Het is ook complete onzin.

Elk domein heeft zijn eigen context, zijn eigen begrippen, zijn eigen nuances. Een "patiënt" in de zorg heeft hele
andere eigenschappen en relaties dan een "student" in het onderwijs, ook al zijn het allebei personen. Probeer dat in
één ontologie te vatten en je krijgt ofwel iets zo generiek dat het nutteloos is, ofwel iets zo complex dat niemand het
begrijpt.

En het ironische? Ondertussen bouwen developers gewoon domein-specifieke APIs met JSON schemas die perfect werken binnen
hun domein. Ze hebben de illusie van universele semantiek allang opgegeven.

Uiteindelijk heb je misschien een werkend systeem. Het is traag, niemand begrijpt hoe het werkt, en nieuwe developers
kijken je aan alsof je gek bent geworden. "Waarom gebruiken we geen JSON?" vragen ze. Goede vraag.

## Language Models: Het Einde van Formele Semantiek

En dan is er de olifant in de kamer: moderne language models hebben de hele linked data premisse achterhaald.

De belofte van linked data was dat machines data zouden kunnen "begrijpen" door formele semantische beschrijvingen. RDF
zou de betekenis vastleggen, ontologieën zouden concepten definiëren, en reasoning engines zouden logische conclusies
trekken.

Language models doen gewoon wat linked data beloofde, maar dan beter. Ze extraheren betekenis rechtstreeks uit
natuurlijke taal. Ze begrijpen context zonder formele definities. Ze kunnen redeneren over relaties zonder ontologieën.
En ze doen dit op een schaal waar linked data alleen maar van kon dromen.

Wil je een agent die data uit verschillende bronnen kan begrijpen en integreren? Train een language model op je
documentatie. Het begrijpt de nuances, de context, de impliciete betekenis. Zonder dat je eerst elk concept moet
modelleren als RDF triples.

Wil je zoeken over heterogene databronnen? Embedding models brengen semantisch vergelijkbare concepten samen zonder dat
ze dezelfde URI delen. Gerelateerde concepten worden automatisch herkend, zonder eindeloze ontologie-discussies.

Wil je wet- en regelgeving machine-leesbaar maken? Language models kunnen wetgeving direct interpreteren en zelfs
inconsistenties detecteren. Zonder dat je eerst een semantisch model van het hele rechtssysteem moet bouwen.

Dit is niet alleen een verschil in aanpak. Het is een fundamenteel ander paradigma. Linked data wilde betekenis
formaliseren. Language models leren betekenis uit gebruik. Linked data wilde perfecte, expliciete semantiek. Language
models werken met probabilistische, impliciete semantiek die goed genoeg is voor de praktijk.

En het werkt. ChatGPT beantwoordt vragen over miljarden webpagina's zonder een enkele RDF triple. GitHub Copilot
begrijpt code zonder formele ontologieën. Moderne zoekmachines gebruiken embeddings, niet SPARQL.

De ironie is dat Tim Berners-Lee intelligente agents beloofde die het web zouden begrijpen. Die agents zijn er nu. Ze
heten language models. En ze hebben geen linked data nodig.

## Waarom Blijft Het Terugkomen?

Hier is mijn theorie: linked data blijft terugkomen omdat het de eigenschappen heeft waar besluitvormers naar zoeken.
Het heeft de aura van "enterprise-grade," van "toekomstbestendig," van "strategisch." Het heeft indrukwekkende
standaarden van het W3C. Het heeft academische geloofwaardigheid.

Het is een oplossing die goed klinkt in presentaties. Je kunt prachtige diagrammen maken. Je kunt praten over "
semantische interoperabiliteit" en "federated queries." Maar het heeft niet de eigenschappen waar implementerende teams
om geven: snelheid, eenvoud, werkbaarheid. Die spanning tussen hoe het klinkt en hoe het werkt - dat is het probleem.

En zoals ik [eerder schreef over architectuur](/2025/06/23/toch-een-architect.html): het grootste gevaar van
architectuur als aparte discipline is de neiging tot overmatige abstractie. Linked data is die abstractie in zijn meest
pure vorm.

## De Overheid en Linked Data

Wat me zorgen baart is hoeveel overheidsorganisaties nog steeds linked data pushen. Ik zie voorstellen voorbijkomen
voor "nationale dataplatforms" gebouwd op RDF. Ik zie architecten die linked data als oplossing zien voor
data-integratie tussen departementen.

Dit gaat mis. Niet omdat de mensen incompetent zijn, maar omdat linked data fundamenteel niet schaalt. Niet technisch,
niet organisatorisch, en niet praktisch.

Het echte probleem van data-integratie tussen overheidssystemen is niet technisch. Het is organisatorisch. Het is
governance. Het is de vraag wie eigenaar is van welke data, wie toegang heeft, wie onderhoud doet. Linked data lost geen
van deze problemen op. Het voegt alleen een laag technische complexiteit toe die het lastiger maakt om echte vooruitgang
te boeken.

## Wat Dan Wel?

Als je echt data wilt delen tussen systemen:

1. Begin niet met technologie. Begin met de vraag: welke data moet gedeeld worden, met wie, en waarom?

2. Kies de simpelste technologie die werkt. Vaak is dat REST APIs met JSON - simpel, breed geadopteerd, en begrijpelijk
   voor elke developer.

3. Als je graafstructuren nodig hebt, overweeg een graph database zoals Neo4j. Ze bieden flexibele relaties en graph
   queries zonder de semantische overhead. Maar wees eerlijk: heb je echt graafstructuren nodig?

4. Investeer in documentatie, niet in ontologieën. Goede API docs met voorbeelden en OpenAPI specs zijn meer waard dan
   perfecte semantische definities die niemand begrijpt.

5. Schrijf pragmatische mapping code tussen systemen. Het is niet elegant, maar het werkt. En als je domein verandert,
   pas je de mapping aan.

6. Bouw in iteraties. Start klein, test met echte gebruikers, leer, pas aan.

7. En belangrijkst: betrek de mensen die het systeem moeten bouwen en gebruiken bij de beslissing. Niet alleen de
   architecten.

## Tot Slot

Ik ben niet tegen linked data uit principe (al zijn pointy brackets wel erg lelijk). Er zijn domeinen waar RDF redelijk
werkt: gestructureerde website metadata (zoals schema.org), bibliotheken, wetenschappelijke datasets, cultureel erfgoed.
Projecten als Wikidata en
DBpedia hebben waarde. Wat deze gevallen gemeen hebben: relatief stabiele domeinen, beperkte scope, en vaak academische
contexten waar de overhead geaccepteerd wordt.

Al is het veelzeggend dat zelfs deze "succesvolle" projecten hun eigen linked data infrastructuur moeten omzeilen voor
basale functionaliteit. Wikidata bijvoorbeeld heeft full-text search uitgeschakeld op hun SPARQL endpoint - te traag. In
plaats daarvan gebruiken ze Elasticsearch via de MediaWiki API. De meeste RDF triple stores gebruiken Lucene of
Elasticsearch voor full-text search - externe systemen omdat de RDF infrastructuur het niet aankan.

Als zelfs de showcase projecten van linked data hun eigen technologie moeten omzeilen voor iets zo fundamenteels als
zoeken in tekst, wat zegt dat dan over de geschiktheid van de technologie?

Maar als je een zeer specifiek probleem hebt waarvoor RDF echt de beste oplossing is, wees dan eerlijk over de
trade-offs. De leercurve is steil. De performance is slecht. De tooling is matig. En de kans is groot dat je probleem
beter opgelost wordt met simpelere technologie.

Na bijna twee decennia heeft linked data bewezen dat het geen revolutie gaat brengen. Het is een niche technologie voor niche problemen, niet de toekomst van data-integratie.

Het is tijd om dat te erkennen en verder te gaan.

Als je dit leest en denkt "maar linked data heeft ons enorm geholpen!", dan ben ik oprecht benieuwd naar je
ervaring. [Stuur me een bericht](/about). Misschien leer ik iets nieuws. Maar na 20 jaar wachten op de Semantische Web
revolutie ben ik niet optimistisch.

Voorlopig blijf ik [maken boven schrijven](/2025/04/11/maken-over-schrijven.html): JSON schrijven, API's bouwen,
en [demo's maken die werken](/2025/05/02/demo.html). En ik blijf waakzaam voor elegante abstracties die het in productie
niet leveren.
