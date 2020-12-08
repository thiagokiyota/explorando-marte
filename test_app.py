import numpy as np
import unittest
from app import base, rotate

class TestBase(unittest.TestCase):
    def test_base(self):
        a = base(5, 5)
        b = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.assertEqual(a.shape, b.shape)

class TestRotate(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(rotate('N', 'L'), 'W')
        self.assertEqual(rotate('E', 'L'), 'N')
        self.assertEqual(rotate('S', 'L'), 'E')
        self.assertEqual(rotate('W', 'L'), 'S')
        self.assertEqual(rotate('N', 'R'), 'E')
        self.assertEqual(rotate('E', 'R'), 'S')
        self.assertEqual(rotate('S', 'R'), 'W')
        self.assertEqual(rotate('W', 'R'), 'N')

if __name__ == '__main__':
    unittest.main()
