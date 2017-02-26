import unittest
from hell_triangle import solve_hell_triangle

class TestStringMethods(unittest.TestCase):

    def test_solution_for_one_element(self):
        self.assertEqual(solve_hell_triangle(0,0,[[6]]), 6)

    def test_solution(self):
        self.assertEqual(solve_hell_triangle(0,0,[[6],[3,5],[9,7,1],[4,6,8,4]]), 26)

    def test_raises_exception_if_no_array_is_provided(self):
        self.assertRaises(TypeError, solve_hell_triangle, 0, 0, 6)

    def test_raises_exception_if_no_sub_array_is_provided(self):
        self.assertRaises(TypeError, solve_hell_triangle, 0, 0, [6])

    def test_raises_exception_if_row_sizes_are_wrong(self):
        self.assertRaises(ValueError, solve_hell_triangle, 0, 0, [[6],[9,7,1],[4,6,8,4]])

    def test_raises_exception_if_element_type_is_wrong(self):
        self.assertRaises(ValueError, solve_hell_triangle, 0, 0, [[6],[3,5],[9,'A',1],[4,6,8,4]])    

    def test_raises_exception_if_row_is_none(self):
        self.assertRaises(ValueError, solve_hell_triangle, 0, 0, [[6],None,[9,'A',1],[4,6,8,4]])

    def test_raises_exception_if_element_is_none(self):
        self.assertRaises(ValueError, solve_hell_triangle, 0, 0, [[6],[3,None],[9,'A',1],[4,6,8,4]])         
        

if __name__ == '__main__':
    unittest.main()
