# SREINGS in python
# string is nothing but the collections carecters. it is represeted by single qoute'', double, triple"", double qoutes""""""
# the data type of the string is STR

# slicing and indexing

# INDEXING 
# it is used to extracting 1 element from the string or single carecter is called as INDEXING

# there are two types of indexing
# 1. positive indexing
# 2. negative indexing

# val = 'ARJUN'
# here: 'A'==> 0,'R'==> 1, 'J'==> 2, 'U'==> 3, 'N'==> 4
# here: 'A'==> -5,'R'==> -4, 'J'==> -3, 'U'==> -2, 'N'==> -1

# by using these values 
# we can get single elements like
# val[0] = A,
# val[1] = R,
# val[2] = J,
# val[3] = U,
# val[4] = N,
# val[-5] = A,
# val[-4] = R,
# val[-3] = J,
# val[-2] = U,
# val[-1] = N

# the entire string('arjun') is storing in val

# SLICING
# slicing is used to extract morethan one element.
# it is used to get the substrings
# there are two types of slicing
# 1. start, stop
# 2. start, stop, step


# to extract sita from ramasita
name = 'ramasita'
# print((name[4:8]))
# print((name[4:]))
# print((name[-4:]))
# print((name[-4:]))

# steping is used to skip the in between elements

# print(name[0: 8: 2])
#rmst

# if the values are not mentioned, then it always go with default values
# starting = 0
# stoping = length - 1


# print(name[::1])
# print(name[::-1])
# ramasita
# atisamar

# there is a word called madam' check the value palandrome or note
# paladrome = malayalam

name = 'madamy'
# if(name == name[::-1]):
#       print(name, ' is a polindrome')
# else:
#     print(name, ' is not a polindrome')

for i in range(len(name) -1, -1, -1):
      print(name[i])