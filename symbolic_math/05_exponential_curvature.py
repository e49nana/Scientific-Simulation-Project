#Aufgabe 6. Exponentialfunktion - Krümmung
#Wir betrachten die Exponential-Funktion f(x) = ea x mit reellem Exponenten a.

#nach sympy anrufen für symbolische Rechnungen
import sympy as sy

#nach matplotlib und numpy für zukunftige charts
import matplotlib.pyplot as plt
import numpy as np

#Variabeln
x = sy.symbols('x', real=True)
a = sy.symbols('a', positive=True)

#exponentiale funktion definieren
def f(x, a):
    return sy.exp(a * x)

#krümmung berechnen
def krümmung(x, a):
    f1 = sy.diff(f(x, a), x)        # f'(x)
    f2 = sy.diff(f(x, a), x, x)     # f''(x)
    denom = (1 + f1**2)**(3/2)      # nenner der formel
    return f2 / denom               # krümmungsformel

a_values = [1, 2] # anfangswerte a = 1, 2
colors = ['green', 'blue']
#n = 1, plt.figure(figsize=(12, 5))

#chart bilden
fig, ax = plt.subplots()
for idx, a_val in enumerate(a_values):
    # krümmungsabteilung
    krümmung_expr =krümmung(x, a).subs(a, a_val)         #  a bekommst 1,2
    krümmung_derivative = sy.diff(krümmung_expr, x)       # erste abteilung
    x0 = sy.solve(krümmung_derivative, x)[0]  # exakte lösung
    y0 = f(x, a).subs({x: x0, a: a_val})  # f(x0)

        #wenn f''<0, haben wir einer local max
    #nehmen wir an dass, wir mindestens eine lösung haben

    #für den plot umsetzen
    f_np = sy.lambdify(x, f(x, a).subs(a, a_val), modules="numpy")
    x_vals = np.linspace(float(x0) - 2, float(x0) + 2, 300)
    y_vals = f_np(x_vals)

    #fig, ax = plt.subplots(1,2)

    #krümmung zeichnen
    ax.plot(x_vals, y_vals, label=f'$f(x) = e^{{{a_val}x}}$', color='blue') #kurve, krümmung
    ax.plot(float(x0), float(y0), 'ro', label=f'max krümmungspoint\n$(x_0, f(x_0))$') #krümmungspunkt max
    ax.stem([float(x0)], [float(y0)], linefmt='r--', markerfmt='ro', basefmt=" ") #plot ein rotter punkt und eine ligne

    # Chart aussicht
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Exponentialle Funktion und maximale Krümmung a = 1")
    ax.legend()
    ax.grid(True)
    plt.show()







#------------------------------------------------------------------------

a_val = 2  # anfangswert a = 2

# krümmungsabteilung
krümmung_expr = krümmung(x, a).subs(a, a_val)         #  a bekommst 1
krümmung_derivative = sy.diff(krümmung_expr, x)       # erste abteilung
x0_candidates = sy.solve(krümmung_derivative, x)   # wo sind die nullen


for x0 in x0_candidates:
    second_derivative = sy.diff(krümmung_expr, x, x).subs(x, x0)
    print(f"x0 = {x0.evalf()}, zweite abteilung = {second_derivative.evalf()}")

    #wenn f''<0, haben wir einer local max
#nehmen wir an dass, wir mindestens eine lösung haben
x0 = x0_candidates[0]
y0 = f(x, a).subs({a: a_val, x: x0})

#für den plot umsetzen
f_lambdified = sy.lambdify(x, f(x, a).subs(a, a_val), modules="numpy")
x_vals = np.linspace(float(x0) - 2, float(x0) + 2, 300)
y_vals = f_lambdified(x_vals)

#krümmung zeichnen
fig, ax = plt.subplots(1,2,2)
ax.plot(x_vals, y_vals, label=f'$f(x) = e^{{{a_val}x}}$', color='blue') #kurve, krümmung
ax.plot(float(x0), float(y0), 'ro', label=f'max krümmungspoint\n$(x_0, f(x_0))$') #krümmungspunkt max
ax.stem([float(x0)], [float(y0)], linefmt='r--', markerfmt='ro', basefmt=" ") #plot ein rotter punkt und eine ligne

# Chart aussicht
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("Exponentialle Funktion und maximale Krümmung")
ax.legend()
ax.grid(True)
plt.show()

