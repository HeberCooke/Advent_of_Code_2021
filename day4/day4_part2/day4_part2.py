
def open_file():
    directory = 'C:\\Users\heber\Desktop\Advent_of_Code_2021\day4\day4_part2\data.txt'
    with open(directory, 'r') as file:
        numbers, *boards = file.read().split('\n\n')
        numbers = [int(i) for i in numbers.split(',')]
        all_boards = [[[int(col) for col in row.split()] for row in board.split('\n')]for board in boards]

    return numbers, all_boards



def print_board():
    n,all_boards = open_file()
    for board in all_boards:
        for row in board:
            print(row)
        print()


#####################################################################################################

def mark_board(number, board):
    for row in board:
        for col in range(0, len(row)) :
            if row[col] == number:
                row[col] = 'x'

def sum_board(board):
    sum = 0
    for row in board:
        for col in row:
            if col != 'x':
                sum += col

    return sum


def check_for_winner(board):
    winner = False

    for row in board:
        winner = all(elem in ['x'] for elem in row)

        if winner:
            return winner

    for col in range(0,5):
        winner = all(elem in ['x'] for elem in [row[col] for row in board]) 

        if winner:
            return winner



def part2():
    all_numbers,all_boards = open_file()

    winner = False

    while not winner:
        number = all_numbers[0]
        all_numbers = all_numbers[1:]

        for board in all_boards:
            mark_board(number, board)

        index = 0 
        while index < len(all_boards):
            if check_for_winner(all_boards[index]):
                if len(all_boards) > 1:
                    all_boards.pop(index)

                else:
                    winner = True
                    return sum_board(all_boards[index]) * number

            else:
                index += 1


print(part2())