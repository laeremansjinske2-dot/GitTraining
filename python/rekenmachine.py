"""
Eenvoudige rekenmachine - Git Training
Pas deze functies aan als oefening!
"""


def optellen(a, b):
    return a + b


def aftrekken(a, b):
    return a - b


def vermenigvuldigen(a, b):
    return a * b


def delen(a, b):
    if b == 0:
        return "Fout: delen door nul!"
    return a / b


# === Voeg hieronder je eigen functies toe! ===
# Bijvoorbeeld: machtsverheffen, modulo, gemiddelde...


print("=== Rekenmachine ===")
print("5 + 3 =", optellen(5, 3))
print("10 - 4 =", aftrekken(10, 4))
print("6 * 7 =", vermenigvuldigen(6, 7))
print("15 / 3 =", delen(15, 3))
print("10 / 0 =", delen(10, 0))
