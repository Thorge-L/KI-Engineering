# Day 3 Einführung in die Klassen

import math

class VectorEngine:

    @staticmethod  # scalar product
    def scalar_product(vector_a, vector_b):
        if len(vector_a) != len(vector_b):
            raise ValueError("Vectors must be of the same length")
        
        product = 0
        for a, b in zip(vector_a, vector_b):
            product += a * b

        return product

    @staticmethod  # Euclidean norm (L2)
    def euclidean_norm(vector):
        sum_of_squares = sum(i ** 2 for i in vector) 
        return math.sqrt(sum_of_squares) 

    @staticmethod  # Manhattan distance L1 norm
    def d(a, b):
        distance = abs(a - b)
        return distance
    
    @staticmethod  # Cosine similarity
    def cosine_sim(a: list[float], b: list[float]):
        if len(a) != len(b):
            raise ValueError("Vectors must be of same length")
        similarity = (VectorEngine.scalar_product(a, b)) / (VectorEngine.euclidean_norm(a) * VectorEngine.euclidean_norm(b))
        return similarity
