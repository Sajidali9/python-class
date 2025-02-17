#sting
#integer
#boolean
#list

#list

names = "asif ali"
#                      0           1               2               3              4  
names: list[str] = ["asif ali","sajid ali","mushahid hussain","kaiser abbas","muntazir mehdi"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
 
name = ["asif ali","sajid ali","mushahid hussain","kaiser abbas","muntazir mehdi"]
print(names)
 #range


print(range(5))
res = range(1,5)
#starting point
#condition
#increment

 #loop

numbers: list[int] = [1 , 2 ,3 , 4 , 5]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

#for varible in interable:

num = numbers[0] > 1
num = numbers[1] > 2
#for n in numbers:
print("n0 is,n1")


numbers = (1,2,3,4,5,6,7,8,9,10)
print("Aam zindagi")
print(numbers[0])
print(numbers[1])
print(numbers[3])
print(numbers[4])


print("mintos zindagi")
for num in numbers:
    print(num)

print("marksheet")





#assigment

#table of 4

print("table of four")

for i in range(1,11):
    print("4 x",i,"=",i*4)

#table of 9

print("table of   nine")

for i in range(1,11):
    print("9 x",i,"=",i*9)

#table of 17
for i in range(1,11):
    print("33x",i,"=",i*33)

#range function / method

x = range(5)

print(1,5) # 1 ,2 ,3 ,4

# table of aam zindagi

for num in range(1,11,1): # 1, 2, 3, 4, . . . . .10
    print("num is", num)        #indentation

# table of 2
for i in range(1,11):
   print(f"2 x {num} =2 *{2 * num}") # f string ha...

 #loop
 #for loop
#while loop

num = 1
while  num <= 10:
    print(num)
    num =num + 1 
    
    start = 1
    while start<=10:
        print(f"count {start}")
        start=start +1 #start ki phli value ma add kr do

#while loop






#tupple
numbers = [1, 2, 3, 4]
#          0     ,  `1      ,2      ,    3`
names1= ["asif", "sajid" , "mushahid" , "aqib"]
names2 = ("asif", "sajid" , "mushahid" , "aqib")

print("list first name is" , names1[0])
print("tuple first name is",names2[0])
