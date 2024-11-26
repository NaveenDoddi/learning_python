# home work
# unicode 
# difference between unicode and ascii values
# study on converting ascii values to binary values
# create emojis with help of unicode and ascii values
# get the copy chip for ascii values


# isalpha 
# isalpha is used to check the string is having alphabets or not
# isnumeric
# it is used to check the string is having numbrs ot not
# isalnum
# it is used to check wheather having alphabets and numbers

# val = 'abc'
# print(val.isalpha())
# val = '123'
# print(val.isnumeric())
# val = 'abc123'
# print(val.isalnum())
# val = 'Sfs'
# print(val.istitle())

# True
# True
# True
# True


# counter values
# val = 'naveen'
# length = 0
# for i in val:
#       # length = length + 1
#       length += 1
#       print(i, length)
# print('total length of',val ,'is',length)


# password policy should have the length between 8 - 13  charecters
# aplhabets should atleast 4 
# numbers should be atleast 3
# special should be atleast 1


password = input('enter passsword: ')

alpha = 0
numeric = 0
spl = 0

if len(password) >= 8 and len(password) <= 13:
      for i in password: 
            if i.isalpha():
                  alpha += 1
            elif i.isnumeric():
                  numeric =+ 1
            else:
                  spl =+ 1
      
      if(alpha >= 4 and numeric >= 3 and spl >= 1):
            print('passwrod accepted.')

      if(alpha < 4):
            print('passwrod invalid:  alphabets in password cantians less than 4')
      
      if(numeric < 3):
            print('passwrod invalid:  numbers in password cantians less than 3')
      
      if spl < 1:
            print('passwrod invalid:  special in password cantians less than 1')

else:
      print('passwrod lenght is not matched')