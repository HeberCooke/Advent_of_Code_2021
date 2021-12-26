

def open_file(path ='C:\\Users\heber\Desktop\Advent_of_Code_2021\day3\data2.txt'):
    
    with open(path, "r") as txt_file:
        data = txt_file.read().splitlines()
    return data



data = open_file()

data_length = len(data)
position = 0


#Step 1: find the common bit at 
def find_bit(data, position):
    ones = 0
    zeros = 0
    for i in range(len(data)):
        data_element = data[i]
        if data_element[position] =='1':
            ones += 1
        else:
            zeros += 1
    return ones,zeros

#Step 2: If ones is greater add elements to a new list
def add_to_list(data, position,ones_greater):
    new_list =[]
    if ones_greater:
        for element in data:
            if element[position] =='1':
                new_list.append(element)
    else:
        for element in data:
            if element[position] =='0':
                new_list.append(element)
    return new_list






# main loop
main_counter = len(data)
print(data)
oxygen_generator_rating = ''
co2_scrubber_rating = ''
# loop for oxygen generator rating
while len(data) > 0:
    if position > 11 or len(data) == 1:
        print('------------')
        oxygen_generator_rating = data[0]
        break
    ones,zeros = find_bit(data, position)

    print('Position ',position)
    print('ones ', ones)
    print('zeros ', zeros)
    
    if ones >= zeros:
        data = add_to_list(data,position,True) #False to switch to CO2 rating
    else:
        data = add_to_list(data, position, False)# True to switch to Co2 rating
    print(data)
    
    position += 1
    

print('oxygen_generator_rating --> ',oxygen_generator_rating)
print(int(oxygen_generator_rating,2))
