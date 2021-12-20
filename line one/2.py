#!/usr/bin/python3   
INC = "Increased"
DEC = "Decreased"
NO = "No Change"
count = 0
   
def increase_or_decrease(newData):
    global count
    for i in range(len(newData)):
        if i > 0:  
            if newData[i - 1] == newData[i]:
                print("%s %s" % (newData[i],NO))       
            elif newData[i- 1]  < newData[i]:
                print('%s %s' % (newData[i], INC))
                count += 1 
        else:
            print('%s %s' % (newData[i], DEC))
    else:
        print("NA", newData[i])
    print("Count ",count) 
   
   
with open("/home/heber/Desktop/Advent_Of_Code/data.txt", "r") as myfile:
    depthes = myfile.read().splitlines()
    newData = [int(x) for x in depthes]  
   
#newData= [199, 200, 208, 210, 200, 207, 240, 169, 260, 263]

first_Count = 0
one = 0
two = 0
three = 0
total = 0
totalList = []

for i in range(len(newData)):
    if  i < (len(newData) - 2):
        one = newData[i]
        #print(one, " one")
        two = newData[i + 1]
        #print(two, " two")
        three = newData[i + 2]
        #print(three , " three")
        total = (one + two + three)
        #print(total)
        totalList.append(total)

#print(totalList)
increase_or_decrease(totalList)