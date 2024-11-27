# IN operator
# in operator is used to check values are present or not in the main string

# val = 'naveen'
# vowels = 'aeiou'
# for i in val:
#       if i in vowels:
#             print(i, 'vowels')
#       if i not in vowels:
#             print(i, 'consonants')


# split 
# split is the inbuild function which is used to convert larger sentence in smaller words by using the reference of 
# all special carecters

# note: split will work on space by default

# sen = 'the king to back to his terotory'
# spt = sen.split()
# print(spt)
# for i in spt:
#       print(len(i), end=',')

sen = 'the king to back to his terotory'
# spt = sen.split('o')
# print(spt)
# for i in spt:
#       print(len(i), end=',')

# for i in sen:
#       spt = ''
#       if i ==" ":
#             pass
#       else:
#             spt = spt + i


# to split the sentence uisng slice into smaller words
# prev = 0
# def spliting(sen):
#       res = []
#       for i in range(len(sen)):
#             if sen[i] == " ":
#                   res.append(sen[prev:i])
#                   print(sen[prev:i])
#                   prev = i+1
#       print(res)
#       return res

# spliting()
# typecast
# type casting form one datatype to another datatype is called as typecast

# str1 = '990 123 44'
# spt = spliting(str1)
# for i in spt:
#       res = 1
#       for j in i:
#             res *= int(j)
#       print(res)

