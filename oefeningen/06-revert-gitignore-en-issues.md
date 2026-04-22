# Oefening 6: Revert, .gitignore & GitHub Issues (EXTRA zie les 8)

## Doel
In 1 korte oefening leer je:
- een foute commit terugdraaien met `git revert`
- een lokaal bestand correct negeren met `.gitignore`
- een GitHub Issue aanmaken voor een verbeteridee

## Deel A - Revert demo

### 1. Maak een kleine testwijziging
Voeg in `python/kleuren.py` onderaan tijdelijk een print toe:

```python
print("testregel voor revert")
```

Commit en push:

```bash
git add python/kleuren.py
git commit -m "voeg tijdelijke testregel toe"
git push
```

### 2. Draai die commit terug
Zoek je laatste commit en revert die:

```bash
git log --oneline -n 3
git revert HEAD
git push
```

Controleer dat de testregel weer weg is.

## Deel B - .gitignore demo

### 3. Maak een lokaal notitiebestand
Maak een bestand `NOTITIES-LOKAAL.md` met eender welke tekst.

### 4. Voeg ignore-regel toe
Open `.gitignore` en voeg onderaan toe:

```gitignore
NOTITIES-LOKAAL.md
```

### 5. Check of het genegeerd wordt

```bash
git status --short
git check-ignore -v NOTITIES-LOKAAL.md
```

Je zou moeten zien dat het bestand genegeerd wordt.

## Deel C - GitHub Issue

### 6. Maak een issue in je fork
Maak in GitHub een issue met:
- **Titel:** `Voeg korte les over git revert toe`
- **Beschrijving:** waarom dit nuttig is voor beginners
- **Checklist:** 2-3 kleine actiepunten

## Checklist
- [ ] Tijdelijke commit gemaakt en met revert teruggedraaid
- [ ] `NOTITIES-LOKAAL.md` toegevoegd aan `.gitignore`
- [ ] Gecontroleerd dat het bestand genegeerd wordt
- [ ] 1 GitHub Issue aangemaakt

**Klaar? Nice. Dit zijn exact de kleine workflows die je in echte projecten vaak nodig hebt.**
