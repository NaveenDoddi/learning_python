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

# for row in range(7):
#       for col in range(7):
#             if row == col or row+col == 7-1:
#                   print("*", end='')
#             else:
#                   print(' ', end='')

#       print()

# *     *
#  *   *
#   * *
#    *
#   * *
#  *   *
# *     *
# ----------------------------------------------------------------------------------------------------
import math
rows = int(input('enter rows: '))
colum = rows * 2 + 1

for row in range(rows):
      for col in range(colum):
            place = math.floor(colum/(row+2))
            # print()
            rev = colum - place
            if place == col or rev == col:
                  print('*', end='')
            else:
                  print(" ", end="")
      print()
