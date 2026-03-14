# Les 3: Wijzigingen maken - Stage, Commit & Push

## De drie zones van Git

Git werkt met drie "zones" waar je bestanden doorheen gaan:

```
Working Directory    →    Staging Area    →    Repository
(je bestanden)            (klaar om te        (opgeslagen
                           committen)          in git)

   bewerken          git add            git commit
```

### 1. Working Directory
Dit zijn je bestanden zoals je ze ziet in je editor. Als je iets wijzigt, weet Git dat er iets veranderd is.

### 2. Staging Area
Hier zet je de bestanden die je wilt opslaan in je volgende commit. Niet elke wijziging hoeft in dezelfde commit!

### 3. Repository
Na een commit zijn je wijzigingen veilig opgeslagen in de Git geschiedenis.

## Stap voor stap

### Status bekijken

```bash
git status
```

Dit toont welke bestanden gewijzigd, nieuw, of gestaged zijn.

### Bestanden stagen (klaarzetten)

```bash
# Een specifiek bestand stagen
git add bestandsnaam.py

# Alle gewijzigde bestanden stagen
git add .
```

### Committen (opslaan)

```bash
git commit -m "Beschrijving van je wijziging"
```

> **Tip:** Schrijf duidelijke commit messages! "fix" of "update" zegt niks. Beter: "voeg rekenmachine functies toe" of "fix bug in quiz score berekening".

### Pushen (uploaden naar GitHub)

```bash
git push
```

Dit stuurt je commits naar GitHub zodat ze online staan.

## De volledige flow

```bash
# 1. Bekijk wat er veranderd is
git status

# 2. Stage je wijzigingen
git add .

# 3. Commit met een duidelijke boodschap
git commit -m "voeg nieuwe functie toe"

# 4. Push naar GitHub
git push
```

## Commando overzicht

| Commando | Wat doet het? |
|----------|---------------|
| `git status` | Bekijk de status van je bestanden |
| `git add <bestand>` | Stage een bestand |
| `git add .` | Stage alle wijzigingen |
| `git commit -m "msg"` | Sla je wijzigingen op met een bericht |
| `git push` | Upload je commits naar GitHub |
| `git log --oneline` | Bekijk je commit geschiedenis |
| `git diff` | Bekijk de exacte wijzigingen |

---

**Oefening:** [Commit & Push oefening](../oefeningen/02-commit-en-push.md)

**Volgende les:** [Branching & Merging](04-branching.md)
