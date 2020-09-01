import unittest

import Closest
#[JOHN BONANNO]
class Test(unittest.TestCase):
    def testClosest(self):
        print("test1:")
        self.assertEqual(Closest.closest_pair([5,10]),[5,10])
        # sequence of size 0
        print("test2:")
        self.assertEqual(Closest.closest_pair([-1,5,-10,-11]),[-11,-10])
        print("test3:")
        self.assertEqual(Closest.closest_pair([-13, 5, 18, 7, -14, 21]),[-13,-14])
        print("test4:")
        self.assertEqual(Closest.closest_pair([-13, 5, 18, 7, -14, 21,-13]),[-13,-13])