# Day 1, small code calculating the scalar product of two vectors 
def scalar_product(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must be of the same length")
    
    product = 0
    for a, b in zip(vector_a, vector_b):
        product += a * b
    
    return product
# Example usage
vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
result = scalar_product(vector_a, vector_b)
print("The scalar product of", vector_a, "and", vector_b, "is:", result)


