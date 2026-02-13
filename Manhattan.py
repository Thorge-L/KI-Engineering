# Day 2 Manhattan distance and cosine similarity

import math

# I. Manhattan distance
def d(a,b):
    distance = abs(a-b)
    return distance

print(d(8,15))

# II. Cosine similarity

# Using the functions of day 1 and 2
def scalar_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    
    product = 0
    for a, b in zip(vector_a, vector_b):
        product += a * b
    
    return product

def euclidean_norm(vector):
    sum_of_squares = sum(i ** 2 for i in vector) 
    return math.sqrt(sum_of_squares) 


def cosine_sim(a,b):
    if len(a) != len(b):
        print("Vectors must be of same length")
    similarity= (scalar_product(a,b))/(euclidean_norm(a)*euclidean_norm(b))
    return similarity

print(cosine_sim([1,2],[2,4,6]))