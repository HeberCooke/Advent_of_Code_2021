#!/usr/bin/python3

from typing import Match


position_Horizontal = 0
position_depth = 0

# Test DATA
#data = ['forward 5','down 5','forward 8', 'up 3', 'down 8', 'forward 2']


def open_file():
    global data
    with open("/home/heber/Desktop/Advent_of_Code_2021/line_two/data.txt", "r") as myfile:
        return myfile.read().splitlines()

def split_data(data):
    comand = ''
    amount = ''
    horiz = 0
    depth = 0
    aim = 0


    for i in data:
        comand,amount = i.split(' ')
        if comand == 'forward':
            horiz += int(amount)
            depth += (aim * int(amount))
            print('forward ', int(amount))
            print('aim ', aim)
            print('depth ', depth)
        elif comand == 'down':
            aim += int(amount)
        elif comand == 'up':
            aim -= int(amount)

    print('Horizontal ', horiz)
    print('depth ', depth)
    print(horiz * depth)


data = open_file()

split_data(data)

