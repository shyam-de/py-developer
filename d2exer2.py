# to print fibonacci series upto nth numbber
def fibo(num):
    a=0
    b=1
    sum=0
    count=1
    if num<=0:
        print("incorrect input ")
    elif num==1:
        return a
    elif num==2:
        return a,b
    else:
        while count<=num:
            print(sum,end=" ")
            count+=1
            a=b
            b=sum
            sum=a+b

num=int(input("enter a number for fibonacci series"))
print(fibo(num))
