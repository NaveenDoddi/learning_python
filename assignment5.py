# 1.Write a Python program to print the following right-angle triangle pattern:
# 1
# 12
# 123
# 1234
# 12345
for row in range(5):
    for col in range(row+1):
        print(col+1, end='')
    print()

# ----------------------------------------------------------------------------------------------------------

# 2.Write a Python program to print the following inverted pyramid of numbers:
# 54321
# 4321
# 321
# 21
# 1
for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col, end='')
    print()

# ----------------------------------------------------------------------------------------------------------

# 3.Write a Python program to print the following diamond pattern:
#   *
#  ***
# *****
#  ***
#   *




# 5.Write a Python program to print the following pattern using alphabets:
# A
# AB
# ABC
# ABCD
# ABCDE
for row in range(5):
    for col in range(row+1):
        print(chr(65+col), end='')
    print()

# ----------------------------------------------------------------------------------------------------------

# 7.Write a Python program to print Floyd's triangle for 5 rows:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
num=1
for row in range(1,6):
    for col in range(1,row+1):
        print(num,end=" ")
        num+=1
    print()

# ----------------------------------------------------------------------------------------------------------

# 9.Write a Python program to print the following pattern:
# 1
# 22
# 333
# 4444
# 55555
num=1
for row in range(1,6):
    for col in range(1,row+1):
        print(num,end="")
    num+=1
    print()

# ----------------------------------------------------------------------------------------------------------

# 10.Write a Python program to print the following reverse pyramid pattern:
# 54321
# 4321
# 321
# 21
# 1

for row in range(5,0,-1):
    for col in range(row,0,-1):
        print(col, end='')
    print()