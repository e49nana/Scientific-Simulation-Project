import math                        # Importation du module math pour exp(), sin(), etc.
import matplotlib.pyplot as plt    # Importation de matplotlib pour la visualisation

# -----------------------------------------------------------------------------
# Teil a): Fehlerordnung prüfen - Taylorpolynom 4. Ordnung
# Näherung von f(x)=exp(x) mit T4(x) = 1 + x + x²/2 + x³/6 + x⁴/24
# Verfahrensfehler ist gegeben durch E4(h) = T4(h) - exp(h) = O(h^5)
# -----------------------------------------------------------------------------

# werte von h : h = 1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/64, 1/128
h_values_a = [1 / (2 ** i) for i in range(0, 8)]
errors_a = []   # Liste für E4(h) -- je ein Wert für jede h
# Für jeden h-Wert, berechnen wir dem Taylorspolynom und der Wert dem Fehler
for h in h_values_a:
    T4 = 1 + h + h**2/2 + h**3/6 + h**4/24     # T4(h)
    exp_h = math.exp(h)                        # exp(h)
    error = abs(T4 - exp_h)                    # Fehler E4(h)
    errors_a.append(error)                     # In der Liste speichern

# Erstellen einem Plot in doppelt-logarithmischer Darstellung
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)                          # subplot teil (a)
plt.loglog(h_values_a, errors_a, marker='o', linestyle='-', color='blue', label='E4(h)')
plt.xlabel('h')
plt.ylabel('Fehler E4(h)')
plt.title('Teil (a): Fehler des Taylorpolynoms 4. Ordnung für exp(x)')
plt.legend()
plt.grid(True, which="both", ls="--")         # Stellen einen Grid dar

# Erklärung:
# In einem Log-Log-Diagramm, wenn E4(h) = C-h^5, dann. 
# 
# ln(E4) = ln(C) + 5-ln(h),

# was eine Gerade mit der Steigung 5 darstellt. Die Punkte sollten sich also ungefähr auf einer Geraden ausrichten.

# -----------------------------------------------------------------------------
# Teil (b): Überprüfung der Fehlerordnung des quadratischen Taylorpolynoms.
# für die Funktion f(x,y) = 3 + exp(x)-sin(3y) in (x,y)=(h, h).
# Die gegebene Quadratik ist T2(h,h) = 3*(1 + h + h²).
# Der Fehler ist definiert durch E2(h) = |T2(h,h) - f(h,h)| und die erwartete theoretische Ordnung ist O(h^3)
# -----------------------------------------------------------------------------

# teil a) werte für teil (b) benutzen
h_values_b = h_values_a
errors_b = []   # Liste für E2(h) Werte

# für jede h, rechnen wir T2(h,h), f(h,h) und der Fehler E2(h)
for h in h_values_b:
    T2 = 3 * (1 + h + h**2)                    # Berechnung des quadratischen Taylorpolynoms T2(h,h)
    f_val = 3 + math.exp(h) * math.sin(3 * h)    # f(h,h)
    error = abs(T2 - f_val)                    # Fehler E2(h)
    errors_b.append(error)                     # In der Liste speichern

# Erstellen eines zweiten Subgraphen für Teil (b) in log-log-Skala
plt.subplot(1, 2, 2)                          # teil (b) subplot
plt.loglog(h_values_b, errors_b, marker='o', linestyle='-', color='green', label='E2(h)')
plt.xlabel('h')
plt.ylabel('Fehler E2(h)')
plt.title('Teil (b): Fehler des quadratischen Taylorpolynoms für f(x,y)')
plt.legend()
plt.grid(True, which="both", ls="--")         # grid darstellen

# Erklärung:
# Indem man x = h und y = h setzt und die Reihenentwicklung anwendet,
# findet man, dass f(h,h) = 3 + 3h + 3h² - 3h³ + O(h⁴). Somit ist T2(h,h) = 3 + 3h + 3h².
# und der Fehler ist von der Ordnung O(h³). In der Grafik log-log,
# 

#  ln(E2) ≈ ln(C') + 3·ln(h),


# daher sollten sich die Punkte ungefähr auf einer Geraden mit der Steigung 3 ausrichten.

# -----------------------------------------------------------------------------
# Anzeige der Abbildung mit den beiden Untergraphen
# -----------------------------------------------------------------------------
plt.tight_layout()   # Raum zwischen der Plot
plt.show()           # final darstellung
