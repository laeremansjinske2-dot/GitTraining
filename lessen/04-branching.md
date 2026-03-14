# Les 4: Branching & Merging

## Wat is een Branch?

Een **branch** is een aparte "tak" van je project. Je kan er in werken zonder de hoofdversie (`main`) te beinvloeden.

```
main:        A --- B --- C
                         \
feature:                  D --- E
```

Dit is superhandig wanneer je:
- Een **nieuwe feature** wilt bouwen
- Een **bug** wilt fixen
- Wilt **experimenteren** zonder risico

## Branch maken en gebruiken

### Nieuwe branch maken en ernaar switchen

```bash
git checkout -b mijn-feature
```

Dit doet twee dingen: maakt de branch **en** switcht ernaar.

### Alle branches bekijken

```bash
git branch
```

De actieve branch heeft een `*` ervoor.

### Tussen branches switchen

```bash
git checkout main          # Ga terug naar main
git checkout mijn-feature  # Ga naar je feature branch
```

## Merging: Branches samenvoegen

Als je klaar bent met je feature, wil je die terug in `main` brengen. Dit heet **mergen**.

```bash
# 1. Ga naar main
git checkout main

# 2. Merge je feature branch
git merge mijn-feature
```

### Visueel

```
Voor merge:
main:        A --- B --- C
                         \
feature:                  D --- E

Na merge:
main:        A --- B --- C --- D --- E
```

## Branch verwijderen

Na het mergen kan je de branch opruimen:

```bash
git branch -d mijn-feature
```

## Waarom branches gebruiken?

| Zonder branches | Met branches |
|-----------------|--------------|
| Iedereen werkt in dezelfde code | Iedereen heeft een eigen plek |
| Bugs komen direct in productie | Je kan testen voor je merget |
| Moeilijk om samen te werken | Makkelijk om parallel te werken |
| Geen manier om te experimenteren | Probeer dingen uit zonder risico |

## Commando overzicht

| Commando | Wat doet het? |
|----------|---------------|
| `git branch` | Bekijk alle branches |
| `git checkout -b <naam>` | Maak en switch naar nieuwe branch |
| `git checkout <naam>` | Switch naar een branch |
| `git merge <naam>` | Merge een branch in je huidige branch |
| `git branch -d <naam>` | Verwijder een branch |

---

**Oefening:** [Branching oefening](../oefeningen/03-branching.md)

**Volgende les:** [Pull Requests](05-pull-requests.md)
