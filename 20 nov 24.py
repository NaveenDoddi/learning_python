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


# n = 0
# for row in range(10):
#       if row <= 5:
#             pass
#       else:
#             n = n - 2
#       for col in range(row+n):
#             print('*', end='')
#       print()

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# ----------------------------------------------------------------------------------------------------

for row in range(7):
      for col in range(7):
            if row == col:
                  print("* ", end='')
            else:
                  print(' ', end='')

      for col in range(7,0,-1):
            if row == col:
                  print("* ", end='')
            else:
                  print(' ', end='')

      print()

# for row in range(7):
#       for col in range(7, 0, -1):
#             print("*", end='')
#       print()