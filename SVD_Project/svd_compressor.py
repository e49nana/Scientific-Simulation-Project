"""
SVD Image Compressor
====================
Interactive GUI application for image compression using Singular Value Decomposition.

Authors: Maximilian Bazlov, Emmanuel Nana Nana
Course: B-AMP3 - Seminar zu Simulationstools
Institution: Technische Hochschule Nürnberg Georg Simon Ohm

This application demonstrates image compression using the mathematical concept of
low-rank matrix approximation via SVD. The Eckart-Young-Mirsky theorem guarantees
that the rank-k approximation is optimal in the Frobenius norm sense.
"""

import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, ttk
from typing import Tuple, List, Optional


class SVDCompressor:
    """
    SVD-based image compressor implementing rank-k approximation.
    
    For a matrix A ∈ ℝ^(m×n), the SVD gives A = UΣV^T where:
    - U ∈ ℝ^(m×m) contains left singular vectors
    - Σ ∈ ℝ^(m×n) is diagonal with singular values σ₁ ≥ σ₂ ≥ ... ≥ σᵣ > 0
    - V ∈ ℝ^(n×n) contains right singular vectors
    
    The rank-k approximation A_k = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ minimizes ||A - B||_F
    over all matrices B with rank(B) ≤ k.
    """
    
    def __init__(self):
        self.U_list: List[np.ndarray] = []
        self.S_list: List[np.ndarray] = []
        self.V_list: List[np.ndarray] = []
        self.original_shape: Optional[Tuple[int, int, int]] = None
        self.is_grayscale: bool = False
        
    def load_image(self, filepath: str) -> np.ndarray:
        """Load and prepare image for SVD computation."""
        img = Image.open(filepath)
        
        # Convert to RGB or grayscale
        if img.mode == 'L':
            self.is_grayscale = True
            data = np.array(img, dtype=np.float64)
            data = data[:, :, np.newaxis]
        else:
            self.is_grayscale = False
            img = img.convert('RGB')
            data = np.array(img, dtype=np.float64)
            
        self.original_shape = data.shape
        return data
    
    def compute_svd(self, data: np.ndarray) -> None:
        """
        Compute SVD for each color channel.
        
        Uses numpy.linalg.svd with full_matrices=False for efficiency
        (thin SVD: only computes min(m,n) singular vectors).
        """
        self.U_list = []
        self.S_list = []
        self.V_list = []
        
        n_channels = data.shape[2] if len(data.shape) == 3 else 1
        
        for i in range(n_channels):
            channel = data[:, :, i] if n_channels > 1 else data
            U, s, Vt = np.linalg.svd(channel, full_matrices=False)
            self.U_list.append(U)
            self.S_list.append(s)
            self.V_list.append(Vt)
    
    def reconstruct(self, k: int) -> np.ndarray:
        """
        Reconstruct image using rank-k approximation.
        
        A_k = U_k @ Σ_k @ V_k^T
        
        where U_k, V_k contain the first k columns/rows and Σ_k is k×k diagonal.
        """
        channels = []
        
        for U, s, Vt in zip(self.U_list, self.S_list, self.V_list):
            # Rank-k approximation: A_k = U[:,:k] @ diag(s[:k]) @ V[:k,:]
            reconstructed = (U[:, :k] @ np.diag(s[:k])) @ Vt[:k, :]
            channels.append(reconstructed)
        
        # Stack channels and clip to valid range [0, 255]
        result = np.stack(channels, axis=2) if len(channels) > 1 else channels[0]
        result = np.clip(result, 0, 255).astype(np.uint8)
        
        if self.is_grayscale:
            result = result[:, :, 0]
            
        return result
    
    def compute_error(self, k: int) -> float:
        """
        Compute Frobenius norm of approximation error.
        
        ||A - A_k||_F = sqrt(Σᵢ₌ₖ₊₁ʳ σᵢ²)
        
        This is computed efficiently from discarded singular values.
        """
        total_error_sq = 0.0
        
        for s in self.S_list:
            if k < len(s):
                total_error_sq += np.sum(s[k:]**2)
                
        return np.sqrt(total_error_sq)
    
    def compute_compression_size(self, k: int) -> Tuple[float, float]:
        """
        Calculate storage requirements for rank-k approximation.
        
        Storage = k(m + n + 1) × 8 bytes per channel (64-bit floats)
        
        Returns:
            Tuple of (compressed size in KB, percentage of original)
        """
        if self.original_shape is None:
            return 0.0, 0.0
            
        m, n = self.original_shape[0], self.original_shape[1]
        n_channels = self.original_shape[2] if len(self.original_shape) == 3 else 1
        
        # Storage: k columns of U (m×k) + k singular values + k rows of V (k×n)
        compressed_elements = k * (m + n + 1) * n_channels
        compressed_bytes = compressed_elements * 8  # 64-bit floats
        
        original_bytes = m * n * n_channels
        
        compressed_kb = compressed_bytes / 1024
        percentage = (compressed_bytes / original_bytes) * 100
        
        return compressed_kb, percentage
    
    def get_max_rank(self) -> int:
        """Return maximum possible rank (min of image dimensions)."""
        if self.original_shape is None:
            return 1
        return min(self.original_shape[0], self.original_shape[1])
    
    def get_singular_values(self, channel: int = 0) -> np.ndarray:
        """Return singular values for specified channel."""
        if channel < len(self.S_list):
            return self.S_list[channel]
        return np.array([])


