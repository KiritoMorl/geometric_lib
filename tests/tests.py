import unittest
import math
from circle import circle_area, circle_perimeter
from square import square_area, square_perimeter
from triangle import triangle_area, triangle_perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square_area(0)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = square_area(10)
        self.assertEqual(res, 100)
    
    def test_square_negative(self):
        res = square_area(-5)
        self.assertEqual(res, 25)
    
    def test_square_float(self):
        res = square_area(2.5)
        self.assertEqual(res, 6.25)
    
    def test_square_perimeter_zero(self):
        res = square_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_square_perimeter_positive(self):
        res = square_perimeter(5)
        self.assertEqual(res, 20)
    
    def test_square_perimeter_negative(self):
        res = square_perimeter(-3)
        self.assertEqual(res, -12)
    
    def test_square_perimeter_float(self):
        res = square_perimeter(1.5)
        self.assertEqual(res, 6.0)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle_area(0, 5)
        self.assertEqual(res, 0)
       
    def test_square_mul(self):
        res = triangle_area(10, 2)
        self.assertEqual(res, 10)
    
    def test_triangle_area_zero_height(self):
        res = triangle_area(10, 0)
        self.assertEqual(res, 0)
    
    def test_triangle_area_negative_base(self):
        res = triangle_area(-5, 4)
        self.assertEqual(res, -10)
    
    def test_triangle_area_negative_height(self):
        res = triangle_area(5, -4)
        self.assertEqual(res, -10)
    
    def test_triangle_area_float(self):
        res = triangle_area(3.5, 2.0)
        self.assertEqual(res, 3.5)
    
    def test_triangle_area_large_numbers(self):
        res = triangle_area(1000, 500)
        self.assertEqual(res, 250000)

    def test_perimeter_little_numbers(self):
        res = triangle_perimeter(1, 5, 3)
        self.assertEqual(res, 9)
       
    def test_perimeter_normal_numbers(self):
        res = triangle_perimeter(30, 100, 90)
        self.assertEqual(res, 220)

    def test_perimeter_big_numbers(self):
        res = triangle_perimeter(10000, 500000, 96000)
        self.assertEqual(res, 606000)
    
    def test_perimeter_zero_sides(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    
    def test_perimeter_negative_sides(self):
        res = triangle_perimeter(-2, -3, -4)
        self.assertEqual(res, -9)
    
    def test_perimeter_float_sides(self):
        res = triangle_perimeter(1.5, 2.5, 3.5)
        self.assertEqual(res, 7.5)
    
    def test_perimeter_mixed_signs(self):
        res = triangle_perimeter(5, -3, 2)
        self.assertEqual(res, 4)


class CircleTestCase(unittest.TestCase):
    def test_circle_area_zero(self):
        res = circle_area(0)
        self.assertEqual(res, 0)
    
    def test_circle_area_positive(self):
        res = circle_area(1)
        self.assertEqual(res, math.pi)
    
    def test_circle_area_negative(self):
        res = circle_area(-2)
        self.assertEqual(res, math.pi * 4)
    
    def test_circle_area_float(self):
        res = circle_area(0.5)
        self.assertEqual(res, math.pi * 0.25)
    
    def test_circle_area_large_number(self):
        res = circle_area(100)
        self.assertEqual(res, math.pi * 10000)
    
    def test_circle_perimeter_zero(self):
        res = circle_perimeter(0)
        self.assertEqual(res, 0)
    
    def test_circle_perimeter_positive(self):
        res = circle_perimeter(1)
        self.assertEqual(res, 2 * math.pi)
    
    def test_circle_perimeter_negative(self):
        res = circle_perimeter(-3)
        self.assertEqual(res, 2 * math.pi * -3)
    
    def test_circle_perimeter_float(self):
        res = circle_perimeter(2.5)
        self.assertEqual(res, 2 * math.pi * 2.5)
    
    def test_circle_perimeter_large_number(self):
        res = circle_perimeter(50)
        self.assertEqual(res, 2 * math.pi * 50)


class EdgeCaseTestCase(unittest.TestCase):
    
    def test_mixed_operations(self):
        square_result = square_area(5)
        circle_result = circle_area(5)
        triangle_result = triangle_area(5, 10)
        
        self.assertEqual(square_result, 25)
        self.assertEqual(circle_result, math.pi * 25)
        self.assertEqual(triangle_result, 25)
