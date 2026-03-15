"""
Kleuren module - wordt gebruikt voor de merge conflict oefening!
"""


def favoriete_kleur():
    return "groen"


def kleuren_lijst():
    return ["rood", "blauw", "groen", "geel", "paars", "roze"]


def kleur_mix(kleur1, kleur2):
    if kleur1 == "rood" and kleur2 == "blauw":
        return "paars"
    elif kleur1 == "blauw" and kleur2 == "rood":
        return "paars"
    elif kleur1 == "rood" and kleur2 == "geel":
        return "oranje"
    elif kleur1 == "geel" and kleur2 == "rood":
        return "oranje"
    elif kleur1 == "blauw" and kleur2 == "geel":
        return "groen"
    elif kleur1 == "geel" and kleur2 == "blauw":
        return "groen"
    else:
        return "mix van " + kleur1 + " en " + kleur2


print("Mijn favoriete kleur is:", favoriete_kleur())
print("Alle kleuren:", kleuren_lijst())
print("Rood + blauw =", kleur_mix("rood", "blauw"))
print("Rood + geel =", kleur_mix("rood", "geel"))
