import unittest
import calc

class Test_Calculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.sum(3,1), 4)

if __name__ == '__main__':
    unittest.main()