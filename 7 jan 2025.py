# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks
# finally is uded for normal excution of the program


# def validate(value):
#       try:
#             if len(value) == 10:
#                   print('mobile number is validate')
#             else:
#                   raise ValueError
#       except ValueError:
#             print(' catch error')
      
# def main():
#       mob = 1243334
#       validate(mob)

# main()


# def menu(item):
#       try:      
#             if item == 'idley':
#                   print('emjoy', item)
#             elif item == 'pizza':
#                   print('emjoy', item)
#             elif item == 'dosa':
#                   print('emjoy', item)
#             else:
#                   raise NameError
#       except NameError:
#             print('invalid item')
#       except:
#             print('invalid item1111')

# def main():
#       item = 'pasta'
#       menu(item)
# main()


def fun(x):
      try:
            res = 100 / x
            print('inside try')
      except:
            print('inside except')
      else:
            print('inside else')
      finally:
            print('inside finally')
      
fun(2)


# valid
# try:
#       ----------
# except:
#       -------------
# ====================================
# try:
#       ----------
# except:
#       -------------
# else:
#       ------------
# ====================================
# try:
#       ------------
# except:
#       -------------
# else:
#       ------------
# finally:
#       ------------
# ====================================
# try:
#       ------------
# except:
#       -------------
# finally:
#       ------------
# ====================================
# try:
#       ------------
# finally:
#       ------------

