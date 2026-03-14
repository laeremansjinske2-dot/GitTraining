# Les 5: Pull Requests (PR's)

## Wat is een Pull Request?

Een **Pull Request** (PR) is een manier om te zeggen: *"Ik heb wijzigingen gemaakt, wil je ze bekijken en mergen?"*

Het is de standaard manier om in teams samen te werken. In plaats van direct in `main` te pushen, maak je een PR zodat iemand je code kan **reviewen** voor het gemerged wordt.

## Waarom Pull Requests?

- **Code review**: iemand anders bekijkt je code voor fouten
- **Discussie**: je kan commentaar geven op specifieke regels
- **Kwaliteit**: voorkomt dat bugs in de hoofdcode terechtkomen
- **Documentatie**: je ziet precies wat er veranderd is en waarom

## Hoe maak je een Pull Request?

### Stap 1: Maak je wijzigingen in een branch

```bash
git checkout -b mijn-feature
# ... maak wijzigingen ...
git add .
git commit -m "voeg nieuwe feature toe"
git push -u origin mijn-feature
```

### Stap 2: Maak een PR op GitHub

1. Ga naar je repository op GitHub
2. Je ziet een melding: *"mijn-feature had recent pushes"*
3. Klik op **"Compare & pull request"**
4. Vul in:
   - **Titel**: korte beschrijving
   - **Beschrijving**: wat heb je veranderd en waarom?
5. Klik op **"Create pull request"**

### Stap 3: Review & Merge

1. Andere teamleden bekijken je code
2. Ze kunnen **commentaar** geven of **wijzigingen** vragen
3. Als alles goedgekeurd is, klik je op **"Merge pull request"**

## PR vanuit een Fork

Als je aan iemand anders' project werkt (via een fork):

```
Jouw fork (branch: feature)  →  PR  →  Originele repo (main)
```

Dit is hoe open source werkt! Je forkt, maakt wijzigingen, en stuurt een PR naar het origineel.

## Een PR reviewen (als eigenaar)

Als iemand een PR naar jouw repo stuurt:

1. Ga naar het **"Pull requests"** tabblad
2. Open de PR
3. Bekijk de **"Files changed"** tab
4. Laat commentaar achter of keur goed
5. Klik **"Merge pull request"** als het er goed uitziet

## Tips voor goede PR's

- Hou PR's **klein** - makkelijker te reviewen
- Schrijf een **duidelijke beschrijving**
- Voeg **screenshots** toe als het visuele wijzigingen zijn
- Reageer op **feedback** van reviewers

---

**Oefening:** [Pull Request oefening](../oefeningen/04-pull-request.md)

**Volgende les:** [Merge Conflicts](06-merge-conflicts.md)
