import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

def exact_derivative(x):
    return -np.sin(x)

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def main():
    x = 1.0
    exact = exact_derivative(x)

    h_values = np.logspace(-16, -1, 100)
    errors = []

    for h in h_values:
        approx = forward_difference(f, x, h)
        error = abs(approx - exact)
        errors.append(error)

    # Plotting
    plt.loglog(h_values, errors, marker='o')
    plt.xlabel("Step size (h)")
    plt.ylabel("Absolute error")
    plt.title("Numerical Differentiation Error vs. Step Size")
    plt.grid(True, which='both', ls='--')
    plt.show()

    # Print smallest error and associated h
    min_error = min(errors)
    best_h = h_values[errors.index(min_error)]
    print(f"Minimum error: {min_error:.2e} at h = {best_h:.2e}")

if __name__ == "__main__":
    main()
