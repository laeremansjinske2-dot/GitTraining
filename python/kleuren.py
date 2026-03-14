"""
Kleuren module - wordt gebruikt voor de merge conflict oefening!
"""


def favoriete_kleur():
    """Geeft de favoriete kleur terug."""
    return "blauw"


def kleuren_lijst():
    """Geeft een lijst van kleuren terug."""
    return ["rood", "blauw", "groen", "geel", "paars"]


def kleur_mix(kleur1, kleur2):
    """Mixt twee kleuren."""
    mixen = {
        ("rood", "blauw"): "paars",
        ("blauw", "rood"): "paars",
        ("rood", "geel"): "oranje",
        ("geel", "rood"): "oranje",
        ("blauw", "geel"): "groen",
        ("geel", "blauw"): "groen",
    }
    return mixen.get((kleur1, kleur2), f"mix van {kleur1} en {kleur2}")


def main():
    print(f"Mijn favoriete kleur is: {favoriete_kleur()}")
    print(f"Alle kleuren: {kleuren_lijst()}")
    print(f"Rood + blauw = {kleur_mix('rood', 'blauw')}")
    print(f"Rood + geel = {kleur_mix('rood', 'geel')}")


if __name__ == "__main__":
    main()
