# Les 6: Merge Conflicts

## Wat is een Merge Conflict?

Een **merge conflict** ontstaat wanneer twee branches **dezelfde regel** in hetzelfde bestand op een **verschillende manier** hebben aangepast. Git weet dan niet welke versie je wilt houden.

```
main:        "kleur = blauw"
                    ↕ conflict!
feature:     "kleur = rood"
```

## Wanneer gebeurt dit?

- Twee mensen bewerken **dezelfde regel** in hetzelfde bestand
- Een branch verwijdert een bestand dat een andere branch heeft gewijzigd
- Twee branches voegen content toe op **dezelfde plek**

## Hoe ziet een conflict eruit?

Wanneer Git een conflict detecteert, markeert het de problematische plek in je bestand:

```python
def favoriete_kleur():
<<<<<<< HEAD
    return "blauw"
=======
    return "rood"
>>>>>>> feature
```

- `<<<<<<< HEAD` = jouw huidige branch versie
- `=======` = scheiding tussen de twee versies
- `>>>>>>> feature` = de inkomende versie van de andere branch

## Hoe los je een conflict op?

### Stap 1: Bekijk het conflict

Open het bestand en zoek de conflict markers (`<<<<<<<`).

### Stap 2: Kies wat je wilt houden

Je hebt drie opties:
- **Houd jouw versie** (HEAD)
- **Houd de andere versie** (feature)
- **Combineer beide** (handmatig)

### Stap 3: Verwijder de conflict markers

```python
# Bijvoorbeeld: je kiest voor rood
def favoriete_kleur():
    return "rood"
```

**Vergeet niet** de `<<<<<<<`, `=======`, en `>>>>>>>` regels te verwijderen!

### Stap 4: Stage en commit

```bash
git add .
git commit -m "los merge conflict op"
```

## Hoe vermijd je conflicts?

| Tip | Waarom? |
|-----|---------|
| **Pull regelmatig** (`git pull`) | Hou je branch up-to-date |
| **Kleine commits** | Minder kans op overlapping |
| **Communiceer** met je team | Spreek af wie waar aan werkt |
| **Korte branches** | Hoe langer een branch leeft, hoe meer kans op conflicts |
| **Verdeel het werk** | Werk niet tegelijk aan hetzelfde bestand |

## Merge Conflicts in Pull Requests

Conflicts kunnen ook opduiken in **Pull Requests**! Als iemand een PR maakt en ondertussen is `main` veranderd op dezelfde plek, dan kan GitHub de PR niet automatisch mergen.

Je ziet dan op GitHub:

> **This branch has conflicts that must be resolved**

Je kan het conflict dan oplossen:
- **Op GitHub zelf** - klik "Resolve conflicts" (voor simpele conflicts)
- **Lokaal** - pull beide branches, merge lokaal, los op, en push

> **Demo:** De trainer laat een echte PR met een merge conflict zien!

## Demo: Een conflict zelf veroorzaken

We gaan dit live doen! Open `python/kleuren.py` en volg de instructies in de oefening.

---

**Oefening:** [Merge Conflict oefening](../oefeningen/05-merge-conflict.md)

**Volgende les:** [GitHub Actions & Pages](07-actions-en-pages.md)
