
with open("C:\\Users\heber\Desktop\Advent_of_Code_2021\day3\data2.txt", "r") as txt_file:
  data = txt_file.read().splitlines()





one_count  = 0
zero_count = 0
count_position = 0

for i in range(len(data)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1


first_list = []                    
for i in range(len(data)):
    strings = data[i]
    if strings[count_position] == '1':
        first_list.append(data[i])

print(first_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0



# second iteration
for i in range(len(first_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
second_list = []                    
for i in range(len(first_list)):
    strings = data[i]
    if strings[count_position] == '1':
        second_list.append(first_list[i])

print(second_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# third iteration
for i in range(len(second_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
third_list = []                    
for i in range(len(second_list)):
    strings = data[i]
    if strings[count_position] == '0':
        third_list.append(second_list[i])

print(third_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# fourth iteration
for i in range(len(third_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
fourth_list = []                    
for i in range(len(third_list)):
    strings = data[i]
    if strings[count_position] == '1':
        fourth_list.append(third_list[i])

print(fourth_list)
print(one_count)
print(zero_count)


count_position += 1
one_count = 0
zero_count = 0

# fifth iteration
for i in range(len(fourth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
fifth_list = []                    
for i in range(len(fourth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        fifth_list.append(fourth_list[i])

print(fifth_list)
print(one_count)
print(zero_count)


count_position += 1
one_count = 0
zero_count = 0

# sixth iteration
for i in range(len(fifth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
sixth_list = []                    
for i in range(len(fifth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        sixth_list.append(fifth_list[i])

print(sixth_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# seventh iteration
for i in range(len(sixth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
seventh_list = []                    
for i in range(len(sixth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        seventh_list.append(sixth_list[i])

print(seventh_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# eighth iteration
for i in range(len(seventh_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
eighth_list = []                    
for i in range(len(seventh_list)):
    strings = data[i]
    if strings[count_position] == '1':
        eighth_list.append(seventh_list[i])

print(eighth_list)
print(one_count)
print(zero_count)



count_position += 1
one_count = 0
zero_count = 0

# ninth iteration
for i in range(len(eighth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
ninth_list = []                    
for i in range(len(eighth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        ninth_list.append(eighth_list[i])

print(ninth_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# tenth iteration
for i in range(len(ninth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
tenth_list = []                    
for i in range(len(ninth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        tenth_list.append(ninth_list[i])

print(tenth_list)
print(one_count)
print(zero_count)

count_position += 1
one_count = 0
zero_count = 0

# eloeventh iteration
for i in range(len(tenth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        one_count += 1
    else:
        zero_count += 1
eleventh_list = []                    
for i in range(len(tenth_list)):
    strings = data[i]
    if strings[count_position] == '1':
        eleventh_list.append(tenth_list[i])

print(eleventh_list)
print(one_count)
print(zero_count)