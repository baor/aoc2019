import unittest

from main import getFuelForModule
from main import getFuelForModuleAndFuel

class TestStringMethods(unittest.TestCase):

    def test_getFuelForModule(self):
        self.assertEqual(getFuelForModule(12), 2)
        self.assertEqual(getFuelForModule(14), 2)
        self.assertEqual(getFuelForModule(1969), 654)
        self.assertEqual(getFuelForModule(100756), 33583)
    
    def test_getFuelForModuleAndFuel(self):
        self.assertEqual(getFuelForModuleAndFuel(14), 2)
        self.assertEqual(getFuelForModuleAndFuel(1969), 966)
        self.assertEqual(getFuelForModuleAndFuel(100756), 50346)

if __name__ == '__main__':
    unittest.main()