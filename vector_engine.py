# Einführung in die Klassen

import math

class VectorEngine:
    @staticmethod
    def _check_dimensions(v1, v2):
    if len(v1) != len(v2):
            raise ValueError("Vectors must be of the same length")



    @staticmethod  # scalar product
    def scalar_product(v1, v2):
        VectorEngine._check_dimensions(v1, v2)
        
        product = 0
        for a, b in zip(v1, v2):
            product += a * b

        return product

    @staticmethod  # Euclidean norm (L2)
    def euclidean_norm(vector):
        sum_of_squares = sum(i ** 2 for i in vector) 
        return math.sqrt(sum_of_squares) 

    @staticmethod  # Manhattan distance L1 norm
    def d(v1, v2):
        VectorEngine._check_dimensions(v1, v2)
        distance = 0
        for coordinate1,coordinate2 in zip(v1, v2):
            distance += abs(coordinate1 - coordinate2)
        return distance
    
    @staticmethod  # Cosine similarity
    def cosine_sim(v1: list[float], v2: list[float]):
        VectorEngine._check_dimensions(v1, v2)

        norm_v1 = VectorEngine.euclidean_norm(v1)
        norm_v2 = VectorEngine.euclidean_norm(v2)

        if norm_v1 or norm_v2 < 1e-10:
            return 0.0
        
        similarity = (VectorEngine.scalar_product(v1, v2)) / (VectorEngine.euclidean_norm(v1) * VectorEngine.euclidean_norm(v2))
        return similarity