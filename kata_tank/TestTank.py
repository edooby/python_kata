'''
Created on 18 oct. 2012

@author: Edooby
'''
import unittest
from Tank import Tank

class TestTank(unittest.TestCase):
    def testTankHasImage(self):
        tank = Tank()
        
    def testTankHasRectangle(self):
        tank = Tank()
        assert tank.rect != None,
            "tank rectangle is None“


if __name__=="__main__":
    unittest.main()