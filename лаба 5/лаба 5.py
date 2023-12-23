while True:
    try:
        n = int(input("Введите количество строк в матрице:"))
        break
    except ValueError:
        print("Введите число:")
while True:
    try:
        m = int(input("Введите количество столбцов в матрице:"))
        break
    except ValueError:
        print("Введите число:")
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        while True:
            try:
                element = int(input("Введите элемент:"))
                row.append(element)
                break
            except ValueError:
                print("Введите число:")
                matrix.append(row)
    matrix.append(row)
def min_elements(matrix):
    smallest_elements = []
    for i in range(len(matrix)):
        if i % 2 == 1:
            smallest_element = min(matrix[i])
            smallest_elements.append(smallest_element)
    return smallest_elements

def swap_max_min(matrix):
    flat_matrix = [item for row in matrix for item in row]
    max_value = max(flat_matrix)
    min_value = min(flat_matrix)

    max_index = flat_matrix.index(max_value)
    min_index = flat_matrix.index(min_value)

    flat_matrix[max_index], flat_matrix[min_index] = flat_matrix[min_index], flat_matrix[max_index]

    result_matrix = [flat_matrix[i:i + len(matrix[0])] for i in range(len(flat_matrix)) if i % len(matrix[0]) == 0]
    return result_matrix

smallest_elements = min_elements(matrix)
print("Наименьшие элементы четных строк:", smallest_elements)

swapped_matrix = swap_max_min(matrix)
print("Матрица после замены наибольшего и наименьшего элементов:", swapped_matrix)
