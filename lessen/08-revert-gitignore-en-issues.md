# Les 8: Revert, .gitignore & GitHub Issues

## Waarom deze les?
Dit zijn drie praktische dingen die je heel vaak nodig hebt in echte projecten:

- Een foute commit veilig terugdraaien (`git revert`)
- Bestanden bewust lokaal houden (`.gitignore`)
- Werk organiseren met issues (bugs, taken, ideeën)

## 1) Revert: een commit ongedaan maken zonder geschiedenis te breken

### Wat is het?
`git revert` maakt een **nieuwe commit** die de gekozen commit terugdraait.

Dit is veilig op gedeelde branches, omdat je de bestaande geschiedenis niet herschrijft.

### Basisstappen

```bash
git log --oneline
# Zoek de commit-hash die je wil terugdraaien

git revert <commit-hash>
git push
```

### Wanneer gebruiken?
- Iets staat al op `main`
- Je wil snel terug naar een werkende staat
- Anderen hebben de commit mogelijk al binnengehaald

## 2) .gitignore: wat hoort niet in Git?

### Wat is het?
In `.gitignore` zet je bestanden/mappen die Git niet moet tracken.

### Typische voorbeelden

```gitignore
__pycache__/
*.log
.env
```

### Belangrijk detail
Als een bestand al tracked is, dan is alleen toevoegen aan `.gitignore` niet genoeg.
Je moet het eerst untracken:

```bash
git rm --cached bestandsnaam
```

## 3) GitHub Issues: werk en bugs bijhouden

### Wat is het?
Een issue is een ticket voor:
- een bug
- een taak
- een idee of verbetering

### Goed issue format (kort)
- **Titel:** duidelijk en concreet
- **Beschrijving:** wat is het probleem / wat wil je bereiken?
- **Checklist:** kleine stappen om op te volgen

### Waarom handig?
- Iedereen ziet wat nog open staat
- Taken kunnen verdeeld worden
- Je kan issues linken aan PR's

## Samenvatting

- `git revert` = veilige undo met extra commit
- `.gitignore` = lokale rommel uit je repo houden
- `Issues` = betere planning en samenwerking

---

**Volgende stap:** maak de oefening [08-revert-gitignore-en-issues](../oefeningen/06-revert-gitignore-en-issues.md).
