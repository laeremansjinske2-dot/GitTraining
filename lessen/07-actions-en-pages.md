# Les 7: GitHub Actions & GitHub Pages

## GitHub Actions

### Wat is het?

**GitHub Actions** is een systeem dat automatisch taken uitvoert wanneer er iets gebeurt in je repository. Dit heet **CI/CD** (Continuous Integration / Continuous Deployment).

### Voorbeelden van wat Actions kan doen

- Automatisch **testen** draaien bij elke push
- Je code **controleren** op fouten
- Een **website deployen** wanneer je naar main pusht
- Een **app builden** en publiceren

### Hoe werkt het?

Actions worden geconfigureerd met **YAML bestanden** in de `.github/workflows/` map.

```yaml
name: Naam van de workflow

on:                    # Wanneer moet het draaien?
  push:
    branches: [main]   # Bij elke push naar main

jobs:
  build:               # Naam van de job
    runs-on: ubuntu-latest   # Op welk systeem?
    steps:
      - name: Stap 1
        run: echo "Hallo wereld!"
```

### Belangrijke concepten

| Concept | Uitleg |
|---------|--------|
| **Workflow** | Het volledige automatiseringsproces |
| **Trigger** (`on`) | Wat start de workflow (push, PR, schedule...) |
| **Job** | Een set stappen die samen draaien |
| **Step** | Een individuele actie binnen een job |
| **Runner** | De (virtuele) computer waarop het draait |

## GitHub Pages

### Wat is het?

**GitHub Pages** is een gratis service van GitHub waarmee je een **statische website** kan hosten, rechtstreeks vanuit je repository.

### Hoe werkt het?

1. Je zet HTML/CSS/JS bestanden in een `docs/` map (of een aparte branch)
2. GitHub Actions bouwt en publiceert de site automatisch
3. Je site is beschikbaar op `https://username.github.io/repo-naam/`

### Live Demo

Deze repository heeft een website in de `docs/` map! Na het inschakelen van GitHub Pages is de site te bereiken op:

```
https://JOUW-USERNAME.github.io/GitTraining/
```

### GitHub Pages inschakelen

1. Ga naar je repository **Settings**
2. Klik op **Pages** in het linkermenu
3. Onder **Source**, kies **GitHub Actions**
4. De workflow in `.github/workflows/pages.yml` doet de rest!

## Samenvatting

```
Push naar main → GitHub Actions start → Website wordt gedeployd → Live op GitHub Pages!
```

Dit is een mini-versie van hoe echte softwarebedrijven werken: code pushen, automatisch testen, automatisch deployen.

---

**Nog tijd over? Ga door naar [Les 8: Revert, .gitignore & GitHub Issues](08-revert-gitignore-en-issues.md). Bekijk ook de [cheatsheet](../cheatsheet.md) voor een handig overzicht van alle commando's.**
