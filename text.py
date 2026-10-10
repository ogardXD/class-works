import unittest
import u3

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(u3.division(15,5), 3)

    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            u3.division(10,0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            u3.division("5",5)

    def test_type_none(self):
        with self.assertRaises(TypeError):
            u3.division(None, 5)

if __name__ == "__main__":
    unittest.main()