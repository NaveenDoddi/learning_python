
# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

obj = {
      'name' : 'naveen',
      "age" : 21,
      "school" : "st joseph public school",
      "palce" : "atp"
}

# print(obj.keys())
# print(obj.values())
# print(len(obj.values()))

# for i in obj.items():
#       print(i[0], i[1])

# for i in obj.keys():
#       print(i)
      
# for i in obj.values():
#       print(i)

# obj.update({'age': 31})
# print(obj.get('age'))
# obj["age"] = 32
# print(obj["age"])

obj.clear()
print(obj)
