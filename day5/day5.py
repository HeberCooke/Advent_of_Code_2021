
# Parse the text file input
with open('data.txt', 'r') as file:
    all_data = []
    for i in file:
        line = file.readline().replace('->', ',').replace(' ','')
        line = [int(i) for i in line.split(',')]
        all_data.append( list(line))
        

    
    


#Test data
# data = [
#     [0,9,5,9],
#     [8,0,0,8],
#     [9,4,3,4],
#     [2,2,2,1],
#     [7,0,7,4],
#     [6,4,2,0],
#     [0,9,2,9],
#     [3,4,1,4],
#     [0,0,8,8],
#     [5,5,8,2],
# ]



def find_max(data):
    temp = 0
    for row in data:
        for col in row:
            if col > temp:
                temp = col
    return temp 

print(find_max(all_data))