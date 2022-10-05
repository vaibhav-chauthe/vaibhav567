# -*- coding: utf-8 -*-
"""


@author: vaibhav chauthe
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    

   

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Scalene','also a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Scalene','also a Right triangle')

    
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is a Equilateral')

    def test_all_sides_are_equal(self):
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 is a Equilateral triangle')

    def test_all_zero_sides_is_not_a_triangle(self):
        self.assertNotEqual(classifyTriangle(0,0,0),'Equilateral','Not a triangle')

    def test_third_triangle_inequality_violation(self):
        self.assertnotEqual(classifyTriangle(3,3,3),'Isosceles','Not an Isosceles')

    def test_sides_may_be_floats(self):
        self.assertEqual(classifyTriangle(0.5,0.5,0.5),'Equilateral','0.5,0.5,0.5 is a Equilateral triangle')

    def test_last_two_sides_are_equal(self):
        self.assertEqual(classifyTriangle(3,4,4),'Isosceles','3,4,4 is a Isosceles triangle')

   

    def test_equilateral_triangles_are_also_isosceles(self):
        self.assertEqual(classifyTriangle(4,4,4),'Equilateral','Also an Isosceles')

    def test_third_triangle_inequality_violation(self):
        self.assertNotEqual(classifyTriangle(3,1,1),'Isosceles','Not an Isosceles')
    
    def test_sides_may_be_floats(self):
        self.assertEqual(classifyTriangle(0.5,0.4,0.5),'Isosceles','0.5,0.4,0.5 is a Isosceles triangle')

    def test_no_sides_are_equal(self):
        self.assertEqual(classifyTriangle(5,4,6),'Scalene','5,4,6 is a Scalene triangle')

    def test_all_sides_are_equal(self):
        self.assertNotEqual(classifyTriangle(4,4,4),'Scalene','not a Scalene triangle')

    
    
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