class SVDCompressorGUI:
    """
    Tkinter GUI for interactive SVD image compression.
    
    Features:
    - Load any image (JPG, PNG, etc.)
    - Real-time rank adjustment via slider
    - Display of approximation error and compression ratio
    - Side-by-side comparison of original and compressed images
    """
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("SVD Bildkompressor")
        self.root.geometry("900x700")
        
        self.compressor = SVDCompressor()
        self.original_image: Optional[Image.Image] = None
        self.current_k = 20
        
        self._setup_ui()
        
    def _setup_ui(self):
        """Initialize all UI components."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Load button
        self.load_btn = ttk.Button(
            main_frame, 
            text="Bild einlesen", 
            command=self._load_image
        )
        self.load_btn.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Image labels
        ttk.Label(main_frame, text="Originalbild").grid(row=1, column=0)
        ttk.Label(main_frame, text="Komprimiert").grid(row=1, column=1)
        
        # Image display canvases
        self.original_canvas = tk.Canvas(main_frame, width=400, height=400, bg='gray')
        self.original_canvas.grid(row=2, column=0, padx=5, pady=5)
        
        self.compressed_canvas = tk.Canvas(main_frame, width=400, height=400, bg='gray')
        self.compressed_canvas.grid(row=2, column=1, padx=5, pady=5)
        
        # Rank slider
        self.rank_var = tk.IntVar(value=20)
        self.rank_slider = ttk.Scale(
            main_frame,
            from_=1,
            to=100,
            variable=self.rank_var,
            orient='horizontal',
            command=self._on_slider_change
        )
        self.rank_slider.grid(row=3, column=0, columnspan=2, sticky='ew', pady=10)
        
        # Rank label
        self.rank_label = ttk.Label(main_frame, text="Rang k: 20")
        self.rank_label.grid(row=4, column=0, columnspan=2)
        
        # Error display
        self.error_label = ttk.Label(main_frame, text="Approximationsfehler (F-Norm): -")
        self.error_label.grid(row=5, column=0, columnspan=2)
        
        # Size display
        self.size_label = ttk.Label(main_frame, text="Größe (SVD-Daten): -")
        self.size_label.grid(row=6, column=0, columnspan=2)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def _load_image(self):
        """Handle image loading via file dialog."""
        filepath = filedialog.askopenfilename(
            title="Bild auswählen",
            filetypes=[
                ("Bilder", "*.jpg *.jpeg *.png *.bmp *.gif"),
                ("Alle Dateien", "*.*")
            ]
        )
        
        if not filepath:
            return
            
        # Load and process image
        data = self.compressor.load_image(filepath)
        self.compressor.compute_svd(data)
        
        # Store original for display
        self.original_image = Image.open(filepath).convert('RGB')
        
        # Update slider range
        max_rank = self.compressor.get_max_rank()
        self.rank_slider.configure(to=max_rank)
        
        # Display images
        self._display_original()
        self._update_compressed()
        
    def _display_original(self):
        """Display the original image on canvas."""
        if self.original_image is None:
            return
            
        # Resize for display
        display_img = self.original_image.copy()
        display_img.thumbnail((400, 400), Image.Resampling.LANCZOS)
        
        self.original_photo = ImageTk.PhotoImage(display_img)
        self.original_canvas.delete("all")
        self.original_canvas.create_image(200, 200, image=self.original_photo)
        
    def _update_compressed(self):
        """Update compressed image display based on current k."""
        if not self.compressor.S_list:
            return
            
        k = self.rank_var.get()
        
        # Reconstruct image
        reconstructed = self.compressor.reconstruct(k)
        compressed_img = Image.fromarray(reconstructed)
        
        # Resize for display
        compressed_img.thumbnail((400, 400), Image.Resampling.LANCZOS)
        
        self.compressed_photo = ImageTk.PhotoImage(compressed_img)
        self.compressed_canvas.delete("all")
        self.compressed_canvas.create_image(200, 200, image=self.compressed_photo)
        
        # Update labels
        error = self.compressor.compute_error(k)
        size_kb, percentage = self.compressor.compute_compression_size(k)
        
        self.rank_label.configure(text=f"Rang k: {k}")
        self.error_label.configure(text=f"Approximationsfehler (F-Norm): {error:.2f}")
        self.size_label.configure(
            text=f"Größe (SVD-Daten): {size_kb:.1f} KB ({percentage:.1f}% vom Original)"
        )
        
    def _on_slider_change(self, event=None):
        """Handle slider value changes."""
        self._update_compressed()


def main():
    """Entry point for the SVD compressor application."""
    root = tk.Tk()
    app = SVDCompressorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
