# task https://adventofcode.com/2019/day/1

import os
dirname = os.path.dirname(__file__)


def getFuelForModule(mass):
    return int(mass/3) - 2


def getFuelForAllModules():
    totalFuel = 0
    with open(os.path.join(dirname, "input.txt"), "r") as f:
        for line in f:
            totalFuel += getFuelForModule(int(line))
    print("totalFuel:"+str(totalFuel))


def getFuelForModuleAndFuel(mass):
    fuel = int(mass/3) - 2
    if fuel <= 0:
        return 0
    fuel += getFuelForModuleAndFuel(fuel)
    return fuel

def getFuelForAllModulesWithFuel():
    totalFuel = 0
    with open(os.path.join(dirname, "input.txt"), "r") as f:
        for line in f:
            totalFuel += getFuelForModuleAndFuel(int(line))
    print("totalFuel:"+str(totalFuel))



if __name__ == '__main__':
    # task1
    # getFuelForAllModules()
    #res: 3373568

    getFuelForAllModulesWithFuel()
    # res: 3373568
