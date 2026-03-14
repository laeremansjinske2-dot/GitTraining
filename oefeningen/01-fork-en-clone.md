# Oefening 1: Fork & Clone

## Doel
Je eigen kopie van deze repository krijgen op je computer.

## Stappen

### 1. Fork de repository
- Ga naar de originele repository op GitHub
- Klik op **"Fork"** rechtsboven
- **Belangrijk:** zet het vinkje bij "Copy the `main` branch only" **UIT** zodat je alle branches meekrijgt!
- Kies je eigen account

### 2. Clone je fork
```bash
git clone https://github.com/JOUW-USERNAME/GitTraining.git
cd GitTraining
```

### 3. Controleer
```bash
# Bekijk de remote verbinding
git remote -v

# Je zou iets zoals dit moeten zien:
# origin  https://github.com/JOUW-USERNAME/GitTraining.git (fetch)
# origin  https://github.com/JOUW-USERNAME/GitTraining.git (push)
```

### 4. Bekijk de bestanden
```bash
# Bekijk alle bestanden
ls

# Bekijk de Git status
git status
```

## Checklist
- [ ] Repository geforkt
- [ ] Repository geclonet naar je computer
- [ ] `git remote -v` toont jouw fork
- [ ] `git status` werkt zonder errors

**Iets niet duidelijk? Ga terug naar naar [de uitleg](/lessen/02-fork-en-clone.md)!**
**Klaar? Ga door naar [oefening 2](02-commit-en-push.md)!**
