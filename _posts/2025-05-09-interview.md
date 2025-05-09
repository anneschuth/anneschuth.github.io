---
title: "Interview"
date: '2025-05-09T09:00:00+01:00'
author: Claude
layout: post
tags:
  - '2025'
  - 'weeknotes'
---

*Het was een wat gekke week, met twee vrije dagen doordat mijn kinderen deze week ook vakantie hadden.
Mede daarom dit experiment: een interview afgenomen door een LLM (Claude 3.7 met extende thinking). Ik was benieuwd wat
voor vragen zo'n model zou stellen en of het me aan het denken zou zetten over mijn werk.*

*Dit was mijn prompt aan Claude:*

> Ik ben Anne Schuth, auteur van een blog op https://anneschuth.nl (laatste blog posts bijgevoegd, maar zoek ook
> informatie op!) waar ik weeknotes schrijf over mijn werk bij Bureau Architectuur, een team binnen de Nederlandse
> overheid dat zich bezighoudt met digitale transformatie.
>
> Ik heb een achtergrond in Search en heb eerder gewerkt bij
> bedrijven als Blendle, Google, DPG Media, en Spotify. In mijn blog reflecteer ik op de uitdagingen van het bouwen van
> bruggen tussen beleid en techniek, de spanning tussen architectuur en daadwerkelijk bouwen, en de culturele
> verschillen
> tussen tech-bedrijven en de overheid.
>
> Kun je me interviewen met kritische, diepgaande vragen die me dwingen tot eerlijke
> reflectie over de structurele obstakels bij digitale transformatie van de overheid? Vermijd vragen die
> zelfverheerlijkend overkomen. Focus op spanningen en paradoxen in mijn werk, de praktische uitdagingen van verandering
> binnen bureaucratische systemen, en de realistische verwachtingen voor digitale overheid in Nederland.
>
> In het Nederlands. Stel vragen 1 voor 1 en maak aan het einde een blog in markdown voor Jekyll. De blog moet interview
> style zijn opgemaakt.

*Hieronder het resultaat van dit experiment, zonder bewerkingen. De vragen dus van Claude, de antwoorden van mij (Claude
heeft wel wat typos en hoofdletter gebruik gefixt).*

Anne Schuth werkt sinds 2023 bij Bureau Architectuur, een team binnen de Nederlandse overheid dat zich bezighoudt met
digitale transformatie. Met een achtergrond in zoekmachines en een carrière bij bedrijven als Spotify, Google en DPG
Media brengt hij een uniek perspectief mee. In dit interview reflecteert Anne openhartig op de uitdagingen, paradoxen en
mogelijkheden van digitale verandering binnen de overheid.

**Je schreef in "Hosting in slow motion" over het 93+ dagen durende proces om een eenvoudige Kubernetes-omgeving op te
zetten bij de overheid. Wat zegt dit over de fundamentele uitdagingen van digitale soevereiniteit in Nederland?**

"De overheid kent gewoon echt een complexiteit van een andere orde dan het bedrijfsleven. Als was het maar omdat
*niemand* mandaat (ja, je gaat vanzelf meedoen aan ambtenaren taal) heeft om iets te veranderen, of anders in te
richten. Daarnaast is het, noodzakelijkerwijs, zo dat de overheid zo ingericht is dat het aansluit bij de wensen van de
politiek. Of beter: de ambtenarij richt zich zo in dat het de politiek zo goed mogelijk bedient (of cynischer: dat het
zo min mogelijk gedoe krijgt). Dit zorgt ervoor, anders dan in het bedrijfsleven, dat het niet per se de inhoudelijk
sterksten (alhoewel die er ook zijn!) zijn die het voor het zeggen hebben."

**In je blog "Heimwee" vergelijk je je tijd bij Spotify met de huidige situatie bij de overheid. Is de "platform
engineering organisatie" die je beschrijft überhaupt realistisch binnen de overheidscultuur, of vereist dit een
fundamentele herstructurering?**

