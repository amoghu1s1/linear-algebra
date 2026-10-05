"""Elementary vector operations: dot product, norm, and angle between vectors."""

import ast
import math


def dot_product(u, v):
    """Return the dot product of vectors u and v."""
    if len(u) != len(v):
        raise ValueError("Vectors must be of the same length!")

    return sum(a * b for a, b in zip(u, v))


def norm(v):
    """Return the Euclidean norm of vector v."""
    return math.sqrt(dot_product(v, v))


def angle_degrees(u, v):
    """Return the angle between vectors u and v in degrees."""
    norm_u = norm(u)
    norm_v = norm(v)

    if norm_u == 0 or norm_v == 0:
        raise ValueError("The given vector cannot be the zero vector.")

    cosine = dot_product(u, v) / (norm_u * norm_v)
    cosine = max(-1.0, min(1.0, cosine))  # guard against rounding errors
    return math.degrees(math.acos(cosine))


def main():
    print("Please provide the vectors in this format: [x,y,z,u]")
    u = ast.literal_eval(input("Vector 1: "))
    v = ast.literal_eval(input("Vector 2: "))

    print(f"Here is your dot product:  {dot_product(u, v)}")
    print(f"Here is the norm: {norm(v)}")
    print(f"Here is the angle in degrees: {angle_degrees(u, v)}")


if __name__ == "__main__":
    main()
