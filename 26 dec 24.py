# Methods 
# Methods in objects are functions that belong to the object.
# (function in objects are called methods)
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()


# Isinstance variable
# # types of variables
# memory segments

# isinstance,
# stack segment, 
# statice segment 
# global segment 
# core segment

#       ----------------------------

#                               global
#                               -------
#                               heap
#                               -----
#       code segment            stack
#                               -------
#                               static
#                               -------


#       ----------------------------

# isinstance variable declraded under heap session 
# and declared under initialisation method is called as isinstance variable
# note: in python any variable we need to declare we need a method 
# methods are function are similar but method used under class and functions are indipendante block

# intialisation method it will decalre atomatically
#                         or 
# we declare manually to create or declare isinstance variable 
# instialisation method which is used to intiallise the program


# self
# self is the word which is used for to carry the address of the object
        

# class Facebook:
#        def __init__(self):
#             self.Followers : 1000
#             self.likes : 100
#       def search(self):
#         pass
#       def messaginf(self):
#         pass

# f1 = Facebook()



class laptop:
      def __init__(self):
            self.nooflaptops = 20
            self.price = 30
            # print(id(self))
dell = laptop()
realme = laptop()
print(id(dell))
print(id(realme))


# here id of self and id of dell is same and equal
# referecnce and isinstance(self) both are same, but
# self is used for internalll comunication 
# and Reference is used for outer communication


# Local variables
# variables is declared under method without self word is callled as local variables



# methods are set of instuctions it will activate when its called
# and it declared class only, it canot as a indipendandle block

# we are just assigning that class to ReferenceVariable and from that we are accesssing the that class


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# p1 = Person("John", 36)
# p1.myfunc()
