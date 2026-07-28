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

## 📚 Scripts

### 🧮 Numerical Precision & Fundamentals

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 01 | Floating-point arithmetic | `numerical_precision/01_precision_comparison.py` | IEEE 754, `Decimal` & `Rational`, machine epsilon |
| 02 | Numerical differentiation | `numerical_precision/02_numerical_subtraction_cancellation.py` | Cancellation error, step-size optimization |
| 09 | Heron's method | `numerical_precision/09_heron_root_method.py` | Babylonian algorithm, convergence rate analysis |

### 📈 Symbolic Computation & Analysis

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 03 | Disturbed motion | `symbolic_math/03_disturbed_motion_model.py` | ODE modeling with SymPy, perturbation analysis |
| 05 | Curvature analysis | `symbolic_math/05_exponential_curvature.py` | κ(x) for exponential families, osculating circles |
| 06 | Taylor approximation | `symbolic_math/06_taylor_polynomial_error.py` | Remainder bounds, convergence radius |
| 10 | Functions & tangents | `symbolic_math/10_functions_tangents.py` | Symbolic derivatives, tangent-line plotting |
| 11 | Direction fields | `symbolic_math/11_richtungsfeld_plotter.py` | ODE direction-field visualization |

### 📊 Grids, Norms & Matrix Computations

| # | Topic | Notebook | Key Concepts |
|:-:|-------|----------|-------------|
| 04 | Grids & norms | `grids_and_matrices/04_grid_and_norms.py` | Uniform & Chebyshev nodes, L¹/L²/L∞ norms |
| 07 | Eigenvalue sensitivity | `grids_and_matrices/07_eigenvalue_visualization.py` | Condition numbers, similarity transforms |
| 08 | Determinant methods | `grids_and_matrices/08_determinant_computation_timing.py` | Cofactor vs LU vs Bareiss, O(n!) vs O(n³) |

---

## 🏗️ Project Structure

```
Scientific-Simulation-Project/
│
├── numerical_precision/        # 01, 02, 09 — floating point, cancellation, Heron
├── symbolic_math/              # 03, 05, 06, 10, 11 — SymPy modeling & analysis
├── grids_and_matrices/         # 04, 07, 08 — norms, eigenvalues, determinants
│
├── SVD_Project/                # Image compression via SVD — GUI app + report (PDF)
│   ├── svd_compressor.py
│   └── projektbericht_svd.pdf
│
├── Robotic/                    # ExoHand — exoskeleton arm build guides (DE/EN)
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
pip install -r requirements.txt

# Run any script directly, e.g.
python numerical_precision/01_precision_comparison.py
python SVD_Project/svd_compressor.py   # SVD compression GUI
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
- [x] 🖼️ **Image Compression via SVD** — GUI app + written report → [`SVD_Project/`](SVD_Project/)
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

[![GitHub](https://img.shields.io/badge/GitHub-e49nana-181717?style=flat&logo=github)](https://github.com/e49nana)

---

## 📄 License

[MIT License](LICENSE) — free to use for educational purposes.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,50:1a1b27,100:1f6feb&height=100&section=footer" width="100%"/>

</div>
