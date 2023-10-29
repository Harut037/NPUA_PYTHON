import random

def generate_random_matrix(rows, columns):
    matrix = [[random.randint(1, 100) for _ in range(columns)] for _ in range(rows)]
    return matrix

def get_column_sum(matrix, column_index):
    column_sum = sum(row[column_index] for row in matrix)
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average




matrix = generate_random_matrix(5, 5)


print("Random matrix")
for row in matrix:
    print(row)


column_sum = get_column_sum(matrix, 2)
print(f"\nSum of values in third column: {column_sum}")


row_average = get_row_average(matrix, 2)
print(f"Average value in third row: {row_average}")
