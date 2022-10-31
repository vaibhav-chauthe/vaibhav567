# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(_1,_2,_3):
    """
    Your correct code goes here... Fix the faulty logic below until the code passes all of
     you test cases.
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if _1 > 200 or _2 > 200 or _3 > 200:
        return 'InvalidInput'

    if _1 <= 0 or _2 <= 0 or _3 <= 0:
        return 'InvalidInput'

    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(_1,(int,float)) and isinstance(_2,(int,float)) and isinstance(_3,(int,float))):
        return 'InvalidInput'
    if (_1 <= (_2 - _3)) or (_2 <= (_1 - _3)) or (_3 <= (_1 - _2)):
        return 'NotATriangle'

    if _1 == _2 and _2 == _1:
        return 'Equilateral'
    if _1==_2 or _2==_3 or _3==_1:
        return 'Isosceles'
    if ((_1 * 2)+(_2 * 2))==(_3 * 2)or((_2 * 2)+(_3 * 2))==(_1 * 2)or((_3 * 2)+(_1 * 2))==(_2 * 2):
        return 'Right'

    return 'Scalene'
