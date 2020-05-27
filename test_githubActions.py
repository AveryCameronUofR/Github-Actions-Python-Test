import pytest
import githubActions
class TestClass:
    def test_one(self):
        assert githubActions.addOne(3) == 4

    def testEven(self):
        assert githubActions.makeEven(6) == 6
