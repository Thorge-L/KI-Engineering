from vector_engine import VectorEngine
database = [
    [0.8,0.2,-0.5],[0.4,0.1,-0.2],[1.0,1.0,1.0]
]
query = [0.3,0.6,0.0]

max_score = -1.0
best_vector = None

for vector in database:
    score = VectorEngine.cosine_sim(vector, query)
    print(f"Vektor: {vector} hat Score : {score}")

    if score > max_score:
        max_score = score
        best_vector = vector

print(f"Den besten score hat {best_vector} mit einem Score von {max_score:.4f}")
