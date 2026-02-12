<div align="center">

<!-- HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:1f6feb&height=180&section=header&text=Scientific%20Simulation%20Project&fontSize=36&fontColor=58a6ff&fontAlignY=35&desc=Numerical%20Computing%20%E2%80%A2%20Symbolic%20Math%20%E2%80%A2%20Scientific%20Visualization&descSize=15&descColor=8b949e&descAlignY=55&animation=fadeIn" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](#)
[![SymPy](https://img.shields.io/badge/SymPy-3B5526?style=for-the-badge&logo=sympy&logoColor=white)](#)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-58a6ff?style=for-the-badge)](LICENSE)

</div>

---

## 📖 About

Computational mathematics projects and exercises from **"Einführung in Simulationstools"** (Introduction to Simulation Tools) at **TH Nürnberg**, as part of my B.Sc. in Applied Mathematics & Physics.

This repository covers three pillars of scientific computing: **numerical precision**, **symbolic computation**, and **matrix analysis** — each implemented as interactive Jupyter notebooks with visualizations.

---

## 📚 Notebooks

### 🧮 Numerical Precision & Fundamentals

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 1 | Floating-point arithmetic | `floating_point.ipynb` | IEEE 754, `Decimal` & `Rational`, machine epsilon |
| 2 | Numerical differentiation | `subtraction_cancellation.ipynb` | Cancellation error, step-size optimization |
| 3 | Heron's method | `heron_method.ipynb` | Babylonian algorithm, convergence rate analysis |

### 📈 Symbolic Computation & Analysis

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 4 | Disturbed motion | `disturbed_motion.ipynb` | ODE modeling with SymPy, perturbation analysis |
| 5 | Curvature analysis | `curvature_exponential.ipynb` | κ(x) for exponential families, osculating circles |
| 6 | Taylor approximation | `taylor_errors.ipynb` | Remainder bounds, convergence radius |
| 10 | Functions & tangents | `functions_tangents_sympy.ipynb` | Symbolic derivatives, tangent-line plotting |

### 📊 Grids, Norms & Matrix Computations

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 7 | Grid generation | `grid_generation.ipynb` | Uniform & Chebyshev nodes, L¹/L²/L∞ norms |
| 8 | Eigenvalue sensitivity | `matrix_eigen_sensitivity.ipynb` | Condition numbers, similarity transforms |
| 9 | Determinant methods | `determinant_comparison.ipynb` | Cofactor vs LU vs Bareiss, O(n!) vs O(n³) |

---

## 🏗️ Project Structure

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
│   ├── taylor_errors.ipynb
│   └── functions_tangents_sympy.ipynb
│
├── grids_and_matrices/
│   ├── grid_generation.ipynb
│   ├── matrix_eigen_sensitivity.ipynb
│   └── determinant_comparison.ipynb
│
├── utils/
│   └── numerical_differentiation.py
│
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/e49nana/Scientific-Simulation-Project.git
cd Scientific-Simulation-Project

# Install dependencies
pip install numpy sympy matplotlib jupyter

# Launch
jupyter notebook
```

---

## 🛠️ Tech Stack

<div align="center">

| Tool | Role |
|------|------|
| **Python 3.10+** | Core language |
| **NumPy** | Numerical arrays & linear algebra |
| **SymPy** | Symbolic differentiation, integration, series |
| **Matplotlib** | Publication-quality plots |
| **Jupyter** | Interactive exploration & documentation |

</div>

---

## 🗺️ Roadmap

Upcoming projects that will extend this repository into a full scientific computing portfolio:

- [x] Numerical precision & floating-point analysis
- [x] Symbolic computation & ODE modeling
- [x] Matrix computations & eigenvalue sensitivity
- [ ] 🔥 **Heat Equation Solver** — Finite Differences (explicit/implicit) + FEM with animated 2D visualization
- [ ] 🖼️ **Image Compression via SVD** — Low-rank approximation, PSNR analysis, Eckart-Young theorem
- [ ] 🌍 **COVID-19 Spatial Analysis** *(R)* — Moran's I, LISA clusters, Getis-Ord Gi*, bivariate choropleth maps
- [ ] ⚡ **ODE Solvers Comparison** — Euler vs RK4 vs adaptive methods, stability regions
- [ ] 📐 **PDE-Constrained Optimization** — Adjoint method, gradient-based solvers

---

## 📖 Learning Outcomes

Each notebook builds intuition through implementation:

- **Numerical stability** — Why does $(f(x+h)-f(x))/h$ fail for very small $h$? Explored with real floating-point experiments.
- **Symbolic → Numeric bridge** — Model a system symbolically with SymPy, then discretize and solve numerically with NumPy.
- **Matrix conditioning** — How a tiny perturbation in $A$ can cause a huge shift in its eigenvalues.
- **Visualization as understanding** — Every concept is accompanied by plots that reveal the underlying mathematics.

---

## 👤 Author

**Emmanuel Nana Nana**  
B.Sc. Applied Mathematics & Physics — TH Nürnberg  
🎯 MSc @ TUM | Exchange @ École Polytechnique (EuroTech)

[![GitHub](https://img.shields.io/badge/GitHub-e49nana-181717?style=flat&logo=github)](https://github.com/e49nana)

---

## 📄 License

[MIT License](LICENSE) — free to use for educational purposes.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:1f6feb&height=100&section=footer" width="100%"/>

</div>
