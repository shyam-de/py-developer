# - Swap 2 Variables without using a third variable.
a,b=input("enter two number").split(",")
a=a+b
b=a-b
a=a-b
print(f"swap of number is  first : {a}\n secand : {b} ")