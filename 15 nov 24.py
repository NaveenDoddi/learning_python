# country = input("enter your country: ")
# age = int(input('enter your age: '))
# if(country == 'morocco'):
#       if age < 16:
#             print('not eligible for driving')
#       else:
#             print('eligible for ')
#             if age >= 16:
#                   print('motorcycles')
#                   if age >= 18:
#                         print('cars')
#                         if age >= 21:
#                               print('trucks')
# elif country == 'india':
#       if age >= 18:
#             print('eligible for motorcycle, cars and trucks')
#       else:
#             print('not eligible for driving')
# elif country == "sri lanka":
#       if age >= 17:
#             print('eligible for motorcycle, cars and trucks')
#       else:
#             print('not eligible for driving')
# elif country ==  "japan":
#       if age >= 16 and age < 18:
#             print('eligible for motorcycles (under 400 cc)')
#       elif age >= 18:
#             print(' rligible for ordinary/semi-medium vehicle and motorcycles over 401 cc')
#       else:
#             print('not eligible for driving')


# travelling agency
# the travelling agency name is "JUGAD journey". the jugad is present in two contents
# asia and america. in asia they are present in 4 countries. They are india, pakistan, bangladesh, sri lanka
# in INDIA they are running a package of two states karnataka and kerala and ticket price is 25k per each person
# ask a user how many people are attending this journwey and calculate the total prize

continent = input("enter your continent: ")
if continent == 'asia':
      print('we available in 4 countries\nindia, pakistan, bangladesh, sri lanka')
      country = input("enter your country: ")
      if(country == 'india'):
            print('we available in 2 states karnataka and kerala')

            state = input('enter state: ')
            if state == 'karnataka':
                  print('enter how many persons are attending for', state)

                  ticket = 25000
                  persons = int(input('enter no of people: '))

                  total_package = persons * ticket
                  print("total cost of the package for", persons, "is", total_package)
