n = int(input("Enter the value of rows: "))

#upper part of pattern
for i in range(n):

    print(" " * i + "*" + "  " * (n - 1 - i) + "*")

# lower part of pattern
for i in range(n):

    print(" " * (n - 1 - i) + "*" + "  " * i + "*")