"Ik denk zeker dat dat realistisch is. Ik denk dat er helemaal niet zo heel erg veel voor nodig is om dat voor elkaar te
krijgen! Met een klein team dat daar op focust (wat mij betreft het verlengde van developer.overheid.nl) komen we echt
al een heel eind."

**Waar lopen de huidige initiatieven dan volgens jou vast?**

"Anderen, met mandaat (tja), moeten dat met me eens zijn en er opdracht toe geven."

**In je blogs schrijf je over de "schijnbare tegenstelling" tussen architecten en engineers binnen de overheid. Hoe
beïnvloedt deze gescheiden benadering concreet de kwaliteit van digitale overheidsdiensten voor burgers?**

"Dit is echt heel erg sterk aanwezig. Architecten waren er niet bij bijvoorbeeld Spotify. We hadden daar wel Staff
engineers die een deel van het architectenwerk op zich namen, maar staff engineers schrijven ook code. Hun scope is dan
of heel groot (over meerdere teams heen) of ze werken aan een heel complex stuk code met grote impact. Architectuur
beslissingen bij Spotify worden hierdoor genomen door mensen die diep in de materie zitten, niet losgezongen van de
werkelijkheid. Hoe anders is dat bij de overheid. Architecten zijn hier vaak niet eens technisch, kunnen niet
programmeren, en zijn er ook nog eens heel erg sterk van overtuigd dat dat geen enkel probleem is. Het produceren van
plaatjes is tot een kunst verheven, dat dat los staat van de werkelijkheid lijkt niets uit te maken."

**Je schrijft vaak over de kloof tussen de 'manager's schedule' en de 'maker's schedule' binnen de overheid. Hoe
manifesteert deze spanning zich in de producten die jullie opleveren, en heb je voorbeelden van projecten die mislukten
specifiek door deze cultuurbotsing?**

"Dit is een hardnekkig probleem (overigens niet alleen bij de overheid, ook in het bedrijfsleven). Het blijft lastig om
de brug te zijn tussen beleidsmakers (product management bij tech bedrijven) en engineering. Beleidsmakers / product
managers besteden van nature een significant deel van hun tijd in overleggen, ze zijn constant aan het context-switchen.
Terwijl engineers ruimte en tijd (dagdelen!) moeten hebben om effectief te zijn.

Toch moet iemand die brug zijn. Ik ben dat vaak, en merk hoe moeilijk het is om tussen meetings door, of na een paar
dagen vol meetings, weer de diepte in te duiken. Ergens zou ik het liefst met een koptelefoon (en oogkleppen?) diep de
code in duiken. Maar ergens ook niet natuurlijk: code schrijf je niet in isolatie, het dient een doel, er is afstemming
nodig."

**Je hebt het over de botsende werkstijlen, maar heb je concrete voorbeelden van hoe dit negatieve gevolgen heeft voor
projecten?**

"Ah, ik gaf inderdaad geen antwoord! Ik denk dat we constant kansen missen. Dat wat we vinden/tegenkomen tijdens het
bouwen van oplossingen (bijvoorbeeld in de PoC Machine Law nu) is denk ik vaak waardevolle input voor beleidsmakers.
Maar dat aankaarten bij de juiste persoon/organisatie zou veel tijd en energie van de maker vragen. Daardoor gebeurt het
niet (niet altijd), daar zit een enorme opportunity cost."

**Je experimenteert met "Machine Law" om wetgeving machine-leesbaar te maken. Is er vanuit juristen en beleidsmakers
weerstand tegen dit idee, en hoe ga je om met de terechte zorg dat wetgeving contextgevoelig is en soms opzettelijk
ambigu?**

"Vooralsnog valt die weerstand heel erg mee! Mensen zijn vooral geïnteresseerd, willen meer weten, zien kansen. En
natuurlijk zijn er ook bezwaren en obstakels, maar vooralsnog geen fundamentele. Bijvoorbeeld rondom open normen: ja,
dat is soms (vaak?) opzettelijk zo, en daar moeten we niet aan tornen. Eens. Ik denk ook niet dat we dat voorstellen.
Nog sterker, met Machine Law maken we expliciet waar de norm open is, en waar niet."

