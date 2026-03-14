"""
Git Quiz - Test je kennis!
Voer dit script uit om je Git kennis te testen.
"""


def stel_vraag(vraag, opties, correct):
    """Stel een multiple choice vraag."""
    print(f"\n{vraag}")
    for i, optie in enumerate(opties, 1):
        print(f"  {i}. {optie}")

    try:
        antwoord = int(input("Jouw antwoord (nummer): "))
        if antwoord == correct:
            print("Correct!")
            return True
        else:
            print(f"Fout! Het juiste antwoord was: {correct}. {opties[correct - 1]}")
            return False
    except (ValueError, EOFError):
        print(f"Ongeldig. Het juiste antwoord was: {correct}. {opties[correct - 1]}")
        return False


def main():
    print("=" * 40)
    print("      GIT QUIZ")
    print("  Test je kennis!")
    print("=" * 40)

    score = 0
    totaal = 0

    vragen = [
        {
            "vraag": "Wat doet 'git init'?",
            "opties": [
                "Een repo clonen",
                "Een nieuwe Git repo aanmaken",
                "Een commit maken",
                "Een branch verwijderen",
            ],
            "correct": 2,
        },
        {
            "vraag": "Wat is het verschil tussen 'git add' en 'git commit'?",
            "opties": [
                "Er is geen verschil",
                "add uploadt, commit downloadt",
                "add staget wijzigingen, commit slaat ze op",
                "add maakt een branch, commit merget",
            ],
            "correct": 3,
        },
        {
            "vraag": "Wat doet 'git push'?",
            "opties": [
                "Wijzigingen ophalen van GitHub",
                "Een nieuwe branch maken",
                "Lokale commits uploaden naar GitHub",
                "Een bestand verwijderen",
            ],
            "correct": 3,
        },
        {
            "vraag": "Wat is een merge conflict?",
            "opties": [
                "Een fout in je Python code",
                "Wanneer twee branches dezelfde regel anders aanpassen",
                "Wanneer je internet uitvalt",
                "Wanneer je een branch verwijdert",
            ],
            "correct": 2,
        },
        {
            "vraag": "Wat is een Pull Request?",
            "opties": [
                "Een verzoek om code te downloaden",
                "Een manier om wijzigingen voor te stellen en te laten reviewen",
                "Een commando om branches te verwijderen",
                "Een type merge conflict",
            ],
            "correct": 2,
        },
        {
            "vraag": "Wat is een fork?",
            "opties": [
                "Een kopie van een repo naar je eigen account",
                "Een branch in je repo",
                "Een type commit",
                "Een Git commando",
            ],
            "correct": 1,
        },
    ]

    for v in vragen:
        totaal += 1
        if stel_vraag(v["vraag"], v["opties"], v["correct"]):
            score += 1

    print("\n" + "=" * 40)
    print(f"  Score: {score}/{totaal}")
    if score == totaal:
        print("  Perfect! Je bent een Git expert!")
    elif score >= totaal * 0.7:
        print("  Goed gedaan!")
    else:
        print("  Blijf oefenen, je komt er wel!")
    print("=" * 40)


if __name__ == "__main__":
    main()
