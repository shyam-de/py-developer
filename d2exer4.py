n = int(input("Enter the value of rows: "))

#upper part of pattern
for i in range(n):
    print("* " * (n - i) +"    " * i +" *" * (n - i))

# lowe part of pattern
for i in range(1,n + 1):
    print("* " * i +"    " * (n - i) +" *" * i)