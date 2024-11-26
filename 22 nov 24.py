# inbuild function on the strings

# isalpa

# rtrip,
# ltrip,
# strip
# split,

# upper

# val = 'naveen'
# print(val.upper())
# print(val.lower())

# ordinal number
# it is used to fetch carecters to numbers
# asci value
# american standard code for international exchange

# char = 'A'
# print(ord(char))

# 'A' ==> 65
# 'a' ==> 97

# num = 97
# print(chr(97))

# chr is used to convert numbers to carecters


# to covert small to caps
# val = 'naveen'
# new = ""
# for i in val:
#       ele = chr(ord(i)-32)
#       # print(ele, end="")
      
# print(new)

# to covert caps to small
# val = 'NAVEEN'
# for i in val:
#       ele = chr(ord(i)+32)
#       print(ele, end="")


# ---------------------------------------------------------------------------------------------------------

# SWAPCASE()
# it is used to swap upper and lower cases of elements

# val = 'aBcD!'
# for i in val:
#       ord_val = ord(i)
#       if ord_val >= 65 and ord_val <=90:
#             print(chr(ord_val + 32), end='')
#       else:
#             print(chr(ord_val - 32), end='')
# output: AbCd☺

# --------------------------------------------------------------------------------------------------------------------

# qwiz application 
# it will retrun true or false. 

# print('answer the following question...')
# cap = input('enter capital of Karnataka: ').lower()
# if cap == "bengaluru" or cap == 'banglore':
#       print('correct answer')
# else:
#       print('wrong answer')
