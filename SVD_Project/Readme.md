# SVD Image Compression

**Bildkompression mit Singulärwertzerlegung (SVD)**

An interactive Python application demonstrating image compression using Singular Value Decomposition, developed as part of the *Seminar zu Simulationstools* course at TH Nürnberg.

<p align="center">
  <img src="assets/demo_screenshot.png" alt="SVD Compressor GUI" width="600">
</p>

## 📚 Mathematical Background

### Singular Value Decomposition

For any matrix $A \in \mathbb{R}^{m \times n}$, the SVD factorization gives:

$$A = U \Sigma V^\top$$

where:
- $U \in \mathbb{R}^{m \times m}$ — orthogonal matrix of left singular vectors
- $\Sigma \in \mathbb{R}^{m \times n}$ — diagonal matrix with singular values $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$
- $V \in \mathbb{R}^{n \times n}$ — orthogonal matrix of right singular vectors

### Low-Rank Approximation

The rank-$k$ approximation is obtained by keeping only the $k$ largest singular values:

$$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^\top = U_k \Sigma_k V_k^\top$$

### Eckart–Young–Mirsky Theorem

This approximation is **optimal** in the Frobenius norm sense:

$$\|A - A_k\|_F^2 = \sum_{i=k+1}^{r} \sigma_i^2$$

No other rank-$k$ matrix achieves a smaller approximation error.

### Compression Ratio

The storage requirement for a rank-$k$ approximation is:

$$N_k = k(m + n + 1)$$

floating-point numbers per channel, compared to $m \times n$ for the original.

| Rank $k$ | Storage | Compression |
|----------|---------|-------------|
| 10       | ~2%     | 50×          |
| 50       | ~10%    | 10×          |
| 100      | ~20%    | 5×           |

*(for a 1000×1000 image)*

## 🚀 Features

- **Interactive GUI** — Real-time rank adjustment with slider
- **Side-by-side comparison** — Original vs. compressed image
- **Live metrics** — Frobenius norm error and compression ratio
- **Multi-channel support** — Works with both grayscale and RGB images
- **Educational focus** — Clear visualization of SVD concepts

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/scientific-simulations.git
cd scientific-simulations/svd-image-compression

# Install dependencies
pip install numpy pillow
```

## 🎮 Usage

```bash
python svd_compressor.py
```

1. Click **"Bild einlesen"** to load an image
2. Adjust the rank $k$ using the slider
3. Observe how image quality and compression ratio change

## 📊 Results

<p align="center">
  <img src="assets/rank_comparison.png" alt="Rank comparison" width="700">
</p>

*Reconstruction quality at different ranks: k=5, k=10, k=15, k=20*

### Key Observations

- **k < 10**: Strong blur, only gross structures visible
- **k = 10–30**: Contours become sharp, main features recognizable  
- **k = 30–100**: Quality approaches original, fine details emerge
- **k > 100**: Differences only visible under close inspection

## 📄 Documentation

The full project report (in German) is available in [`projektbericht_svd.pdf`](projektbericht_svd.pdf), covering:

- Mathematical foundations of SVD
- Implementation details
- User manual
- Experimental results and analysis
- Comparison with JPEG compression

## 🛠️ Technical Details

### Dependencies

- Python 3.8+
- NumPy (SVD computation)
- Pillow (image I/O)
- Tkinter (GUI)

### Algorithm Complexity

- SVD computation: $O(\min(m,n) \cdot m \cdot n)$
- Reconstruction: $O(k \cdot m \cdot n)$

## 👥 Authors

- **Maximilian Bazlov**
- **Emmanuel Nana Nana**

*B-AMP3: Seminar zu Simulationstools*  
*Technische Hochschule Nürnberg Georg Simon Ohm*  
*Fakultät Angewandte Mathematik, Physik und Allgemeinwissenschaften*

## 📜 License

MIT License — see [LICENSE](../LICENSE) for details.

## 🔗 References

- Eckart, C., & Young, G. (1936). The approximation of one matrix by another of lower rank. *Psychometrika*, 1(3), 211-218.
- Golub, G. H., & Van Loan, C. F. (2013). *Matrix Computations* (4th ed.). Johns Hopkins University Press.
