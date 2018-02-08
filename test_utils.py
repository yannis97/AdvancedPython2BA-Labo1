# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        if fact(3) == 6:
            return True
        pass
    
    def test_roots(self):
        if roots(1,1,0)== (0,-1):
            return True
        # À compléter...
        pass
    
    def test_integrate(self):
        if integrate('2',0,2) == 4:
            return True
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
