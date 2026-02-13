# Day 2 Euclidean norm
import math
def euclidean_norm(vector):
    sum_of_squares = sum(i ** 2 for i in vector) 
    return math.sqrt(sum_of_squares) 

print(euclidean_norm([3,4]))
