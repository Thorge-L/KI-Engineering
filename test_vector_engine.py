import unittest
from vector_engine import VectorEngine

class TestVectorEngine(unittest.TestCase):
    
    def test_scalar_product(self):
        """Prüft, ob das Skalarprodukt korrekt berechnet wird."""
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        # Erwartet: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
        result = VectorEngine.scalar_product(v1, v2)
        self.assertEqual(result, 32)

    def test_dimension_mismatch(self):
        """Prüft, ob der ValueError bei falschen Längen geworfen wird."""
        v1 = [1, 2]
        v2 = [1, 2, 3]
        # Wir erwarten, dass ein ValueError "raised" (geworfen) wird
        with self.assertRaises(ValueError):
            VectorEngine.scalar_product(v1, v2)

    def test_cosine_similarity_ortho(self):
        """Prüft, ob orthogonale (rechtwinklige) Vektoren 0 ergeben."""
        v1 = [1, 0]
        v2 = [0, 1]
        result = VectorEngine.cosine_sim(v1, v2)
        # Bei Floats nutzen wir assertAlmostEqual wegen Rundungsfehlern!
        self.assertAlmostEqual(result, 0.0)

    def test_cosine_similarity_zero_vector(self):
        """Prüft unseren Epsilon-Check von Tag 3."""
        v1 = [0, 0]
        v2 = [1, 1]
        result = VectorEngine.cosine_sim(v1, v2)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()