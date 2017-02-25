def validate_triangle_row(row_number, triangle):
  if triangle[row_number] is None:
    raise ValueError('Triangle row is null: ' + str(row_number))

  if len(triangle[row_number]) - 1 != row_number:
    raise ValueError('Row size invalid: ' + str(row_number))


def validate_element(row_number, element_position, triangle):
  if triangle[row_number][element_position] is None:
    raise ValueError('Triangle element is null: ' + str(row_number) + ':' + str(element_position))

  if not isinstance( triangle[row_number][element_position], ( int, long ) ):
    raise ValueError('Triangle element is invalid: ' + str(row_number) + ':' + str(element_position))


def solve_hell_triangle(current_row, current_element_position, triangle):
  validate_triangle_row(current_row, triangle)
  validate_element(current_row, current_element_position, triangle)

  next_row = current_row + 1

  if len(triangle) <= next_row:
    return triangle[current_row][current_element_position]

  left_triangle_sum = solve_hell_triangle(next_row, current_element_position, triangle)
  right_triangle_sum = solve_hell_triangle(next_row, current_element_position + 1, triangle)

  if left_triangle_sum > right_triangle_sum:
    return left_triangle_sum + triangle[current_row][current_element_position]

  return right_triangle_sum + triangle[current_row][current_element_position]


if __name__ == "__main__":
  import sys
  import ast

  print solve_hell_triangle(0, 0, ast.literal_eval(sys.argv[1]))
