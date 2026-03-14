# Oefening 4: Pull Request

## Doel
Een Pull Request aanmaken vanuit je fork naar de originele repository.

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

### 4. Maak een Pull Request
1. Ga naar je fork op GitHub
2. Je ziet een melding over je recent gepushte branch
3. Klik op **"Compare & pull request"**
4. Zorg dat de PR gaat van **jouw fork** → **originele repo**
5. Schrijf een titel en beschrijving
6. Klik op **"Create pull request"**

### 5. Bekijk je PR
- Ga naar het **"Pull requests"** tabblad van de originele repo
- Je zou je PR moeten zien staan!

## Checklist
- [ ] Nieuwe branch aangemaakt
- [ ] Quiz vraag toegevoegd
- [ ] Wijziging gecommit en gepusht
- [ ] Pull Request aangemaakt
- [ ] PR is zichtbaar in de originele repo

**Klaar? Ga door naar [oefening 5](05-merge-conflict.md)!**