**Wat was de meest verrassende reactie die je kreeg van een jurist of beleidsmaker toen je het concept voor het eerst
presenteerde?**

"Ik had eigenlijk meer weerstand verwacht. Dat die er niet zo heel erg veel is verraste mij (en betekent of dat we niets
nieuws doen, of dat het gewoon een logische volgende stap is, denk ik)."

**Kun je een specifiek voorbeeld delen van een positieve reactie die je niet had verwacht?**

"Niet echt"

**In "Email is dood, lang leve het team" beschrijf je de uitdagingen bij het bouwen van een teamcultuur binnen de
overheid. Welke concrete veranderingen zie je bij collega's die meegaan in deze nieuwe manier van werken?**

"Ja, dit blijft lastig. En dat ligt niet aan het team, ik zie mensen het echt proberen en doen. Maar de omgeving is zo
anders dat het niet goed past. Alles en iedereen mailt constant met elkaar. Als team is het niet makkelijk om dat anders
te doen. Het heeft zelfs het risico dat communicatie nog verder versnipperd raakt. We hebben echt breder een andere
manier van werken nodig."

**Heb je wel concrete veranderingen gezien in de manier waarop mensen binnen het team samenwerken, ondanks deze externe
druk?**

"Zeker, het meest concrete is onze dagelijks standup! Die blijkt echt nuttig. Het lukt meestal om ons tot 15min te
beperken, en vaak genoeg komen er (soms onverwachte) verbanden tussen werk dat we doen naar voren."

**Je schreef dat je organisatie is "ingericht om de politiek te bedienen". Tegelijkertijd probeer je lange-termijn
veranderingen door te voeren. Hoe ga je om met de spanning tussen politieke tijdlijnen (vaak 4 jaar) en de tijd die
nodig is voor fundamentele digitale transformatie?**

"Goede vraag. Dit weet ik eerlijk gezegd niet. Ik werk hier nu een jaar en 10 maanden, heb 1 kabinetswissel meegemaakt.
Geen idee hoe de langere termijn geborgd moet worden in dit systeem."

**In je blogs bekritiseer je soms impliciet de bestaande structuren. Heb je als een relatieve buitenstaander vrijheid om
te experimenteren, of voel je soms druk om te conformeren aan de bestaande systemen en cultuur?**

"Beide. Er is zeker ruimte te experimenteren! De weeknotes die ik schrijf zijn daar een onderdeel van. De PoC Machine
Law zelf is natuurlijk een groot experiment. En ook de samenwerkvormen zijn dat. Tegelijkertijd word ik regelmatig met
de neus op de feiten gedrukt (door de feiten zelf, of door mensen die ze me voorhouden) dat dingen langer duren dan ik
zou willen, dat er belangen zijn die ik niet zie, dat er (oude) structuren zijn die weerbarstig zijn."

**Hoe ga je om met die momenten van frustratie wanneer je tegen de grenzen van het systeem aanloopt?**

"Ik blijf dit lastig vinden. Minder dan eerder treed ik op de voorgrond. Ik merk dat het me teveel frustreert en dat ik
het persoonlijk opvat/maak (wat onhandig is, natuurlijk). Eerdere bedrijven waar ik werkte waren niet vrij van interne
politiek (hi DPG Media), en ook daar had ik het soms zwaar, maar daar kreeg ik het toch voor elkaar om voortgang te
boeken. Hier voelt dat vaak onmogelijk voor me. Gelukkig zijn er mensen om me heen met meer geduld en een dikkere
huid."

**Je vergelijkt in je blogs vaak je ervaringen bij Spotify met die bij de overheid. Wat is iets dat de overheid beter
doet dan Spotify, dat misschien niet zo vaak wordt benoemd?**

"Nou ja. Uiteindelijk maakt Spotify een muziek appje. Niet zo boeiend, in the grand scheme of things. Terwijl de
overheid de samenleving organiseert: nogal belangrijk. Dus de vergelijking gaat totaal mank. We zijn hier met iets heel
erg wezenlijks bezig. Terwijl, als Spotify er niet zou zijn het nauwelijks iets uit zou maken. (Kleine kanttekening is
dat Spotify wel degelijk instrumenteel was in mensen weer laten betalen voor muziek, maar inmiddels is dat weer de
norm)."

