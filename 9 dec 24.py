# tupples in python
# tupple is nothing but heterogeinous immutable values.
# tuppel is represented by simple parathansesis()
# properties of tupples 
# 1. tupples heterogenious values(mutli datatypes)
# 2. immutable
# 3. output is ordered
# 4. slicing and indexing can be possible

# these are the ways to define tupples
# a = 10, 20 , 30, 40
# print(a)
# print(type(a))
# //<class 'tuple'>


# b = ('10')
# print(type(b))
# //<class 'str'>


# c = (10,)
# print(type(c))
# // <class 'tuple'>

# a = (1,2,3, 'rama', 'rama')
# count = 0
# for i in a:
#       if i == "rama":
#             count += 1
# print(count)
# val = input()
# print(len(tuple([x for x in (1,2,3, 'rama', 'rama') if str(x) == val])))
# here we are converting a list into tuple and finding the length of that tuple
# import sys
# a = (1,2,3, 'rama', 'rama')
# print(sys.getsizeof(a))
# // 80

# a1 = [1,2,3, 'rama', 'rama']
# print(sys.getsizeof(a1))
# // 104

# by comparing with list and tupple, tuple consumes less storage volume 
n = 10
a, b = 0, 1
sum = 0
for _ in range(n):
    print(sum, end=" ")
    sum = a + b
    a = a + b
    b = a
#     a, b = b, a + b
