"""
Given a matrix, find the path from top left to bottom right with the greatest product by moving only down and right.

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

Output: 2016 ( because of this: 1 -> 4 -> 7 -> 8 -> 9)
 
A= [[-1, 2, 3],
    [4, 5, -6],
    [7, 8, 9]]

Output: 1080 (-1 -> 4 -> 5 -> -6 -> 9)
"""

def find_largest_path(matrix, order):
     import pdb; pdb.set_trace()
     return None

if __name__ == "__main__":
     user_input_matrix_order = input('Enter the matrix order(row column):\norder: ')
     matrix_row, matrix_column = map(int, user_input_matrix_order.split())
     matrix = []
     for x in range(matrix_row):
          row = input('{} row: '.format(x))
          matrix.append(list(map(int, row.split())))

     product = find_largest_path(matrix, (matrix_row, matrix_column))

