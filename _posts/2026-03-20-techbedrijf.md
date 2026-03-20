---
layout: post
title: "Techbedrijf"
date: '2026-03-20T10:00:00+01:00'
author: Anne
lang: nl
tags:
  - '2026'
  - 'weeknotes'
  - 'architectuur'
  - 'maken'
---

Ik krijg regelmatig de vraag wat platform engineering is en waarom de overheid zich daar druk om zou moeten maken. Mijn antwoord begint bij een these: de overheid is de facto het grootste en meest complexe softwarebedrijf[^bedrijf] van Nederland, en ze moet zich ook zo organiseren. Platform engineering is de manier om dat te doen. Hier acht argumenten.

[^bedrijf]: [Eerder zei ik](/2025/05/09/interview.html) dat de vergelijking tussen Spotify en de overheid "totaal mank gaat." Dat vind ik nog steeds, qua missie. Maar qua software-complexiteit helpt de vergelijking wel. 

## Argument 1: Softwarebedrijf

De bewering "de overheid is geen techbedrijf" is een categorisatiefout. Spotify maakt een muziek-app. De Belastingdienst verwerkt jaarlijks meer dan 10 miljoen aangiftes, met honderden wijzigingen per jaar in tientallen fiscale regelingen. UWV, SVB, DUO, RvIG: elk van deze organisaties draait software die complexer is dan wat de gemiddelde scale-up bouwt. De overheid heeft minstens zoveel software nodig als een techbedrijf, en die software is ook nog eens domeinspecifiek. Er is geen SaaS-product voor de Toeslagenberekening, voor het beheer van de BRP, of voor de WIA-beoordeling. Die software bestaat alleen voor de overheid, en moet dus door of voor de overheid gemaakt worden.

## Argument 2: Inkopen werkt niet

Het standaardantwoord is: "koop het in." Ruim de helft van de publieke sector geeft aan de komende jaren meer te gaan outsourcen[^whitelane]. Ondertussen loopt twee op de drie grote IT-projecten van de overheid vertraging op, met inmiddels 1,6 miljard euro aan budgetoverschrijdingen over 184 projecten[^ictrapportage]. Die overschrijdingen gaan over alle grote projecten, inclusief in-house. Maar het outsourcing-model heeft een structureel probleem bij domeinspecifieke software: de opdrachtgever moet exact specificeren wat gebouwd moet worden, en overheidsdomeinen zijn te complex om dat in watervaldocumenten te vangen. Het resultaat is eindeloze change requests, vendor lock-in, en systemen die niet aansluiten op de werkelijkheid.

