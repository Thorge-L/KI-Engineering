import unittest
from vector_engine import VectorEngine

class TestVectorEngine(unittest.TestCase):
    
    def test_scalar_product(self):
      
        v1 = [1, 2, 3]
        v2 = [4, 5, 6]
        # Erwartet: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
        result = VectorEngine.scalar_product(v1, v2)
        self.assertEqual(result, 32)

    def test_dimension_mismatch(self):
       
        v1 = [1, 2]
        v2 = [1, 2, 3]
      
        with self.assertRaises(ValueError):
            VectorEngine.scalar_product(v1, v2)

    def test_cosine_similarity_ortho(self):
       
        v1 = [1, 0]
        v2 = [0, 1]
        result = VectorEngine.cosine_sim(v1, v2)
        # Bei Floats nutzen wir assertAlmostEqual wegen Rundungsfehlern!
        self.assertAlmostEqual(result, 0.0)

    def test_cosine_similarity_zero_vector(self):
       
        v1 = [0, 0]
        v2 = [1, 1]
        result = VectorEngine.cosine_sim(v1, v2)
        self.assertEqual(result, 0.0)

if __name__ == '__main__':
    unittest.main()