import math

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def generate_pascals_triangle_ncr(rows):
    triangle = []
    for i in range(rows):
        current_row = []
        for j in range(i + 1):
            current_row.append(combinations(i, j))
        triangle.append(current_row)
    return triangle