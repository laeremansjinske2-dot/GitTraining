# Les 2: Forken & Clonen

## Wat is een Fork?

Een **fork** is een kopie van iemand anders' repository naar jouw eigen GitHub account. Je krijgt een eigen versie waar je vrij in kan werken zonder het origineel te beinvloeden.

```
Originele repo (eigenaar)     Jouw fork (jouw account)
┌─────────────────┐           ┌─────────────────┐
│  GitTraining     │  fork →   │  GitTraining     │
│  (origineel)     │           │  (jouw kopie)    │
└─────────────────┘           └─────────────────┘
```

### Hoe fork je?

1. Ga naar de repository op GitHub
2. Klik op de **"Fork"** knop rechtsboven
3. Kies je eigen account
4. Klaar! Je hebt nu je eigen kopie

## Wat is Clonen?

**Clonen** is een repository downloaden van GitHub naar je eigen computer, zodat je er lokaal aan kan werken.

```
GitHub (online)               Jouw computer (lokaal)
┌─────────────────┐           ┌─────────────────┐
│  Jouw fork       │  clone →  │  GitTraining/    │
│  (online kopie)  │           │  (lokale kopie)  │
└─────────────────┘           └─────────────────┘
```

### Hoe clone je?

1. Ga naar jouw fork op GitHub
2. Klik op de groene **"Code"** knop
3. Kopieer de URL (HTTPS)
4. Open een terminal en typ:

```bash
git clone https://github.com/JOUW-USERNAME/GitTraining.git
```

5. Ga naar de map:

```bash
cd GitTraining
```

## De volledige flow

```
Origineel       →  Fork (GitHub)  →  Clone (je PC)
(andermans repo)   (jouw online)     (jouw lokaal)
```

## Handige commando's

| Commando | Wat doet het? |
|----------|---------------|
| `git clone <url>` | Download een repo naar je computer |
| `git remote -v` | Bekijk de remote verbindingen |

> **Tip:** Na het clonen kan je `git remote -v` uitvoeren om te zien waar je repo mee verbonden is.

---

**Oefening:** [Fork & Clone oefening](../oefeningen/01-fork-en-clone.md)

**Volgende les:** [Stage, Commit & Push](03-commit-en-push.md)
