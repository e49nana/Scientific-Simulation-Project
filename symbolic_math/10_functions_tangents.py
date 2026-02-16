import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def main():
    # Define symbolic variable and function
    x = sp.symbols('x')
    f_expr = sp.sin(x) * sp.exp(-x / 3)  # example: f(x) = sin(x) * exp(-x/3)

    # Compute derivative symbolically
    f_prime_expr = sp.diff(f_expr, x)

    # Choose point to evaluate tangent
    x0_val = 2.0
    f_val = float(f_expr.subs(x, x0_val))
    f_prime_val = float(f_prime_expr.subs(x, x0_val))

    # Define tangent line: y = f(x0) + f'(x0)(x - x0)
    tangent_line = f_val + f_prime_val * (x - x0_val)

    # Convert symbolic expressions to numerical functions
    f_lambdified = sp.lambdify(x, f_expr, "numpy")
    tangent_lambdified = sp.lambdify(x, tangent_line, "numpy")

    # Create x-values for plotting
    x_vals = np.linspace(x0_val - 3, x0_val + 3, 400)
    y_vals = f_lambdified(x_vals)
    tangent_vals = tangent_lambdified(x_vals)

    # Plot function and tangent
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label="f(x)", linewidth=2)
    plt.plot(x_vals, tangent_vals, '--', label="Tangent at x = {:.1f}".format(x0_val), linewidth=2)
    plt.scatter([x0_val], [f_val], color='red', zorder=5)
    plt.text(x0_val, f_val, f"  ({x0_val:.1f}, {f_val:.2f})", verticalalignment='bottom')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Function and Tangent Line")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
