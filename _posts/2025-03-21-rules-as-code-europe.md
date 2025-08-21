---
title: "Rules as Code Europe"
date: '2025-03-21T13:00:00+01:00'
author: Anne
layout: post
lang: nl
tags:
  - '2025'
  - 'weeknotes'
---

Eerst even over weeknotes zelf. Kees schreef vorige
week [De Meta Weeknote: een weeknote over weeknotes](https://kees.it.com/weeknotes/2025/03/13/De-meta-weeknote.html),
de moeite waard om even te lezen!
Inmiddels schrijven meer collega's weeknotes, zie bijvoorbeeld [Eelco](https://eelco.hotting.it/),
[Roos](https://roosdegroot.nl/category/weekly/), [Aliza](https://tekofsky.nl/2025/03/14/iron-your-towels/), en
dus [Kees](https://kees.it.com/).

## Parijs

Begin deze week was ik in Parijs
voor [Rules as Code Europe](https://docs.numerique.gouv.fr/docs/1b64643b-7163-4a96-b78d-251f3a5e81e7/), een tweedaagse
bijeenkomst op 17 en 18 maart over het omzetten van wet- en regelgeving naar code.
Na mijn [eerdere posts](/2025/01/25/machine-law.html) over Machine Law was ik benieuwd hoe ver het veld inmiddels is.

## Staat van het veld

Mijn belangrijkste inzicht: ondanks dat er veel mensen aan werken, is het veld nog niet zo ver als ik had gehoopt. Er
zijn zeker interessante initiatieven, maar de meeste benaderingen pakken slechts deelaspecten aan. Ik zag weinig
projecten die zich richten op het semi-geautomatiseerd omzetten van wetteksten naar machine-leesbare formaten. En
projecten die de daadwerkelijke uitvoering baseren op zo'n representatie waren er al helemaal niet.

## Wat werkt al wel

De meest volwassen toepassingen die ik zag waren [Policy Engine](http://policyengine.org/)
en [LexImpact](https://leximpact.an.fr/). Beide zijn gericht op het doorrekenen van beleids- en wetsveranderingen. Ze
maken het voor beleidsmakers en politici mogelijk om direct te zien wat de effecten van bepaalde wetswijzigingen zouden
zijn. Dat is ontzettend waardevol en sluit aan bij een belangrijk deel van wat we met Machine Law voor ogen hebben

Frankrijk lijkt voorop te lopen met tools als [OpenFisca](https://openfisca.org) (hoewel dat in feite echt Python is,
wat naar mijn mening te expressief is voor dit doel) en [Publi.codes](https://publi.codes/) (een YAML-formaat dat wat
weg heeft van onze aanpak, maar volledig in het Frans is).

## De uitdaging van expressiviteit

Een terugkerend thema in de discussies was de juiste balans in expressiviteit van de gekozen representatietaal. Als een
taal te expressief is (zoals Python in OpenFisca), ben je in feite terug bij wetten diep verborgen in code. Maar als een
taal niet expressief genoeg is, moet je je in allerlei bochten wringen om bepaalde concepten uit te drukken.

Dit dilemma herken ik sterk in ons eigen werk aan Machine Law. We zoeken voortdurend naar die balans: een formaat dat
toegankelijk genoeg is voor niet-programmeurs, maar krachtig genoeg om complexe wettelijke constructies te modelleren.

## Interessante sidenote: Docs en Dinum

Wat leuk was aan dit bezoek, is dat het werd gehost door [DINUM](https://www.numerique.gouv.fr/dinum/) (Direction
Interministérielle du Numérique), de interministeriële digitale directie die rechtstreeks onder de Franse
premier valt. Deze organisatie is verantwoordelijk voor het ontwikkelen en implementeren van de digitale strategie van
de Franse overheid. DINUM streeft naar een effectievere, eenvoudigere en meer soevereine staat door middel van digitale
technologie. Het deed me heel sterk denken
aan [Government Digital Service](https://www.gov.uk/government/organisations/government-digital-service/about) uit het
Verenigd Koninkrijk.

DINUM is ook de club die [Docs](https://docs.numerique.gouv.fr) heeft gemaakt.
Dit open source Notion-alternatief stond vorige week even
op [#1 op Hacker News](https://news.ycombinator.com/item?id=43378239). Vanuit Nederland werken we, in samenwerking met
Duitsland en Frankrijk, hier ook aan mee. Zie bijvoorbeeld [Mijn Bureau](https://minbzk.github.io/mijn-bureau/).

Ik sprak Fransen die mijn directe Nederlandse collega's bleken te kennen. Het voelde als een kleine, maar groeiende
Europese community rond digitale overheidsvernieuwing.

## Wat nu?

De conferentie heeft mijn overtuiging versterkt dat we met Machine Law op het juiste spoor zitten. Hoewel het veld nog
in ontwikkeling is, geloof ik nog steeds dat deze aanpak gaat vliegen. We bouwen voort op het pionierswerk van anderen,
maar gaan ook een stap verder in onze ambities.

Ik heb waardevolle contacten gelegd met de mensen achter Policy Engine en Publi.codes. Deze verbindingen kunnen ons
helpen bij het verder ontwikkelen van onze ideeën en mogelijk leiden tot toekomstige samenwerkingen op Europees niveau.

Voor nu: verder op ons pad, met hernieuwde energie en inzichten uit Parijs.
