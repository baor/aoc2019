# task https://adventofcode.com/2019/day/1

import os
dirname = os.path.dirname(__file__)


def getInput():
    with open(os.path.join(dirname, "input.txt"), "r") as f:
        data = f.read()
        data = data.split(",")
        data = list(map(int, data))
        return data


def executeIntcodeAsText(text):
    data = text.split(",")
    data = list(map(int, data))
    res = executeIntcodeAsArray(data.copy())
    return ",".join(list(map(str, res)))


def executeIntcodeAsArray(data):
    for current_index in range(0, len(data), 4):
        # print(data)
        opcode = data[current_index]
        if opcode == 99:
            return data

        pos1 = data[current_index+1]
        pos2 = data[current_index+2]
        pos3 = data[current_index+3]

        if opcode == 1:
            data[pos3] = data[pos1] + data[pos2]
            continue
        if opcode == 2:
            data[pos3] = data[pos1] * data[pos2]
            continue

    print("Unknown opcode " + opcode)
    return "Error"


def task1():
    # task1
    data = getInput()
    data[1] = 12
    data[2] = 2
    res = executeIntcodeAsArray(data.copy())
    print("value at position 0: " + str(res[0]))
    # res: 12490719


def task2():
    # task2
    data_origin = getInput()
    for noun in range(0, 99):
        for verb in range(0, 99):
            data = data_origin.copy()
            data[1] = noun
            data[2] = verb
            res = executeIntcodeAsArray(data)
            print("value at position 0: {}. noun: {}, verb {}".format(
                str(res[0]), noun, verb))
            if res[0] == 19690720:
                print("answer:", str(100*noun+verb))
                return

    # res: 12490719


if __name__ == '__main__':
    task2()
