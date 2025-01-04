# method overriding
# same class name but different parameter or code can be override in python

class normal_user():
      def log_in(self):
            name =  input('enter name')
            password =  input('enter password')
      def register(self):
            name =  input('enter name')
            password =  input('enter password')
            password =  input('reenter password')
            mb_nu = int(input('enter mobile'))

class prime_user(normal_user):
      def log_in(self):
            pr_id = input('enter prime id')
            print('login succuess')
      
      def register(self):
            amount = input('enter amount')
            print('registered completed')
      
      
# u1 = prime_user()
# u1.log_in()
            
      # here we have same function names from parent class, but this is overring it in child class
      
      
      
bank_bal = 1000

def info():
      print('bank balence', bank_bal)
      
class bank_admin:
      def withdraw(self):
            global bank_bal
            user_amt = int(input('enter amount'))
            if user_amt < bank_bal:
                  bank_bal -= user_amt
                  print('withdraw successfully, please colllect ur money')
                  info()
            else: 
                  print ('insufficent balence')
                  
      
      
class rupeey(bank_admin):
      pass

class cred_user(bank_admin):
      def withdraw(self):
            global bank_bal
            user_amt = int(input('enter amount'))
            bank_bal -= user_amt
            print('withdraw successfully, please colllect ur money')
            info()
            


b_u1 = rupeey()
b_u1.withdraw()
# here we are not using over riding, what ever in the parent class(bank_admin) is directly excuting

# b_u2 = cred_user()
# b_u2.withdraw()
# here we are using overriding, and wihtdraw function is changed not recent one is running



