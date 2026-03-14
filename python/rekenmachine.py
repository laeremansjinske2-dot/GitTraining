"""
Eenvoudige rekenmachine - Git Training
Pas deze functies aan als oefening!
"""


def optellen(a, b):
    """Tel twee getallen op."""
    return a + b


def aftrekken(a, b):
    """Trek b af van a."""
    return a - b


def vermenigvuldigen(a, b):
    """Vermenigvuldig twee getallen."""
    return a * b


def delen(a, b):
    """Deel a door b."""
    if b == 0:
        return "Fout: delen door nul!"
    return a / b


# === Voeg hieronder je eigen functies toe! ===
# Bijvoorbeeld: machtsverheffen, modulo, gemiddelde...


def main():
    print("=== Rekenmachine ===")
    print(f"5 + 3 = {optellen(5, 3)}")
    print(f"10 - 4 = {aftrekken(10, 4)}")
    print(f"6 * 7 = {vermenigvuldigen(6, 7)}")
    print(f"15 / 3 = {delen(15, 3)}")
    print(f"10 / 0 = {delen(10, 0)}")


if __name__ == "__main__":
    main()
