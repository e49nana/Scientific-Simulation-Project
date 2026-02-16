###############################################################################
# Aufgabe 03
###############################################################################
import matplotlib.pyplot as plt  # für Listen
import sympy as sy  # für symbolische Rechnungen
import numpy as np  # für Arrays


# Variabeln ohne Einheiten
m = 1200  # Masse ~ kg
C = 39 / 100  # Koefficient (kg/m)
Fa = 2000  # Kraft ~ N

# Werte der Störungen
listn = [0, 1, 10, 100]

# t als Symbol für numerische Rechnungen
t = sy.symbols('t', real=True)

# Störungsparameter epsilon
eps = 0.1


# Nicht gestörte Strecke Funktion s(t)
def strecke(t):
    # generel Argument Rechnungen : sqrt(C * Fa / m) * t
    argument = sy.sqrt(C * Fa / m) * t
    # s(t) = (m / C) * ln(cosh(argument))
    s = (m / C) * sy.log(sy.cosh(argument))
    return s


# Nicht-gestörte Geschwindigkeit Funktion v(t) per Differenzierung von s(t)
def geschwindigkeit(t):
    s = strecke(t)
    v = sy.diff(s, t)  # Symbolische Differenzierung von s(t) nach t
    return v


# s_eps(t) = s(t) + eps*sin(n*t)
def gestorte_strecke(t, eps, n):
    s_perturbed = strecke(t) + eps * sy.sin(n * t)
    return s_perturbed

def gestorte_geschwindigkeit(t, eps, n):
    s_perturbed = gestorte_strecke(t, eps, n)
    v_perturbed = sy.diff(s_perturbed, t)  # Ableitung der gestörten Strecke um der geschwindigkeit zu bekommen
    return v_perturbed


# Machen wir ein Array mit Werten für den Plot, von 0 bis 120 Sekunden
t_vals = np.linspace(0, 120, 500)

# CÜbersetzungen von symbolische Ausdrücke (nicht gestörten) zu numerischen Funktionnen mit lambdify
s_func = sy.lambdify(t, strecke(t), modules=['numpy'])
v_func = sy.lambdify(t, geschwindigkeit(t), modules=['numpy'])

# Groß Chart
plt.figure(figsize=(12, 5))

# --------------------------- Strecke Plot -----------------------------
plt.subplot(1, 2, 1)  # Sub chart 1
# s(t) plot
plt.plot(t_vals, s_func(t_vals), label="s(t) * nicht gestörte", linewidth=2)

# Schleifen durch n-Werten für gestörten Funktionnen Chart
for n in listn:
    s_eps_expr = gestorte_strecke(t, eps, n)  # s_eps(t)
    s_eps_func = sy.lambdify(t, s_eps_expr, modules=['numpy'])  # von symbolisch nach numerisch
    plt.plot(t_vals, s_eps_func(t_vals), label=f"s_eps(t), n={n}", linestyle='--')

plt.xlabel("Zeit (s)")
plt.ylabel("Strecke s(t)")
plt.title("Zeit - Strecke Gesetz")
plt.legend()

# --------------------------- Geschwindigkeit plot ------------------------------
plt.subplot(1, 2, 2)  # Sub chart 2
# Chart nicht gestörte Geschwindigkeit
plt.plot(t_vals, v_func(t_vals), label="v(t) * nicht gestörte ", linewidth=2)

# Schleifen durch n-Werten für gestörten Funktionnen Chart
for n in listn:
    v_eps_expr = gestorte_geschwindigkeit(t, eps, n)  # Symbolische Ausdrücke von v_eps(t) nach n gegeben.
    v_eps_func = sy.lambdify(t, v_eps_expr, modules=['numpy'])  # von symbolisch nach numerisch
    plt.plot(t_vals, v_eps_func(t_vals), label=f"v_eps(t), n={n}", linestyle='--')

plt.xlabel("Zeit (s)")
plt.ylabel("Geschwindigkeit v(t)")
plt.title("Zeit - Geschwindigkeit Gesetz")
plt.legend()

plt.tight_layout()  # Space adjustment
plt.show()  #
