import numpy as np

class SAW:
    def __init__(self) -> None:
        pass

    def start(self, m, w, b):
        weights = np.array(w)
        benefit = np.array(b)
        matrix = np.array(m)
        # Normalisasi matriks berdasarkan kriteria benefit dan cost
        normalized_matrix = np.zeros_like(matrix, dtype=float)
        for i in range(matrix.shape[1]):
            if benefit[i]:  # Jika kriteria adalah benefit, gunakan metode maximization
                normalized_matrix[:, i] = matrix[:, i] / np.max(matrix[:, i])
            else:  # Jika kriteria adalah cost, gunakan metode minimization
                normalized_matrix[:, i] = np.min(matrix[:, i]) / matrix[:, i]

        # Mengalikan matriks normalisasi dengan bobot
        weighted_matrix = normalized_matrix * weights

        # Menghitung skor akhir untuk setiap alternatif
        final_scores = np.sum(weighted_matrix, axis=1)
        return final_scores