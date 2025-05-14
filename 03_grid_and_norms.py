###############################################################################
# Aufgabe 3: Vektornormen, Listen und Visualisierung der Gitterpunkte
###############################################################################
import math  # Pour les opérations mathématiques (racine carrée, etc.)
import matplotlib.pyplot as plt  # Pour la visualisation

# Définir M, le nombre de pas dans chaque direction
M = 400
h = 1 / M  # Pas de discrétisation

# Générer la liste de tous les points du quadrilatère Ω = [-1,1]x[-1,1]
# Chaque point est [x, y] avec x = i*h, y = j*h pour i, j = -M,...,M
xy_list = [[i * h, j * h] for i in range(-M, M + 1) for j in range(-M, M + 1)]

# Initialiser les listes pour chaque norme.
# Pour la 1-Norm (somme des valeurs absolues)
points_1_le = []  # Points pour lesquels |x|₁ ≤ 1
points_1_gt = []  # Points pour lesquels |x|₁ > 1

# Pour la 2-Norm (norme euclidienne)
points_2_le = []  # Points pour lesquels |x|₂ ≤ 1
points_2_gt = []  # Points pour lesquels |x|₂ > 1

# Pour la ∞-Norm (norme maximum)
points_inf_le = []  # Points pour lesquels |x|∞ ≤ 1
points_inf_gt = []  # Points pour lesquels |x|∞ > 1

# Parcourir tous les points et les répartir dans les listes selon les conditions de norme
for point in xy_list:
    x, y = point
    # Calcul de la 1-Norm : |x|₁ = |x| + |y|
    norm1 = abs(x) + abs(y)
    # Calcul de la 2-Norm : |x|₂ = sqrt(x² + y²)
    norm2 = math.sqrt(x ** 2 + y ** 2)
    # Calcul de la ∞-Norm : |x|∞ = max(|x|, |y|)
    norm_inf = max(abs(x), abs(y))

    # Répartition selon la 1-Norm
    if norm1 <= 1:
        points_1_le.append(point)
    else:
        points_1_gt.append(point)

    # Répartition selon la 2-Norm
    if norm2 <= 1:
        points_2_le.append(point)
    else:
        points_2_gt.append(point)

    # Répartition selon la ∞-Norm
    if norm_inf <= 1:
        points_inf_le.append(point)
    else:
        points_inf_gt.append(point)


# Fonction utilitaire pour "décompacter" une liste de points en deux listes séparées pour x et y
def separate_points(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return xs, ys


# Séparer les coordonnées pour chaque cas de norme
x_1_le, y_1_le = separate_points(points_1_le)
x_1_gt, y_1_gt = separate_points(points_1_gt)

x_2_le, y_2_le = separate_points(points_2_le)
x_2_gt, y_2_gt = separate_points(points_2_gt)

x_inf_le, y_inf_le = separate_points(points_inf_le)
x_inf_gt, y_inf_gt = separate_points(points_inf_gt)

# Création d'une figure avec trois sous-graphes (un pour chaque norme)
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# --------------------------- Visualisation pour la 1-Norm ---------------------------
axes[0].plot(x_1_le, y_1_le, 'o', color='red', label='|x|₁ ≤ 1')
axes[0].plot(x_1_gt, y_1_gt, 'o', color='blue', label='|x|₁ > 1')
axes[0].set_title("1-Norm (Betragssummennorm)")
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[0].legend()
axes[0].grid(True)

# --------------------------- Visualisation pour la 2-Norm ---------------------------
axes[1].plot(x_2_le, y_2_le, 'o', color='red', label='|x|₂ ≤ 1')
axes[1].plot(x_2_gt, y_2_gt, 'o', color='blue', label='|x|₂ > 1')
axes[1].set_title("2-Norm (Euklidisch)")
axes[1].set_xlabel("x")
axes[1].set_ylabel("y")
axes[1].legend()
axes[1].grid(True)

# --------------------------- Visualisation pour la ∞-Norm ---------------------------
axes[2].plot(x_inf_le, y_inf_le, 'o', color='red', label='|x|∞ ≤ 1')
axes[2].plot(x_inf_gt, y_inf_gt, 'o', color='blue', label='|x|∞ > 1')
axes[2].set_title("∞-Norm (Maximumsnorm)")
axes[2].set_xlabel("x")
axes[2].set_ylabel("y")
axes[2].legend()
axes[2].grid(True)

# Titre global et ajustement de la mise en page
plt.suptitle(f"Gitterpunkte im Quadrat Ω mit M={M} (h={h})")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
