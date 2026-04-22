# Tussen Les 1 en 2: Git installeren & eerste setup

Voor je kan forken en clonen, moet Git correct op je computer staan en eenmalig ingesteld zijn.

## 1. Git installeren

### Windows

1. Ga naar [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download en start de installer
3. Klik door met de standaardopties
4. Open daarna **Git Bash** of je terminal

### macOS

Optie A (makkelijkst): installeer via Homebrew

```bash
brew install git
```

Optie B: installeer Xcode Command Line Tools

```bash
xcode-select --install
```

### Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install git -y
```

## 2. Controleer of Git werkt

Voer uit in je terminal:

```bash
git --version
```

Je krijgt iets zoals `git version 2.x.x`.

## 3. Stel je naam en e-mail in (eenmalig)

Gebruik dezelfde e-mail als je GitHub-account.

```bash
git config --global user.name "Jouw Naam"
git config --global user.email "jij@example.com"
```

Controle:

```bash
git config --global --list
```

## 4. Handige basisinstellingen

```bash
git config --global init.defaultBranch main
git config --global pull.rebase false
```

## 5. (Optioneel) Authenticatie kiezen

Voor de training werkt HTTPS prima. Als je vaak met Git werkt, kan je later SSH instellen.

## Veelvoorkomende problemen

| Probleem | Oplossing |
|----------|-----------|
| `git` wordt niet herkend | Sluit/open je terminal opnieuw. Werkt het nog niet: herstart je pc |
| Verkeerde naam of e-mail | Voer `git config --global user.name` en `git config --global user.email` opnieuw uit |
| Onzeker over je instellingen | Gebruik `git config --global --list` |

---

**Volgende les:** [Forken & Clonen](02-fork-en-clone.md)
