# In the range of 10 extract only it odd numbers
# pass is the keyword which is used to ignore the entire condition.

# for i in range(10):
#       if(i % 2 != 0):
#             print(i)

# for i in range(10):
#       if(i % 2 == 0):
#             pass
#       else:
#             print(i)

# for i in range(1, 10, 2):
#       print(i)


# ptint the numbers in the range 50 it should be sum of 9. ex: 1+8=9, 27

# for i in range(9, 50, 9):
#       print(i)


# for i in range(50):
#       leter = str(i)
#       sum = 0
#       for j in leter:
#             sum += int(j)
#       if(sum == 9):
#             print(i)


# nested for loop
#  the loop inside another loop is called nested for loop

# for i in 'Raja':
#       for j in 'Rani':
#             print(i, j , end=' ,')      
#       print()


# PATTERN programming
#  outer loop is for rows and inner loop is for coloumns

# for row in range(5):
#       for col in range(5):
#             print('*', end='')
#       print()
# *****
# *****
# *****
# *****
# *****
# ----------------------------------------------------------------------------------------------------

# for row in range(5):
#       for col in range(row+1):
#             print('*', end='')
#       print()
# *
# **
# ***
# ****
# *****
# ----------------------------------------------------------------------------------------------------

# for row in range(5):
#       for col in range(5-row):
#             print('*', end='')
#       print()
# *****
# ****
# ***
# **
# *
# ----------------------------------------------------------------------------------------------------
