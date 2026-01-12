# 🔬 Scientific Simulation with Python

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org)
[![SymPy](https://img.shields.io/badge/SymPy-3B5526?style=flat&logo=sympy&logoColor=white)](https://sympy.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Numerical, symbolic, and computational mathematics exercises from the **"Einführung in Simulationstools"** course at **TH Nürnberg**.

---

## 🎯 Goals

- Strengthen core skills in **numerical precision** and **approximation theory**
- Master **differential equations** and **symbolic mathematics**
- Develop intuition through **scientific visualization**

---

## 📚 Contents

### 🧮 Numerical Precision & Fundamentals
| # | Topic | Notebook |
|---|-------|----------|
| 1 | Floating-point precision, Decimal & Rational arithmetic | `floating_point.ipynb` |
| 2 | Numerical differentiation & subtraction cancellation | `subtraction_cancellation.ipynb` |
| 3 | Heron's method (Babylonian) for square roots | `heron_method.ipynb` |

### 📈 Symbolic Computation & Analysis
| # | Topic | Notebook |
|---|-------|----------|
| 4 | Symbolic modeling of disturbed motion | `disturbed_motion.ipynb` |
| 5 | Curvature of exponential functions | `curvature_exponential.ipynb` |
| 6 | Taylor series approximation errors | `taylor_errors.ipynb` |
| 10 | Plotting functions & tangents with SymPy | `functions_tangents_sympy.ipynb` |

### 📊 Grids, Norms & Matrix Computations
| # | Topic | Notebook |
|---|-------|----------|
| 7 | Grid generation & norm comparisons | `grid_generation.ipynb` |
| 8 | Eigenvalue sensitivity to matrix similarity | `matrix_eigen_sensitivity.ipynb` |
| 9 | Comparison of determinant computation methods | `determinant_comparison.ipynb` |

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/e49nana/Scientific-Simulation-Project.git
cd Scientific-Simulation-Project

# Install dependencies
pip install numpy sympy matplotlib jupyter

# Launch Jupyter
jupyter notebook
```

---

## 📦 Project Structure

```
Scientific-Simulation-Project/
│
├── numerical_precision/
│   ├── floating_point.ipynb
│   ├── subtraction_cancellation.ipynb
│   └── heron_method.ipynb
│
├── symbolic_math/
│   ├── disturbed_motion.ipynb
│   ├── curvature_exponential.ipynb
│   └── taylor_errors.ipynb
│
├── grids_and_matrices/
│   ├── grid_generation.ipynb
│   ├── matrix_eigen_sensitivity.ipynb
│   └── determinant_comparison.ipynb
│
├── visualization/
│   └── functions_tangents_sympy.ipynb
│
└── utils/                          # ⬅️ NEW: Reusable modules
    └── numerical_differentiation.py
```

---

## 🛠️ Tech Stack

| Tool | Usage |
|------|-------|
| **Python 3.10+** | Core language |
| **NumPy** | Numerical computation |
| **SymPy** | Symbolic algebra & calculus |
| **Matplotlib** | Scientific visualization |
| **Jupyter** | Interactive notebooks |

---

## 📖 Learning Outcomes

- ✅ Understanding numerical stability and floating-point limitations
- ✅ Applying symbolic computation to real physical systems
- ✅ Analyzing matrix sensitivity and numerical errors
- ✅ Visualizing mathematical concepts for deeper intuition

---

## 🗺️ Roadmap

- [ ] Add Heat Equation solver (FD/FEM)
- [ ] Image compression using SVD
- [ ] ODE solvers comparison (Euler vs RK4)
- [ ] Interactive visualizations with Plotly

---

## 👤 Author

**Emmanuel Nana Nana**  
Applied Mathematics & Physics @ TH Nürnberg  

[![GitHub](https://img.shields.io/badge/GitHub-e49nana-181717?style=flat&logo=github)](https://github.com/e49nana)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/emmanuel-nana-nana)

---

## 📄 License

MIT License — feel free to use for educational purposes.

---

*✔️ More exercises and visual demonstrations will be added as the course progresses.*
