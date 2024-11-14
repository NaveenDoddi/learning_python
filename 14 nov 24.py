# nested if else condition
# the condition inside another condition is called as nested if else condition

# note: if once declare if condition then must adn shiuld bt else condition
# this is nothing but standardisation of programing or cohegin programm

# there is a foodball match to attend foodball match, age should be 18. if this condion is satisified 
# then we need to declare ticket price based on the age.
# if 18-30== $20 
# if 30-50== $30 
# if >50== free
# 

# age = int(input('enter age: '))
# if (age >= 18):
#       print('allowed for the match')
#       if age >= 18 and age < 30:
#             ticket_prize = 20
#       elif age >= 30 and age < 50:
#             ticket_prize = 30
#       else:
#             ticket_prize = 0
      
#       print('ticket_prize', ticket_prize,'$')
# else:
#       print('not allowed for the match')


#phone pay chatboot
# it is working on nested if else condition 

print('welcome to phone pay')
print('1. payment issues\n2. profile & payments \n3. money transfer')

user = int(input('eneter user input: '))
if user == 1:
      print('greetings from payment issues')
      print('1. issues with failed payments\n2. issues with pending payments \n3. issues with successfull payments')
      user = int(input('eneter user input: '))

      if user == 1:
            print('greetings from failed payments')
            print('1. why did my UPI payment fail? \n2. Why is my money deducted for my failed payment \n3. Why is my money not refunded yet?')
            user = int(input('eneter user input: '))
            if user == 1:
                  print('Message')
                  print('* UPI network issues')
                  print('* Technical issues with the banks')
            elif user == 2:
                  print('Message')
                  print('If ypur bank fails to refund the amount with 5 days')

      elif user == 2:
            print('greetings from pending payments')
            print('something more...')
      
      elif user == 3:
            print('greetings from successfull payments')
            print('something more...')

      else:
            print('invalid input')

elif user == 2:
      print('greetings from profile & payments')
      print('something more...')

elif user == 3:
      print('greetings from money transfer')
      print('something more...')
else:
      print('invalid input')





      

