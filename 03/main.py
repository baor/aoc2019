# task https://adventofcode.com/2019/day/1

import os
import operator
from enum import Enum, auto
from typing import Dict, List
import time
from datetime import datetime


dirname = os.path.dirname(__file__)


def getInput():
    with open(os.path.join(dirname, "input.txt"), "r") as f:
        data = []
        for line in f:
            data.append(line.strip())
        return data[0], data[1]


class PointType(Enum):
    EMPTY = "."
    VERTICAL = "|"
    HORIZONTAL = "-"
    START = "o"
    TURN = "+"
    CROSS = "X"


class CommandType(Enum):
    L = "L"
    R = "R"
    U = "U"
    D = "D"


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, another):
        return self.x == another.x and self.y == another.y

    def __hash__(self):
        return hash((self.x, self.y))

    def distanceFrom(self, another):
        return abs(self.x-another.x) + abs(self.y-another.y)


def commandToPoints(startPoint: Point, commandType: str, distance: int):
    dictPoints = dict()
    prevPoint = startPoint
    for i in range(0, distance):
        newPointType = PointType.EMPTY
        if commandType == CommandType.R.value:
            newPoint = Point(prevPoint.x+1, prevPoint.y)
            newPointType = PointType.HORIZONTAL
        elif commandType == CommandType.L.value:
            newPoint = Point(prevPoint.x-1, prevPoint.y)
            newPointType = PointType.HORIZONTAL
        elif commandType == CommandType.U.value:
            newPoint = Point(prevPoint.x, prevPoint.y+1)
            newPointType = PointType.VERTICAL
        elif commandType == CommandType.D.value:
            newPoint = Point(prevPoint.x, prevPoint.y-1)
            newPointType = PointType.VERTICAL
        else:
            print("Error! Unknown commandType: " + commandType)

        dictPoints[newPoint] = newPointType
        prevPoint = newPoint

    return dictPoints, newPoint


def commandsSetToPoints(commands1: List[str]) -> Dict[Point, PointType]:
    startPoint = Point(0, 0)
    dictPoints = {startPoint: PointType.START}
    for command in commands1:
        commandType = command[0]
        distance = int(command[1:])
        newPoints, lastPoint = commandToPoints(
            startPoint, commandType, distance)
        dictPoints.update(newPoints)

        if (dictPoints[startPoint] != PointType.START
                and dictPoints[startPoint] != newPoints[lastPoint]):
            dictPoints[startPoint] = PointType.TURN

        startPoint = lastPoint
    return dictPoints


def commandsToPoints(commands1: List[str], commands2: List[str]) -> (Dict[Point, PointType], Dict[Point, PointType]):

    dictPoints1 = commandsSetToPoints(commands1)
    dictPoints2 = commandsSetToPoints(commands2)

    for p1, p1Type in dictPoints1.items():
        if p1Type == PointType.START:
            continue

        if p1 in dictPoints2.keys():
            dictPoints1[p1] = PointType.CROSS
            dictPoints2[p1] = PointType.CROSS

    return dictPoints1, dictPoints2


def drawPoints(arg: (Dict[Point, PointType], Dict[Point, PointType])):
    dictPoints = arg[0]
    dictPoints.update(arg[1])

    keys = dictPoints.keys()
    maxX = max(p.x for p in keys)
    minX = min(p.x for p in keys)
    maxY = max(p.y for p in keys)
    minY = min(p.y for p in keys)

    output = ["\n"]
    for y in range(maxY, minY-1, -1):
        for x in range(minX, maxX+1, 1):
            p = Point(x, y)
            if p not in dictPoints:
                output.append(".")
            else:
                output.append(dictPoints[p].value)
        output.append("\n")
    resString = "".join(output)

    dateTimeObj = datetime.now()
    filename = str(dateTimeObj.hour) + str(dateTimeObj.minute) + str(dateTimeObj.second) + \
        str(dateTimeObj.microsecond) + "_" + str(len(dictPoints)) + ".txt"
    # f = open(filename, "w")
    # f.write(resString)
    # f.close()

    return resString


def draw(wire1, wire2):
    wire1split = wire1.split(",")
    if len(wire2) > 0:
        wire2split = wire2.split(",")
    else:
        wire2split = []
    return drawPoints(commandsToPoints(wire1split, wire2split))


def distance(wire1, wire2):
    wire1split = wire1.split(",")
    if len(wire2) > 0:
        wire2split = wire2.split(",")
    else:
        wire2split = []

    dictPoints, _ = commandsToPoints(wire1split, wire2split)
    crosses = [k for k, v in dictPoints.items() if v == PointType.CROSS]

    p0 = Point(0, 0)
    crossesAndDist = {p: p.distanceFrom(p0) for p in crosses}

    minDist = min(crossesAndDist.items(), key=operator.itemgetter(1))[1]
    return minDist


def findPath(startPoints: List[PointType], endPoint: PointType, trail: Dict[Point, PointType]):
    


def task1():
    wire1, wire2 = getInput()
    #draw(wire1, wire2)
    dist = distance(wire1, wire2)
    print("distance: " + str(dist))
    # answer: 721


if __name__ == '__main__':
    task1()
