# Oefening 5: Merge Conflict

## Doel
Een merge conflict veroorzaken, begrijpen en oplossen.

## Stappen

### 1. Zorg dat je op main staat
```bash
git checkout main
```

### 2. Pas kleuren.py aan op main
Open `python/kleuren.py` en verander de `favoriete_kleur` functie:

```python
def favoriete_kleur():
    return "blauw"    # Verander "groen" naar "blauw"
```

Commit deze wijziging:
```bash
git add python/kleuren.py
git commit -m "verander favoriete kleur naar blauw"
```

### 3. Maak een nieuwe branch VANUIT een eerdere commit
```bash
# Ga 1 commit terug en maak daar een branch
git checkout HEAD~1
git checkout -b feature/andere-kleur
```

### 4. Pas dezelfde regel aan in de branch
Open `python/kleuren.py` en verander de `favoriete_kleur` functie:

```python
def favoriete_kleur():
    return "rood"    # Verander naar "rood"
```

Commit:
```bash
git add python/kleuren.py
git commit -m "verander favoriete kleur naar rood"
```

### 5. Probeer te mergen
```bash
git checkout main
git merge feature/andere-kleur
```

**CONFLICT!** Git kan niet kiezen tussen "blauw" en "rood".

### 6. Bekijk het conflict
Open `python/kleuren.py`. Je ziet zoiets:

```python
def favoriete_kleur():
<<<<<<< HEAD
    return "blauw"
=======
    return "rood"
>>>>>>> feature/andere-kleur
```

### 7. Los het conflict op
Kies welke kleur je wilt (of combineer ze!). Verwijder de conflict markers:

```python
def favoriete_kleur():
    return "rood"    # Of "blauw", of iets anders!
```

### 8. Commit de oplossing
```bash
git add python/kleuren.py
git commit -m "los merge conflict op - kies rood als favoriete kleur"
```

## Checklist
- [ ] Wijziging gemaakt op main
- [ ] Zelfde regel gewijzigd in een andere branch
- [ ] Merge conflict veroorzaakt
- [ ] Conflict markers herkend (`<<<<<<<`, `=======`, `>>>>>>>`)
- [ ] Conflict handmatig opgelost
- [ ] Oplossing gecommit

**Iets niet duidelijk? Ga terug naar naar [de uitleg](/lessen/06-merge-conflicts.md)!**

**Klaar? Gefeliciteerd! Je kan nu merge conflicts oplossen én je hebt alle oefeningen van vandaag gemaakt!**
