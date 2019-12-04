import unittest
from main import draw
from main import distance

class TestStringMethods(unittest.TestCase):

    def test_0(self):
        self.assertEqual(
draw("R8,U5,L5,D3", ""),
"""
...+----+
...|....|
...|....|
...|....|
........|
o-------+
""")

    def test_1(self):
        data = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
        self.assertEqual(
distance(data[0], data[1]), 6)
        self.assertEqual(
draw(data[0], data[1]),
"""
+-----+..
|.....|..
|..+--X-+
|..|..|.|
|.-X--+.|
|..|....|
|.......|
o-------+
""")
    def test_2(self):
        data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
        self.assertEqual(
distance(data[0], data[1]), 159)
        draw(data[0], data[1])

def test_3(self):
        data = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
        self.assertEqual(
distance(data[0], data[1]), 135)
        draw(data[0], data[1])


if __name__ == '__main__':
    unittest.main()