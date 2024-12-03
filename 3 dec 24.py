# inbuild function of list 
# append
# insert
# extend
# sort
# delete
# remove
# shallow copy
# deep copy

# Append
# it is used to adding a value to the last position of the list
# arr = [1,2,3,4]
# arr.append(5)
# print(arr)
# [1, 2, 3, 4, 5]

# exxtend
# it is used for dumping more than one value to the last position of the list is called extend
# arr1 = [1,2,3,4]
# arr2 = [6, 7,8]
# arr1.append(5)
# arr1.extend(arr2)
# print(arr1)
# [1, 2, 3, 4, 5, 6, 7, 8]

# insert
# it is used for to insert a value at a particular position
# it not replaced the previous value
# array1 = [1,2,5,4]
# array1.insert(2,3)
# print(array1)
# [1, 2, 3, 5, 4]

# import copy
# # shallow copy and deep copy
# val = [1,2,3,4]
# val1 = copy.deepcopy(val)
# val1[1] = 10
# print(val1)
# print(val)

# sort 
# it the function which is used to arrange the elements in list from asc or desc
# arr1 = [1,2,3,4]
# arr1.sort()
# print(arr1)

# arr1.sort(reverse = True)
# print(arr1)

# swaping of two values
# a,b = 'a', 'b'
# a,b = b,a
# print(a)


# ascending order without inbuild function
arr = [44,2,4,6,21,5,1]
for i in range(len(arr)):
      for j in range(len(arr)):
            if arr[i] < arr[j]:
                  arr[i], arr[j] = arr[j], arr[i]

print(arr)