[^whitelane]: [Dutch IT Sourcing Study 2026](https://www.eraneos.com/nl/persberichten/eraneos-en-whitelane-research-publiceren-resultaten-van-de-dutch-it-sourcing-study-2026/), Eraneos/Whitelane Research. 51% van de publieke sector is van plan meer uit te besteden.

[^ictrapportage]: [Rapportage Grote ICT-activiteiten 2024](https://www.binnenlandsbestuur.nl/digitaal/meer-ict-projecten-rijk-duurder-en-later-opgeleverd), gepresenteerd aan de Tweede Kamer oktober 2025.

[Eerder schreef ik](/2025/11/28/makelaar-of-maker.html) over de spanning tussen makelaar en maker. De nieuwe rijksbrede IT-sourcingstrategie stelt terecht de vraag over digitale autonomie en afhankelijkheid, maar biedt geen alternatief voor het probleem dat de overheid te weinig eigen engineeringcapaciteit heeft.

## Argument 3: AI kantelt koop-versus-bouw

Code wordt goedkoop. De marginale kosten van het schrijven van software dalen snel door AI-assisted coding. [In oktober](/2025/10/21/praten.html) bouwde ik een app door tegen mijn computer te praten. 38.000 regels code, geen Dart of Swift geleerd. [In december](/2025/12/27/ai-erodeert.html) schreef ik hoe AI het strategisch landschap erodeert: ruig terrein wordt begaanbaar, bergen worden heuvels.

Het gevolg voor de koop-versus-bouw-afweging ligt voor de hand. Grote SaaS-contracten en meerjarige maatwerk-trajecten worden relatief duurder ten opzichte van zelf bouwen. De productiviteitswinst van AI-tooling verschilt per context, maar zelfs conservatieve schattingen laten zien dat kleinere teams significant meer kunnen dan een paar jaar geleden[^aistudies]. Maar dat werkt alleen als die engineers een goed platform hebben om op te bouwen, en niet eerst weken bezig zijn met infrastructure setup en compliance-papierwerk.

[^aistudies]: Een [RCT bij Microsoft en Accenture](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf) (4.867 developers, Management Science 2025) vond 26% meer afgeronde taken, met 27-39% winst bij junior developers. [GitHub's eigen studie](https://arxiv.org/abs/2302.06590) vond 55% sneller op een geïsoleerde taak. De veelgehoorde claim van 4x of meer is niet empirisch onderbouwd.

## Argument 4: De multiplier

Bij [Spotify](/2021/12/01/joining-spotify.html) hoefden productteams zich niet bezig te houden met compute, databases, CI/CD, monitoring of security scanning. Dat was allemaal self-service beschikbaar via het platform. Intern onderzoek liet zien dat frequente gebruikers van het developer portal (Backstage) 2,3x actiever waren op GitHub, 2x zoveel code changes maakten in 17% minder cycle time, en 2x zo vaak deployden[^backstage]. Een correlatie, geen bewezen causaliteit, maar het verschil is opvallend genoeg om serieus te nemen.

[^backstage]: [Supercharged Developer Portals](https://engineering.atspotify.com/2024/04/supercharged-developer-portals/), Spotify Engineering, april 2024. De studie vergeleek frequente met infrequente Backstage-gebruikers. Er was geen controlegroep.

Voor de overheid betekent dit: in plaats van dat elke uitvoeringsorganisatie zelf een Kubernetes-cluster opzet en zelf security scanning inricht, bied je dat aan als self-service. Een team dat een nieuwe service moet bouwen klikt op "new project" en krijgt een repo met CI/CD, monitoring, security scanning, en deployment naar een compliant omgeving. In minuten. In plaats van [93 dagen](/2025/03/07/hosting-in-slow-motion.html).

## Argument 5: Bijzonder genoeg

Je kunt niet zomaar AWS of Azure kopen en klaar zijn. De overheid heeft specifieke eisen: BIO-compliance, AVG, data-soevereiniteit, DigiD-integratie, archivering en toegankelijkheid. Die eisen gelden voor elke uitvoeringsorganisatie, maar elke organisatie implementeert ze nu zelf, op een andere manier, met wisselende kwaliteit. Platform engineering pakt die gedeelde eisen en bouwt ze één keer goed in. Compliance als default.

## Argument 6: Standaarden in code

De overheid publiceert standaarden: API Design Rules, NORA, BIO, WCAG. Maar adoptie is traag en fragmentarisch. [Eerder schreef ik](/2026/02/20/skills.html) over skills die standaarden inbouwen in developer tools. Platform engineering doet hetzelfde op infrastructuurniveau: in plaats van een PDF die zegt "gebruik TLS 1.3" bouw je een platform waar TLS 1.3 de default is. In plaats van een memo over een nieuwe versie van een standaard, stuur je een automatische pull request naar alle repos.

## Argument 7: Talent

Het tekort aan IT-specialisten bij de overheid is nijpend[^whitelane]. Engineers kiezen voor werkgevers waar ze productief kunnen zijn, waar de tooling goed is, waar ze niet het grootste deel van hun [makers-tijd](/2025/03/13/verdwijnende-makers-tijd.html) bezig zijn met bureaucratie. Goed gereedschap trekt goed vakmanschap aan. Een overheid waar je in minuten een productieomgeving hebt is een aantrekkelijkere werkgever dan een overheid waar dat maanden duurt.

## Argument 8: Fragiele bouwblokken

[Haven](https://haven.commonground.nl/) standaardiseert Kubernetes-hosting. [FSC](https://fsc-standaard.nl/) regelt federatieve dienstverlening tussen organisaties. Er zijn initiatieven rond Common Ground, OpenZaak, [Open Notificaties](https://github.com/open-zaak/open-notificaties), [Open Formulieren](https://github.com/open-formulieren/open-forms), [NL Design System](https://nldesignsystem.nl/).

Maar eerlijk: deze bouwblokken zijn fragiel. Open Formulieren heeft meer dan 500 open issues en draait op een alpha-versie. Haven groeit, maar adoptie bij gemeenten gaat langzaam ondanks de VNG-standaardverklaring. De projecten worden onderhouden door kleine teams die kwetsbaar zijn voor uitval. En ze zijn onafhankelijk van elkaar gebouwd, met verschillende aannames over authenticatie, datamodellen en deployment. Ze passen nog niet op elkaar.

Dat is precies waarom platform engineering nodig is. Iemand moet deze bouwblokken versterken en op elkaar aansluiten. Er is geen developer portal, geen service catalog, geen golden paths. Die verbindende laag ontbreekt.

## Conclusie

De overheid is een softwarebedrijf. Ze moet zich ook zo organiseren. In het AI-tijdperk verschuift de business case van inkopen naar zelf bouwen, mits je een platform hebt om op te bouwen.

Maar een platform bouw je niet vanuit een community die op goodwill draait. Dat vereist mandaat en structurele financiering, met een organisatie die er verantwoordelijk voor is. DigiD werkt omdat Logius het beheert met dedicated budget en een helder mandaat. Een overheidsbreed developer platform heeft datzelfde nodig.

De bouwblokken liggen er. Ze moeten nu worden samengebracht en structureel geborgd. Platform engineering maakt het mogelijk om de output van engineers te vermenigvuldigen en compliance in te bouwen als default.

----