# program to check wether input number is odd/even , prime ,palindrome ,armstrong.
def odd_even(num):
    if num%2==0:
        print("number is even")
    else:
        print( 'number is odd')
def is_prime(num):
    if num>1:
        for i in range(2,num//2):
            if (num%i)==0:
                print('number is not prime')
                # print(i,"times",num//i,'is'num)
                break
        else:
            print("number is prime")
    else:
        print("number is not prime")
def is_arm(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if num==sum:
        print("number is armstrong")
    else :
        print("number is not armstrong")

def is_pal(num):
    temp=num
    rev=0
    while num>0:
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if temp==rev:
        print("number is palindrome")
    else:
        print(" numer is not palindrome")
num=int(input("Enter a number "))
print(odd_even(num),is_prime(num),is_arm(num),is_pal(num))
