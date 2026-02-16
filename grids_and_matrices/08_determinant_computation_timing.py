'''
Pflichtaufgabe 8 vergleicht drei Methoden zur Berechnung der Determinante einer Matrix: 
die rekursive Laplace-Entwicklung, die symbolische Berechnung mit SymPy und die numerische 
Berechnung mit NumPy. Ziel ist es, den Rechenaufwand und die Genauigkeit zu untersuchen.
'''

# Pflichtaufgabe 10 – Determinantenvergleich mit verschiedenen Methoden
import sympy as sy
import numpy as np
import time

# Laplace-Entwicklung rekursiv
def det_laplace(A):
    n = A.shape[0]
    if n == 1:
        return A[0, 0]
    if n == 2:
        return A[0, 0]*A[1, 1] - A[0, 1]*A[1, 0]
    
    det = 0
    for j in range(n):
        minor = A.minor_submatrix(0, j)
        det += (-1)**j * A[0, j] * det_laplace(minor)
    return det

# Beispielmatrix: Hilbert-Matrix
N = 10
A = sy.Matrix(N, N, lambda i, j: sy.Rational(1, i + j + 1))

# Numerisch (mit NumPy)
Anum = sy.matrix2numpy(A, dtype='float64')
start = time.time()
det_numpy = np.linalg.det(Anum)
print(f"Det(Numpy) = {det_numpy:.6e}, Zeit: {time.time() - start:.4f} s")

# Symbolisch (mit SymPy)
start = time.time()
det_sympy = A.det()
print(f"Det(Sympy) = {det_sympy}, Zeit: {time.time() - start:.4f} s")

# Rekursiv (mit Laplace)
start = time.time()
det_lap = det_laplace(A)
print(f"Det(Laplace) = {det_lap}, Zeit: {time.time() - start:.4f} s")
