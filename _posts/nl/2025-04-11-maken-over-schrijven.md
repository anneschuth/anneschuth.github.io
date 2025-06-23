---
title: "Maken > Schrijven"
date: '2025-04-11T17:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
lang: nl
---

De naam "Bureau Architectuur" heeft me [sinds dag één](/2025/01/16/starting-bureau-architecture.html) aan het
denken gezet. Niet omdat er iets inherent mis is met architectuur, maar omdat het suggereert dat architectuur iets is
dat los staat van het daadwerkelijke bouwen. Een separate discipline, een aparte functie, een geïsoleerde
verantwoordelijkheid. Deze week heeft die spanning weer op verschillende manieren de kop opgestoken.

## De schijnbare tegenstelling

De tech-wereld heeft een complexe relatie met architectuur. We hebben architecten en we hebben engineers. We hebben
mensen die nadenken over wat we bouwen en mensen die daadwerkelijk bouwen. Althans, dat is de schijnbare tegenstelling
die veel organisaties in stand houden.

In de rijksoverheid zien we deze scheiding misschien wel in zijn meest extreme vorm. Architecten zitten vaak ver van de
werkvloer, produceren documenten vol met pijlen en blokken, en hebben weinig tot geen directe betrokkenheid bij de
implementatie van hun ideeën. Terwijl engineers aan de andere kant worstelen met de dagelijkse realiteit, zonder altijd
de grotere context te zien.

Een tekenend voorbeeld hiervan zijn de zogenaamde "programmeringsstafels" binnen de overheid. Een term die ik als enige
grappig en verwarrend lijk te vinden, omdat het NIETS met programmeren te maken heeft. Het gaat hier om product- en
portfoliomanagement - het beslissen over wat er gebouwd moet worden, niet over het daadwerkelijke programmeerwerk. De
verwarring in terminologie illustreert perfect hoe ver de werelden van beslissen en maken uit elkaar zijn gegroeid.
Opvallend genoeg lijkt niemand binnen de organisatie de term opmerkelijk te vinden - zo genormaliseerd is deze scheiding
al.

Natuurlijk zijn er uitzonderingen - architecten die dicht bij de implementatie staan, die regelmatig code schrijven of
direct samenwerken met developers. Deze mensen slaan juist die brug tussen concepten en uitvoering die zo essentieel is.
Maar ze opereren vaak ondanks de structuur, niet dankzij deze.

## Het gevaar van abstractie

Het grootste gevaar van architectuur als aparte discipline is de neiging tot overmatige abstractie.
Architectuurdocumenten vol met pijlen, blokken en idealistische beschrijvingen die misschien goed klinken in
vergaderzalen, maar die de complexiteit van implementatie onderschatten.

Abstractie is natuurlijk essentieel. Zonder het vermogen om te abstraheren zouden we verlamd raken door de oneindige
complexiteit van de werkelijkheid. Maar abstractie die niet regelmatig wordt getoetst aan de praktijk verliest zijn
verbinding met de werkelijkheid. Het wordt een luchtkasteel, mooi om naar te kijken maar onmogelijk om in te wonen.

Een perfect voorbeeld hiervan zie je in de wereld van Linked Data (RDF, triples, Turtle, DCAT, en alle andere
afkortingen die hierbij horen). Hier slaat de abstractie vaak door in het modelleren van werkelijk ALLES, tot aan het
niveau van individuele atomen. De belofte van een semantisch web waar alle data perfect met elkaar verbonden is, heeft
geleid tot een eindeloze reeks van steeds complexere ontologieën en standaarden. Maar in de praktijk worstelen veel
organisaties om er ook maar iets bruikbaars mee te bouwen, laat staan de beloofde interoperabiliteit te realiseren.

Om eerlijk te zijn: dit gevaar beperkt zich niet tot architecten. Ook engineers (ik) vervallen soms in premature
abstracties
of optimalisaties - het bouwen van complexe systemen voor problemen die misschien nooit zullen optreden, of het maken
van generieke oplossingen wanneer een eenvoudige specifieke oplossing voldoende zou zijn. Het verschil is dat de
feedback voor engineers vaak directer is - code die te abstract is daar werk je niet lekker mee.

Ik heb talloze voorbeelden gezien van architectuurdocumenten die technisch correct waren, maar praktisch onuitvoerbaar.
Of erger nog: die zo ver verwijderd waren van de realiteit dat ze niet eens als uitgangspunt konden dienen voor een
gesprek over implementatie. Het waren papieren tijgers, indrukwekkend in theorie maar machteloos in praktijk.

Dit is waar het concept van Machine Law zo interessant wordt. In onze Proof of Concept brengen we denken en maken direct
samen - we experimenteren met concepten en testen ze meteen in code. Een representatie die getoetst kan worden, die
gevalideerd kan worden, die direct laat zien waar de knelpunten zitten.

## De hereniging van denken en maken

Wat we eigenlijk nodig hebben, is geen Bureau Architectuur, maar een plek waar denken, schrijven, en maken samenkomen.
Waar architectuur ontstaat uit het bouwen, en waar bouwen wordt geïnformeerd door architecturale inzichten.

Dat betekent niet dat we geen architectuurprincipes of -patronen nodig hebben. Integendeel, die zijn essentieel. Maar ze
moeten geworteld zijn in de praktijk, getoetst aan de realiteit, en voortdurend aangepast op basis van wat we leren
tijdens het bouwen.

De beste architecten die ik ken zijn mensen die hun handen vuil hebben gemaakt met code, die hebben geworsteld met
implementatiedetails, die hebben ervaren hoe theoretisch elegante oplossingen soms praktisch onwerkbaar zijn. Het zijn
mensen die begrijpen dat architectuur geen doel op zich is, maar een middel om betere software te bouwen.

Tegelijkertijd zijn de beste engineers die ik ken mensen met een scherp oog voor patronen, voor structuur, voor de
grotere context. Mensen die niet alleen nadenken over hoe ze een specifiek probleem oplossen, maar ook hoe hun oplossing
past in het grotere geheel.

Het gaat niet om het afschaffen van specialisatie - mensen mogen (nee moeten) verschillende expertises en rollen hebben.
Het gaat erom dat deze rollen niet moeten verworden tot strikte scheidingslijnen die samenwerking belemmeren. Teams
functioneren beter wanneer er vloeiende grenzen zijn tussen de verschillende expertises, ook al hebben individuele
teamleden misschien hun eigen specialismen.

## Een nieuwe benadering

Misschien moeten we onze taal aanpassen. In plaats van te praten over architecten en engineers, over tekenen versus
maken, zouden we moeten praten over teams die samen bouwen aan oplossingen. Mensen die verschillende
perspectieven en vaardigheden inbrengen, maar die allemaal betrokken zijn bij het hele proces.

En misschien moeten we onze processen aanpassen. In plaats van architectuurdocumenten die worden "overgedragen" aan
implementatieteams, zouden we kunnen werken met gezamenlijke ontwerpsessies, met prototypes en experimenten, met een
continue dialoog tussen verschillende perspectieven.

Dit is wat ik probeer te bevorderen in mijn werk bij Bureau Architectuur (ironisch genoeg). Niet door architectuur als
discipline af te schaffen, maar door het terug te brengen naar zijn essentie: het vormgeven van systemen die werken voor
echte mensen in de echte wereld.

Uiteindelijk gaat het niet om architectuur zonder architecten, maar om een architectuur die ontstaat uit de gezamenlijke
inspanning van iedereen die betrokken is bij het bouwen van digitale oplossingen. Een architectuur die niet wordt
voorgeschreven, maar die ontstaat.
