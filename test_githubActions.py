import unittest
import githubActions

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(githubActions.addOne(3), 4)

    def testEven(self):
        self.assertEqual(githubActions.makeEven(6), 6)