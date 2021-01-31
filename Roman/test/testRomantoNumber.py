import unittest
from Roman.src.romantoNumber import first_assignment_rn

class NumbertoRomanTest(unittest.TestCase):
    def setUp(self):
        self.classObj = first_assignment_rn()

    def test_converts_one(self):
        self.assertEquals(self.classObj.r2nmethod("I"),1)

    def test_converts_two(self):
        self.assertEquals(self.classObj.r2nmethod("II"), 2)

    def test_converts_five(self):
        self.assertEquals(self.classObj.r2nmethod("V"), 5)

    def test_converts_six(self):
        self.assertEquals(self.classObj.r2nmethod("VI"),6 )

    def test_converts_four(self):
        self.assertEquals(self.classObj.r2nmethod("IV"), 4)

    def test_converts_ten(self):
        self.assertEquals(self.classObj.r2nmethod( "X"),10)

    def test_converts_nine(self):
        self.assertEquals(self.classObj.r2nmethod("IX"), 9)

if __name__ == '__main__':
    unittest.main()
