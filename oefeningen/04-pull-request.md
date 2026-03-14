# Oefening 4: Pull Request

## Doel
Een Pull Request aanmaken in je eigen fork en zelf reviewen.

## Stappen

### 1. Maak een nieuwe branch
```bash
git checkout -b feature/quiz-vraag
```

### 2. Voeg een vraag toe aan de quiz
Open `python/quiz.py` en voeg een nieuwe vraag toe aan de `vragen` lijst:

```python
{
    "vraag": "JOUW VRAAG HIER?",
    "opties": [
        "Optie A",
        "Optie B",
        "Optie C",
        "Optie D",
    ],
    "correct": 1,  # nummer van het juiste antwoord
},
```

### 3. Commit en push
```bash
git add python/quiz.py
git commit -m "voeg nieuwe quiz vraag toe"
git push -u origin feature/quiz-vraag
```

### 4. Maak een Pull Request in je eigen fork
1. Ga naar **jouw fork** op GitHub
2. Je ziet een melding over je recent gepushte branch
3. Klik op **"Compare & pull request"**
4. **Let op:** zorg dat de PR gaat naar **jouw eigen fork** (niet het origineel!)
   - Base repository: `JOUW-USERNAME/GitTraining` branch: `main`
   - Compare: `feature/quiz-vraag`
5. Schrijf een titel en beschrijving
6. Klik op **"Create pull request"**

### 5. Review je eigen PR
1. Open je PR en klik op het **"Files changed"** tabblad
2. Bekijk de wijzigingen - je ziet precies wat je hebt aangepast
3. Klik op een regelnummer om een **comment** achter te laten
4. Probeer een comment te schrijven, bv. "Goede vraag!" of "Misschien optie C aanpassen?"
5. Klik op **"Review changes"** rechtsboven
6. Kies **"Approve"** en klik **"Submit review"**

### 6. Merge je PR
1. Scroll naar beneden in je PR
2. Klik op **"Merge pull request"**
3. Klik op **"Confirm merge"**
4. Je branch is nu gemerged in main!

> **Tip:** De trainer zal live laten zien hoe het reviewen van iemand anders' PR eruit ziet!

## Checklist
- [ ] Nieuwe branch aangemaakt
- [ ] Quiz vraag toegevoegd
- [ ] Wijziging gecommit en gepusht
- [ ] Pull Request aangemaakt **in je eigen fork**
- [ ] PR bekeken via "Files changed"
- [ ] Comment achtergelaten op je eigen PR
- [ ] PR gemerged

**Klaar? Ga door naar [oefening 5](05-merge-conflict.md)!**
