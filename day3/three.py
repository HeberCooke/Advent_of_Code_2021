


with open("C:\\Users\heber\Desktop\Advent_of_Code_2021\day3\data2.txt", "r") as txt_file:
  data = txt_file.read().splitlines()


pos1 =0
pos2 =0
pos3 =0
pos4 =0
pos5 =0
pos6 =0
pos7 =0
pos8 =0
pos9 =0
pos10 =0
pos11 =0
pos12 =0

Npos1 =0
Npos2 =0
Npos3 =0
Npos4 =0
Npos5 =0
Npos6 =0
Npos7 =0
Npos8 =0
Npos9 =0
Npos10 =0
Npos11 =0
Npos12 =0

oxygen_generator_rating_common = []
oxygen_generator_rating_Non_common = []
for i in data:
   
    if i[0] == '1':
        pos1 += 1
        oxygen_generator_rating_common.append(i)
    else:
        Npos1 += 1
        oxygen_generator_rating_Non_common.append(i)
    if i[1] == '1':
        pos2 += 1
    else:
        Npos2 += 1       

    if i[2] == '1':
        pos3 += 1
    else:
        Npos3 += 1

    if i[3] == '1':
        pos4 += 1
    else:
        Npos4 += 1

    if i[4] == '1':
        pos5 += 1
    else:
        Npos5 += 1

    if i[5] == '1':
        pos6 += 1
    else:
        Npos6 += 1

    if i[6] == '1':
        pos7 += 1
    else:
        Npos7 += 1

    if i[7] == '1':
        pos8 += 1
    else:
        Npos8 += 1

    if i[8] == '1':
        pos9 += 1
    else:
        Npos9 += 1

    if i[9] == '1':
        pos10 += 1
    else:
        Npos10 += 1
        
    if i[10] == '1':
        pos11 += 1
    else:
        Npos11 += 1

    if i[11] == '1':
        pos12 += 1
    else:
        Npos12 += 1

#print("data / 2 " ,len(data) /2)

uncommon =[]
common = []

length = len(data) / 2



if pos1 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos2 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos3 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos4 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos5 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos6 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')
    
if pos7 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos8 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos9 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos10 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos11 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')

if pos12 > length:
    common.append('1')
    uncommon.append('0')
else:
    common.append('0')
    uncommon.append('1')




print('Uncommon ', uncommon)
print('Common ', common)

uncommon = ''.join(uncommon)
common = ''.join(common)

print(int(common,2)* int(uncommon,2))
    
print(Npos12)