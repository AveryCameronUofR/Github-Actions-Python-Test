import unittest
import githubActions
class TestApp(unittest.TestCase):
    def test(self):
        self.assertEqual(githubActions.addOne(3), 4)

    def testEven(self):
        self.assertEqual(githubActions.makeEven(6), 6)

    def testEven4(self):
        self.assertEqual(githubActions.makeEven(4), 4)   

def suite():
    suite = unittest.TestSuite()
    suite.addTests(
        unittest.TestLoader().loadTestsFromTestCase(TestApp)
    )
    return suite

if __name__ == '__main__':
   unittest.TextTestRunner(verbosity=2).run(suite())