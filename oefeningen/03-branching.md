# Oefening 3: Branching & Merging

## Doel
Een feature branch maken, wijzigingen maken, en terug mergen naar main.

## Stappen

### 1. Maak een nieuwe branch
```bash
git checkout -b feature/mijn-naam
```
> Vervang `mijn-naam` door je eigen naam!

### 2. Bekijk je branches
```bash
git branch
```
Je zou `main` en `feature/mijn-naam` moeten zien, met een `*` bij je actieve branch.

### 3. Maak een wijziging
Maak een nieuw bestand `python/begroeting.py`:

```python
def begroet(naam):
    return f"Hallo {naam}! Welkom bij de Git training!"

print(begroet("JOUW NAAM"))
```

### 4. Commit je wijziging
```bash
git add python/begroeting.py
git commit -m "voeg persoonlijke begroeting toe"
```

### 5. Push je branch naar GitHub
```bash
git push -u origin feature/mijn-naam
```

### 6. Ga terug naar main
```bash
git checkout main
```

Merk op: `python/begroeting.py` bestaat **niet** op main! Het zit alleen in je feature branch.

### 7. Merge je branch
```bash
git merge feature/mijn-naam
```

Nu bestaat het bestand ook op main!

### 8. Verwijder de branch (optioneel)
```bash
git branch -d feature/mijn-naam
```

## Checklist
- [ ] Nieuwe branch aangemaakt
- [ ] Wijziging gemaakt in de branch
- [ ] Branch gepusht naar GitHub
- [ ] Gecontroleerd dat de wijziging niet op main staat
- [ ] Branch gemerged naar main
- [ ] (Bonus) Branch verwijderd na merge

**Klaar? Ga door naar [oefening 4](04-pull-request.md)!**
