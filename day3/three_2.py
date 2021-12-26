

with open("C:\\Users\heber\Desktop\Advent_of_Code_2021\day3\data.txt", "r") as txt_file:
  data = txt_file.read().splitlines()


keep = []
count_uncommon = 0
count_common = 0
one_count = 0
zero_count = 0
counter = 0
size = len(data)


def find_common_bit(counter):
    global one_count
    global zero_count
    for i in range(len(data)):
        stri = data[i]
    
        # finding the common bit
        if stri[counter] == "1":
            one_count += 1
        else:
            zero_count += 1
    return one_count



def create_new_data(counter, data):
    #checking the common bit
    if one_count > len(data) / 2:
        for j in range(len(data)):
            ss = data[j]
            if ss[counter] == '1':
                keep.append(data[j])
    else:
        for j in range(len(data)):
            ss = data[j]
            if ss[counter] == '0':
                keep.append(data[j]) 
    return keep





print(counter)
print(data)
print(find_common_bit(counter))
data = create_new_data(counter, data)
print(counter)
print(data)
counter +=1
print()
print(find_common_bit(counter))
data = create_new_data(counter, data)
print(counter)
print(data)