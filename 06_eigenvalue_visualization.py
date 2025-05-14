'''
Pflichtaufgabe 8 untersucht die Berechnung der Eigenwerte einer Matrix A und einer 
ähnlichen Matrix B = T⁻¹ A T. Es werden die charakteristischen Polynome von A und B 
bestimmt, deren Nullstellen als numerische Eigenwerte berechnet und mit den 
direkten Eigenwerten aus SymPy verglichen. Die Eigenwerte werden in der 
komplexen Ebene visualisiert.
'''

# Pflichtaufgabe 8 – Eigenwerte über charakteristisches Polynom und direkte Methoden

import sympy as sy
import matplotlib.pyplot as plt

# Dimension der Matrix

N =12 # doppelt ko nj ug ie rt komplexe EW -1 \ pm i , -2 \ pm 2* i , -3 \ pm 3* i
zei = [ -82944 , -304128 , -557568 , -649344 , -529168 , -315264 ,
-140544 , -47232 , -11912 , -2208 , -288 , -24 ]

# Eigenwerte: -1 ± i, -2 ± 2i, -3 ± 3i → erzeugt über charakteristisches Polynom
# Die Koeffizienten erzeugen eine Matrix A mit diesen Eigenwerten
#zei = [-288, -528, -484, -240, -72, -12]


# Konstruktion der Matrix A (N×N)
A = sy.zeros(N - 1, N)
for i in range(N - 1):
    A[i, i + 1] = 1
A = A.row_insert(N - 1, sy.Matrix(1, N, zei))  # letzte Zeile hinzufügen

# Zufallsmatrix T zur Erzeugung einer ähnlichen Matrix B
T = sy.randMatrix(N, N, -10, 10) / 10.01
B = T.inv() * A * T  # B = T⁻¹ A T

# Charakteristische Polynome von A und B
pA = A.charpoly().as_expr()
pB = B.charpoly().as_expr()

# Numerische Nullstellen der charakteristischen Polynome
ewA_roots = sy.nroots(pA)
ewB_roots = sy.nroots(pB)

# Direkte Berechnung der Eigenwerte
ewA_direct = list(A.eigenvals().keys())
ewB_direct = list(B.eigenvals().keys())

# Aufteilung in Real- und Imaginärteil für Plot
def get_parts(eigenlist):
    return [sy.re(z).evalf() for z in eigenlist], [sy.im(z).evalf() for z in eigenlist]

ewA_re, ewA_im = get_parts(ewA_roots)
ewB_re, ewB_im = get_parts(ewB_roots)
ewA_dre, ewA_dim = get_parts(ewA_direct)
ewB_dre, ewB_dim = get_parts(ewB_direct)

# Visualisierung
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle("Eigenwerte in der komplexen Ebene")

# A: Wurzeln von pA
axs[0, 0].scatter(ewA_re, ewA_im, color='red')
axs[0, 0].set_title("Nullstellen von pA (Matrix A)")

# B: Wurzeln von pB
axs[0, 1].scatter(ewB_re, ewB_im, color='blue')
axs[0, 1].set_title("Nullstellen von pB (Matrix B)")

# A: direkte Methode
axs[1, 0].scatter(ewA_dre, ewA_dim, color='green')
axs[1, 0].set_title("Direkte Eigenwerte von A")

# B: direkte Methode
axs[1, 1].scatter(ewB_dre, ewB_dim, color='purple')
axs[1, 1].set_title("Direkte Eigenwerte von B")

# Achsenformatierung
for ax in axs.flat:
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.grid(True)
    ax.set_aspect("equal")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
