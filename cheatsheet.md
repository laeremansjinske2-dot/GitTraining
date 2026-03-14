# Git Cheatsheet

## Setup & Config

| Commando | Beschrijving |
|----------|-------------|
| `git config --global user.name "Naam"` | Stel je naam in |
| `git config --global user.email "email"` | Stel je email in |
| `git init` | Maak een nieuwe Git repo |
| `git clone <url>` | Clone een repo van GitHub |

## Dagelijks gebruik

| Commando | Beschrijving |
|----------|-------------|
| `git status` | Bekijk de status van je bestanden |
| `git add <bestand>` | Stage een bestand |
| `git add .` | Stage alle wijzigingen |
| `git commit -m "bericht"` | Commit met een boodschap |
| `git push` | Upload commits naar GitHub |
| `git pull` | Download wijzigingen van GitHub |

## Branches

| Commando | Beschrijving |
|----------|-------------|
| `git branch` | Bekijk alle branches |
| `git checkout -b <naam>` | Maak en switch naar nieuwe branch |
| `git checkout <naam>` | Switch naar een branch |
| `git merge <naam>` | Merge een branch in je huidige branch |
| `git branch -d <naam>` | Verwijder een branch |

## Informatie

| Commando | Beschrijving |
|----------|-------------|
| `git log --oneline` | Bekijk commit geschiedenis (kort) |
| `git log` | Bekijk commit geschiedenis (uitgebreid) |
| `git diff` | Bekijk wijzigingen (unstaged) |
| `git diff --staged` | Bekijk wijzigingen (staged) |
| `git remote -v` | Bekijk remote verbindingen |

## Ongedaan maken

| Commando | Beschrijving |
|----------|-------------|
| `git checkout -- <bestand>` | Wijzigingen ongedaan maken (voor staging) |
| `git reset HEAD <bestand>` | Unstage een bestand |
| `git reset --soft HEAD~1` | Laatste commit ongedaan maken (wijzigingen behouden) |

## Merge Conflicts

```
<<<<<<< HEAD        ← Jouw versie
jouw code hier
=======             ← Scheiding
andere code hier
>>>>>>> branch      ← Inkomende versie
```

**Oplossen:** kies een versie, verwijder de markers, stage en commit.

## Tips

- Commit vaak, push regelmatig
- Schrijf duidelijke commit messages
- Pull voor je begint te werken
- Gebruik branches voor nieuwe features
- Hou PR's klein en overzichtelijk
