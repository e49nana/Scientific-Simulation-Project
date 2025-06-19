'''
Pflichtaufgabe 7 behandelt das Heron-Verfahren (auch bekannt als Babylonisches Wurzelziehen), 
eine Methode zur iterativen oder rekursiven Approximation der Quadratwurzel einer Zahl a > 0.
Ziel ist der Vergleich zwischen einer iterativen und einer rekursiven Implementierung.
'''
# Pflichtaufgabe 9 – Heron-Verfahren (Quadratwurzel durch Iteration und Rekursion)
import math

# Heron-Verfahren iterativ
def heron_ite(a, an, epsilon):
    while abs(an**2 - a) > epsilon:
        an = 0.5 * (an + a / an)
    return an

# Heron-Verfahren rekursiv
def heron_rek(a, an, epsilon):
    if abs(an**2 - a) <= epsilon:
        return an
    return heron_rek(a, 0.5 * (an + a / an), epsilon)

# Beispiel: a = 144.01
a = 144.01
a0 = (a + 1) / 2  # Startwert
epsilon = 1e-5

# Exakter Wert zur Kontrolle
print(f"Exakte Wurzel: {math.sqrt(a)}")

# Iterative Lösung
wurzel_iterativ = heron_ite(a, a0, epsilon)
print(f"Heron iterativ: {wurzel_iterativ}")

# Rekursive Lösung
wurzel_rekursiv = heron_rek(a, a0, epsilon)
print(f"Heron rekursiv: {wurzel_rekursiv}")
