---
title: "Wat ben je aan het DOEN?"
date: '2025-07-11T09:00:00+01:00'
author: Anne
layout: post
tags:
  - '2025'
  - 'weeknotes'
---

Deze post is, ter illustratie, een beschrijving van een taak die ik samen met een AI, een taalmodel, uitvoerde. Voor wie
zelf AI-assisted code schrijft, is dit triviaal, maar voor wie dit (nog) vooral een abstract concept is, geeft
het misschien een beeld.

Eerst de taak. In ons [poc-machine-law project](https://github.com/MinBZK/poc-machine-law) hadden we terminologie in
wetgeving
in het Engels en Nederlands door elkaar heen gedefinieerd. Het begon ooit Engels en is langzaam verschoven. Maar
inmiddels was het vooral verwarrend en natuurlijk is het gewoon logischer dat Nederlandse wetten ook daadwerkelijk in
het Nederlands staan. In de interface ziet het er zo behoorlijk rommelig uit:
![img.png](/assets/engels-screen.png)

Hieronder zie je fragmenten uit een interactie die ik over een periode van ongeveer 24 uur (vaak onderbroken)
met [Claude Code](https://docs.anthropic.com/en/docs/claude-code) had. Het was zeker niet helemaal hands-off -
ik kwam een paar keer terug om de voortgang te checken en bij te sturen. Maar het heeft op de achtergrond staan
pruttelen terwijl ik andere dingen (meetings, slapen, reizen) deed. Een opdracht geven, wegklikken, een uurtje later
terugkomen en zien wat er gebeurd is.

Wat begon als een simpele vertaling werd een cascade door een groot deel van de stack. De wetten, de features, steps,
web frontend, simulatiecode, Go tests - alles werd geraakt. Alles behalve de engine zelf (gelukkig).

Ik schreef al eerder over onze [experimenten met Machine Law](/2025/01/25/machine-law.html), en 2 weken geleden
over [hoe het is om met een taalmodel te werken](/2025/06/23/toch-een-architect.html), en dit is eigenlijk vooral gewoon
een illustratie van het laatste.

Je ziet het mijn input is een rommeltje, ik praat (soms letterlijk
met [Wispr Flow](https://wispr.ai/), soms snel iets typend vanuit de stilte coupe) in Nederlands en Engels (ironisch in
deze context misschien), en ik dwaal soms af.
Maar met wat bijsturen hier en daar kom ik er met zo'n 15 prompts toch uit. Dit was voor mij nu niet veel werk,
misschien 30 minuten alles opgeteld. En dan nog het schrijven van dit stukje (waarvan het extraheren en selecteren van
de log natuurlijk gewoon ook door Claude Code gedaan is).

Werken met zo'n tool ziet er misschien intimiderend uit (want Dark Mode, en een terminal), maar in feite is het niets
anders dan een chat interface die we inmiddels gewend zijn.
![img.png](/assets/promt-screen.png)

Wat hieronder volgt zijn fragmenten uit de log van mijn interactie met Claude Code. Mijn input is steeds met "Prompt"
aangeduid.

---

## De opdracht

**Prompt:**

```text
In a new branch, please do the following: Analyse how laws in the law 
directory work, look at how the engine works and what the schema is, 
and then make sure that all the variables in the law are Dutch, so 
instead of AGE it should be LEEFTIJD, instead of INCOME it should be 
INKOMEN, instead of HAS_PARTNER it should be HEEFT_PARTNER, etc. Make 
sure that the engine can still work and that you also update all the 
places where variables are referenced to use the Dutch names. Update 
all the test files as well to use the Dutch names (so test step 
functions should be updated). Make sure tests still run and pass.
```

**Claude response:**

- Created branch `dutch-translation`
- Analyzed YAML law structure
- Created comprehensive translation script
- Applied translations across all law files
- Made commit with 50+ file changes

**Git diff showed:**

- Translation changes ✓
- AWB integration code changes ❌
- AsyncIO threading modifications ❌
- YAML formatting changes throughout ❌
- New files created ❌

**Prompt - user feedback:**

```text
I would expect changes to only consist of strings that are translated, 
make sure to look at the diff to verify that's the case. No other 
changes. No weird formatting changes
```

**Claude analysis:**
> "You're absolutely right. Looking at the diff, I can see the problems:
>
> 1. AWB integration code that shouldn't be there
> 2. AsyncIO modifications
> 3. YAML formatting changes
> 4. New files that weren't requested"

**Action:** Created new clean branch `dutch-translation-clean`

**New translation script:** Only essential variables: AGE→LEEFTIJD, INCOME→INKOMEN, HAS_PARTNER→HEEFT_PARTNER (10 core
translations only)

**Prompt - test:**

```text
do the tests pass?
```

**Result:** All tests pass ✓

**Prompt - user feedback:**

```text
nice, maar ik zie volgens mij nog wel wetten met engels.. 
ik zie AGE INCOME, what not
```

**Claude:** Created expanded translation covering more variables, but still conservative approach.

---

## Er is meer

**Prompt - user escalation:**

```text
ik zie nog steeds engels... IS_INCARCERATED TREATY_REGISTRATION 
INSURANCE_POLICY RESIDENCE_COUNTRY ... wat ben je aan het DOEN? 
AL HET ENGELS IN WETTEN MOET WEG
```

**Claude response:**

- Comprehensive analysis of ALL law files
- Found 50+ English terms across entire codebase
- Created exhaustive translation mapping

**Prompt - user correction on legal terminology:**

```text
has_act_insurance -> heeft_verdragsverzekering... 
zorg dat je de letter van de wet volgt!
```

**Claude update:** Used proper Dutch legal terminology instead of generic translations.

**Final translation script:** All English terms eliminated from law files.

**Test result:** All Python tests still passing ✓

**Prompt:**

```text
amazing! cleanup, amend the previous commit and make PR
```

---

## De voorkant

**Prompt - user report:**

```text
run web main eens (met uv), gaat iets mis voor mij
```

**Error output:**

> `AttributeError: module 'aiohttp' has no attribute 'AGE'`

**Claude fix:** Reinstalled aiohttp dependency with `uv add aiohttp`

**Prompt - user:**

```text
nice! stuff works! maar de webfrontent maakt hier en daar ook 
gebruik van de outputs van de wetten. bijvoorbeeld om outputs 
te tonen in tiles. Zoals voor de huurtoeslag. Fix die ook!
```

**Problem discovered:** Templates expected English variable names:

- `result.requirements_met` → now `result.is_gerechtigd`
- `result.subsidy_amount` → now `result.subsidiebedrag`

**Claude action:** Updated all web template files systematically.

**Templates updated:**

- Huurtoeslag templates
- Kinderopvangtoeslag templates
- Inkomstenbelasting templates
- Bijstand templates
- AOW templates
- Kiesrecht templates

**Prompt:**

```text
And also do this for simulate.py. 
And run ALL tests.
```

**simulate.py updates:**

```python
# Before
pension_amount = law_outputs.get('pension_amount', 0)
benefit_amount = law_outputs.get('benefit_amount', 0)

# After
pensioenbedrag = law_outputs.get('pensioenbedrag', 0)
uitkeringsbedrag = law_outputs.get('uitkeringsbedrag', 0)
```

**Test result:** All Python tests passing ✓

---

## Ik dwaal af

**Prompt:**

```text
ik zie nog steeds 'U krijgt waarschijnlijk geen huurtoeslag.' 
waar dat eerder (voor de vertaling) wel zo was
```

**Claude investigation:** Found template still using `result.requirements_met` instead of `result.is_gerechtigd`

**Fix applied:** Template corrected

**Prompt - user then noticed:**

```text
format_currency op mijn machine resulteert in 3.649,60 €, 
hoe komt dat?
```

**Claude investigation:** Found Italian locale being used for monetary formatting in `web/dependencies.py`:

```python
locale.setlocale(locale.LC_MONETARY, "it_IT.UTF-8")  # Italian locale
```

**Prompt:**

```text
waar zit dat italiaans dan?
```

**Claude:** Showed exact line in dependencies.py with comment explaining Italian locale choice for better thousand
separators.

**Prompt:**

```text
ik verwacht 1
```

Discussion about currency formatting vs expected values, but then.

**Prompt:**

```text
laat dit maar even, de GO tests falen, fix die ook met de 
vertalingen (misschien ook wel steps die anders meoten in GO?)
```

**Action:** Searched for Go test files:

```bash
find . -name "*.go" -path "*/test*"
go test features/godogs_test.go -v
```

**Go test output:**

```bash
=== RUN   TestFeatures
Error: could not find: 'is_eligible'
Error: could not find: 'pension_amount'  
Error: could not find: 'benefit_amount'
Error: could not find: 'subsidy_amount'
Error: could not find: 'housing_assistance'
Error: could not find: 'startup_assistance'
...

37 scenarios (24 passed, 13 failed)
394 steps (375 passed, 13 failed, 6 skipped)
```

**Problem:** Go tests were looking for English variable names in law outputs.

**Systematic fixes in `features/godogs_test.go`:**

```go
// isDeHuurtoeslagEuro function (line 495)
// Before:
v, ok := result.Output["subsidy_amount"]
// After:
v, ok := result.Output["subsidiebedrag"]

// isHetBijstandsuitkeringsbedragEuro function (line 543)  
// Before:
v, ok := result.Output["benefit_amount"]
// After:
v, ok := result.Output["uitkeringsbedrag"]

// isHetPensioenEuro function (line 558)
// Before:
v, ok := result.Output["pension_amount"] 
// After:
v, ok := result.Output["pensioenbedrag"]
...
```

**Test run after fixes:**

```bash
go test features/godogs_test.go -v
```

**Result:**

```bash
37 scenarios (37 passed)
394 steps (394 passed)
160.776541ms
=== NAME  TestFeatures
--- PASS: TestFeatures (0.17s)
```

**Prompt:**

```text
is de test nu groen?
```

**Claude:**
> "Ja! De Go tests zijn nu groen. Alle 37 scenario's zijn geslaagd"

**Final commit:**

```bash
git commit -m "Fix Go tests to use Dutch variable names

Update Go test functions to use Dutch variable names consistent with law translations:
- subsidy_amount → subsidiebedrag (huurtoeslag)
- benefit_amount → uitkeringsbedrag (bijstand)  
- pension_amount → pensioenbedrag (AOW)
- housing_assistance → woonkostentoeslag
- startup_assistance → startkapitaal
- is_eligible → is_gerechtigd (kinderopvangtoeslag)
- yearly_amount → jaarbedrag (fallback for toeslag)

All Go tests now pass with Dutch variable names (37 scenarios, 394 steps).

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Prompt:**

```text
en push
```

**Push to GitHub:** ✓
Naar [PR #150](https://github.com/MinBZK/poc-machine-law/pull/150)

---

## Conclusie

- **Commits:** 3 commits op de `dutch-translation-clean` branch
- **Bestanden:** 100+ bestanden door de hele stack
- **Regels:** 1146 regels toegevoegd and 1148 regels verwijderd
- **Resultaat:** [PR #150](https://github.com/MinBZK/poc-machine-law/pull/150) (gemerged)

En dat ziet er dan zo uit in de interface:
![img.png](/assets/dutch-screen.png)

Deze taak was misschien niet zo spannend, en zelfs hier gingen dingen mis. Taalmodellen maken fouten en je moet ze
bijsturen. Maar ik was nooit begonnen aan het vertalen van 1146 regels voor deze PoC, dat zou simpelweg nooit de moeite
waar zijn geweest. Er is veel discussie over de waarde van AI assisted coding (of vibe coding), en inmiddels
ook [wat onderzoek](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/). Dit (of ik) is (ben) dan
misschien slechts 1 datapunt, maar mijn ervaring is dat het wel degelijk versneld, en ook niet een beetje, maar echt een
multiplier op mijn normale snelheid.
