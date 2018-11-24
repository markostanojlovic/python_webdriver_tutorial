import unittest
from testAll import TestLogin
from testAll import TestAdmin

def suite():
    suite = unittest.TestSuite()
    # Login page tests
    suite.addTest(TestLogin('test_TC_L_001'))
    suite.addTest(TestLogin('test_TC_L_002'))
    suite.addTest(TestLogin('test_TC_L_003'))
    # Admin section tests 
    suite.addTest(TestAdmin('test_TC_A_001'))
    suite.addTest(TestAdmin('test_TC_A_002'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    runner.run(suite)