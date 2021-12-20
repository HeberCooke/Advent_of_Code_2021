#!/usr/bin/python3

from typing import NewType


def main():
    INC = "Increased"
    DEC = "Decreased"
    count = 0
    newData = []
    #depthes = [199, 200, 208, 210, 200, 207, 240, 169, 260, 263]
    #newData= [199, 200, 208, 210, 200, 207, 240, 169, 260, 263]
    with open("/home/heber/Desktop/Advent_Of_Code/data.txt", "r") as myfile:

        depthes = myfile.read().splitlines()
        newData = [int(x) for x in depthes] 
    #print(newData)
    for i in range(len(newData)):
        if i > 0:         
            if newData[i- 1]  < newData[i]:
                print('%s %s' % (newData[i], INC))
                count += 1 
            else:
                print('%s %s' % (newData[i], DEC))
        else:
            print("NA", newData[i])
    print(count)


if __name__ == "__main__":
    main()
