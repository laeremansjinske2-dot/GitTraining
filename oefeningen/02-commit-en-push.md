# Oefening 2: Commit & Push

## Doel
Een bestand aanpassen, committen en pushen naar GitHub.

## Stappen

### 1. Pas de rekenmachine aan
Open `python/rekenmachine.py` en voeg een nieuwe functie toe, bijvoorbeeld:

```python
def machtsverheffen(a, b):
    return a ** b
```

Vergeet niet de functie ook aan te roepen met een `print()`! Bijvoorbeeld:

```python
print("2 ** 3 =", machtsverheffen(2, 3))
```

### 2. Test je code
```bash
python python/rekenmachine.py
```

### 3. Bekijk de status
```bash
git status
```

Je zou moeten zien dat `python/rekenmachine.py` gewijzigd is.

### 4. Bekijk je wijzigingen
```bash
git diff
```

### 5. Stage je wijzigingen
```bash
git add python/rekenmachine.py
```

### 6. Commit
```bash
git commit -m "voeg machtsverheffen functie toe aan rekenmachine"
```

### 7. Push naar GitHub
```bash
git push
```

### 8. Controleer op GitHub
Ga naar je fork op GitHub en kijk of je wijziging zichtbaar is!

## Bonus
- Voeg nog een functie toe (bv. `modulo`, `wortel`, `gemiddelde`)
- Maak voor elke functie een aparte commit met een duidelijke boodschap

## Checklist
- [ ] Nieuwe functie toegevoegd
- [ ] Code getest
- [ ] Wijzigingen gestaged met `git add`
- [ ] Gecommit met een duidelijke boodschap
- [ ] Gepusht naar GitHub
- [ ] Wijziging zichtbaar op GitHub

**Iets niet duidelijk? Ga terug naar naar [de uitleg](/lessen/03-commit-en-push.md)!**

**Klaar? Ga door naar [oefening 3](03-branching.md)!**
