from data import boards


# # test boards
# boards = [
#     [
#         [22, 13, 17, 11,  0],
#         [8,  2, 23,  4, 24],
#         [21,  9, 14, 16,  7],
#         [6, 10,  3, 18,  5],
#         [1, 12, 20, 15, 19]],
#     [
#         [3, 15, 0, 2, 22],
#         [9, 18, 13, 17, 5],
#         [19, 8,  7, 25, 23],
#         [20, 11, 10, 24,  4],
#         [14, 21, 16, 12,  6],
#     ],
#     [
#         [14, 21, 17, 24,  4],
#         [10, 16, 15,  9, 19],
#         [18,  8, 23, 26, 20],
#         [22, 11, 13,  6,  5],
#         [2,  0, 12,  3,  7],
#     ]
# ]
#print(boards)

# # test numbers
# directory = 'C:\\Users\heber\Desktop\Advent_of_Code_2021\day4\data.txt'
# with open(directory, 'r') as file:
#     data = file.read().split(',')

# # print(data)
# number_list = data
# # print(boards[0][:5])
number_list = [87,7,82,21,47,88,12,71,24,35,10,90,4,97,30,55,36,74,19,50,23,46,13,44,69,27,2,0,37,33,99,49,77,15,89,98,31,51,22,96,73,94,95,18,52,78,32,83,85,54,75,84,59,25,76,45,20,48,9,28,39,70,63,56,5,68,61,26,58,92,67,53,43,62,17,81,80,66,91,93,41,64,14,8,57,38,34,16,42,11,86,72,40,65,79,6,3,29,60,1]
# Setting False to the bingo list
bingo_list = [[[False for i in range(5)]for j in range(5)] for k in range(len(boards))]
# print(bingo_list[0][0])


def check_win():
    true_count = 0
    last_board_count = 0 
    for i in range(len(boards)):
        for j in range(5):
            true_count = 0
            for k in range(5):
                if bingo_list[i][j][k] == True:
                    true_count += 1
                    if true_count == 5:
                        last_board_count += 1
                        if last_board_count == len(boards) :

                            return True


def check_win_col():
    true_count = 0
    last_board_count = 0 
    for i in range(len(boards)):
        for j in range(5):
            true_count =0
            for k in range(5):
                if bingo_list[i][k][j] == True:
                    true_count += 1
                    if true_count == 5:
                        last_board_count += 1
                        if last_board_count == len(boards):
                            return True



def sum_unmarked_numbers(num):
    sum = 0
    for h in range(5):
        for i in range(0,5):
            #print('{}      {}'.format(boards[num][h][i],bingo_list[num][h][i]))
            if bingo_list[num][h][i] == False:
                
                sum += int(boards[num][h][i])

    return sum




    

called_number = 0
counter = 0
times = len(number_list)
breakout = False
for h in range(times):
    if not breakout:
        for i in range(0,len(boards)):
            if not breakout:
                for j in range(0,5):
                    if not breakout:
                        for k in range(0,5):
                            #print('number list  {}\nboard   {}'.format(boards[i][j][k],number_list[counter]))
                            #input()
                            if int(boards[i][j][k]) == int(number_list[counter]):
                                #print('MAtch-----')
                                bingo_list[i][j][k] = True
                                #print(bingo_list[i][j])
                                if check_win():
                                    print("WIN!!!!!!!------ROW-----------------")
                                    winning_board = int(i)
                                    #print("WINING NUM ", i)
                                    breakout = True
                                    called_number = int(number_list[counter])
                                    break
                                if check_win_col():
                                    print("WIN!!!!!!!------COL-----------------")
                                    winning_board = int(i)
                                    breakout = True
                                    called_number = int(number_list[counter])
                                    break
        counter += 1

print('Winning Board is ', winning_board)  

sum_unmarked_numbers(winning_board)
total = sum_unmarked_numbers(winning_board)
print("Sum --------  ", total)
print('Called Number ',called_number)
print('FINAL ANSWER IS ', total * called_number)


print(bingo_list[93])
print(boards[93])