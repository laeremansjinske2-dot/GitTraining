# Les 1: Wat zijn Git & GitHub?

## Het probleem

Stel je voor: je werkt aan een project met 3 klasgenoten. Iedereen bewerkt dezelfde bestanden. Hoe hou je bij wie wat heeft veranderd? Wat als iemand per ongeluk jouw code overschrijft?

Zonder versiebeheer krijg je dit:

```
project_v1.py
project_v2.py
project_v2_FINAL.py
project_v2_FINAL_echt_final.py
project_v2_FINAL_echt_final_fix.py
```

Herkenbaar? Dat kan beter.

## Wat is Git?

**Git** is een **versiebeheersysteem** (version control system). Het houdt alle wijzigingen bij die je maakt aan bestanden in een project.

Met Git kan je:
- Precies zien **wie** **wat** heeft veranderd en **wanneer**
- Teruggaan naar een **vorige versie** als er iets misgaat
- **Tegelijkertijd** met meerdere mensen aan hetzelfde project werken
- **Experimenteren** in een aparte "branch" zonder het hoofdproject te breken

Git werkt **lokaal** op je computer. Elke wijziging die je opslaat (een "commit") wordt bijgehouden in een verborgen `.git` map.

## Wat is GitHub?

**GitHub** is een **online platform** dat werkt met Git. Het is als een cloud backup + samenwerkingsplatform voor je code.

GitHub biedt extra features bovenop Git:
- **Repositories** (repo's) - je projecten online opslaan
- **Pull Requests** - wijzigingen voorstellen en bespreken
- **Issues** - bugs en taken bijhouden
- **Actions** - automatisch taken uitvoeren (bv. testen draaien)
- **Pages** - gratis websites hosten

> **Git** = het gereedschap op je computer
> **GitHub** = het online platform dat Git gebruikt

## Git vs GitHub

| Git | GitHub |
|-----|--------|
| Software op je computer | Website / online service |
| Houdt versies bij | Slaat je repo online op |
| Werkt offline | Heeft internet nodig |
| Command line tool | Grafische interface + extra features |

## Waarom is dit belangrijk?

- Bijna **elk softwarebedrijf** gebruikt Git
- Het is de **industriestandaard** voor versiebeheer
- GitHub heeft meer dan **100 miljoen** gebruikers
- Het staat op bijna elke **IT vacature**
- Het is **gratis** te gebruiken

---

**Volgende les:** [Git installeren & eerste setup](01b-git-installatie-en-setup.md)
