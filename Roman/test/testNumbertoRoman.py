import unittest
from src.numbertoRoman import first_assignment_nr

class NumbertoRomanTest(unittest.TestCase):
    def setUp(self):
        self.classObj = first_assignment_nr()

    def test_converts_one(self):
        self.assertEquals(self.classObj.n2rmethod(1), "I")

    def test_converts_two(self):
        self.assertEquals(self.classObj.n2rmethod(2), "II")

    def test_converts_five(self):
        self.assertEquals(self.classObj.n2rmethod(5), "V")

    def test_converts_six(self):
        self.assertEquals(self.classObj.n2rmethod(6), "VI")

    def test_converts_four(self):
        self.assertEquals(self.classObj.n2rmethod(4), "IV")

    def test_converts_ten(self):
        self.assertEquals(self.classObj.n2rmethod(10), "X")

    def test_converts_nine(self):
        self.assertEquals(self.classObj.n2rmethod(9), "IX")

if __name__ == '__main__':
    unittest.main()
