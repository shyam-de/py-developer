# program to print half diamond number star pattern
num=int(input("enter a number"))

for i in range(num):


    print((str(num - i) + "*") * (num - 1 - i) + str(num - i))


for i in range(1,num + 1):


    print((str(i) + "*") * (i - 1) + str(i))
