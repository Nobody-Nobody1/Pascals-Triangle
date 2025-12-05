import PascalsDamnTriangle

num_rows = 10
pascal_triangle = PascalsDamnTriangle.generate_pascals_triangle_ncr(num_rows)
for row in pascal_triangle:
    print(row)