**Geeft dit je, ondanks alle frustraties met bureaucratie en trage processen, ook een diepere motivatie of voldoening in
je huidige werk die je bij Spotify niet ervoer?**

"Ja, zeker, heel erg. Dit is de reden dat ik blijf doen wat ik doe."

**In "Terug op oude grond" beschrijf je je bezoek aan het ICAI OpenGov Lab en hoe belangrijk het is dat de overheid niet
in een bubbel werkt. Hoe zou de uitwisseling tussen wetenschap en overheid structureel verbeterd kunnen worden?**

"Dit is een hele goede vraag. Ik blijf me verbazen over het feit dat we de wetenschap als overheid nauwelijks gebruiken
als bron van kennis. We kijken liever naar bijvoorbeeld bedrijven als Gartner (don't get me started!) voor kennis.
Terwijl we als samenleving bedacht hebben dat we kennisinstellingen willen hebben, en die ook financieren. Die
samenwerking zou wat mij betreft vanzelfsprekend moeten zijn."

**Wat denk je dat die voorkeur voor commerciële adviesbureaus boven academische instellingen veroorzaakt?**

"Het heeft vrees ik allemaal te maken met indekken en bereidheid om risico's te nemen. Een bestuurder zegt graag dat
iets
op advies van Gartner/Capgemini/KPMG/... gebeurt, liever dan gebaseerd op onderzoek van een (relatief) onbekende
hoogleraar."

**Zou het helpen als academische instellingen anders zouden communiceren, of denk je dat er structurele veranderingen
nodig zijn in hoe bestuurlijke verantwoordelijkheid wordt beoordeeld?**

"Ik weet het eerlijk gezegd niet. Ik denk dat bereidheid om risico's te nemen belangrijk is. Maar hoe je daar komt, weet
ik niet."

**In je blog "Demo's spreken luider" heb je het over de kracht van prototypes versus beleidsdocumenten. Wat was een
sleutelmoment waarbij je zag dat een werkend prototype een vastgelopen discussie weer in beweging bracht?**

"Dit gebeurt echt vaak! We zijn met een soort road show bezig met onze PoC Machine Law Demo. We gaan langs bij allerlei
wetenschappers, bestuurders, beleidsmakers, juristen, etc. En steeds is men licht sceptisch als we starten (we beginnen
met een gesprek, met een paar introductie slides). Maar zodra we de demo starten slaat het om, gaan mensen recht op
zitten, worden de vragen en discussie inhoudelijker."

**Hebben jullie uit deze ervaringen ook geleerd hoe je demo's effectiever kunt maken?**

"Er zit inmiddels een vaste volgorde en cadans in de demo, die is gaandeweg ontstaan, en bouwt aspecten van het idee
achter machine law 1 voor 1 op."

**Na bijna twee jaar bij de overheid, wat zie je als je belangrijkste bijdrage tot nu toe, en wat hoop je de komende
jaren te bereiken?**

"Ik denk dat mijn belangrijkste bijdrage op een paar assen zit: in de manier van werken die we rondom demos/pocs
opgestart hebben binnen een beleidsafdeling. In het werken als teams vanuit het Rijks ICT Gilde (waar ik dienst ben), en
de PoC Machine law zelf, waar ik een inhoudelijke bijdrage lever."

**Als je zou moeten kiezen, welke van deze bijdragen zie je als meest betekenisvol, en wat hoop je nog te bereiken in de
komende jaren?**

"Ik zou heel graag die machine law veel verder brengen. Dat is een project dat een lange adem (20, misschien wel 30
jaar) nodig heeft, maar is denk ik de moeite waard."

Dit interview geeft een inkijkje in de dagelijkse realiteit van digitale transformatie binnen de overheid. Hoewel de
uitdagingen aanzienlijk zijn, laat het zien dat er ook ruimte is voor innovatie en vooruitgang - zolang we bereid zijn
om de lange adem te hebben die nodig is voor echte verandering.
