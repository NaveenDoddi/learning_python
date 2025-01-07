# the process of inheritence the properties form parent class to child class is called inheritance

# types
#       single 
      
#       multilevel
      
#       multiple
      
#       hyrechicle
      
#       hybrid

#       cyclic (python will not allowed)


# advantages
#       * code reusability
#       * reduce the development time
#       * easy 

# ------------------------------------------------------------------------------------
# single level
# taking properties from parent class to child class at one stage
class Alpha:
      def fun(self):
            print('full *alpha* fun is happening')

class Beta(Alpha):
      pass

# using1 = Beta()
# using1.fun()

# in pyton every thing inheritng from class
# print(dir(Alpha))
# ------------------------------------------------------------------------------------
# multilevel

# child become a parent, then parent become a child
# multiple single level inheritence is called as multilevel inheritance
class Alpha:
      def fun1(self):
            print('full *alpha* fun is happening')

class Beta(Alpha):
      def fun2(self):
            print('full *Beta* fun is happening')
            
class Gama(Beta):
      pass

# using1 = Gama()
# using1.fun1()
# using1.fun2()

# ------------------------------------------------------------------------------------
# multiple
# taking properties from mutliple parent classes to child class is called multiple inheritance

class Alpha:
      def fun1(self):
            print('full *alpha* fun is happening')
class Beta:
      def fun2(self):
            print('full *Beta* fun is happening')      
class Gama(Alpha,Beta):
      pass

# using1 = Gama()
# using1.fun1()
# using1.fun2()

# ------------------------------------------------------------------------------------
# hiracle inheritance
# taking properties from one parent class to multiple child classes is called hiracle inheritance


class Alpha:
      def fun1(self):
            print('full *alpha* fun is happening')
class Beta(Alpha):
      pass  
class Gama(Alpha):
      pass

# ------------------------------------------------------------------------------------



class Plane:
      def fly(self):
            print('flying')
      def landing(self):
            print('landing')
            
class Passenger_palne(Plane):
      def carry(self):
            print('passsengers')
            
class Cargo_plane(Plane):
      def carry(self):
            print('carry goods')
            
class Fighter_plane(Plane):
      
      def __init__(self,weapon1, weapon2):
            self.weapon1 = weapon1
            self.weapon2 = weapon2
      
      def carry(self):
            print('carry weapons',self.weapon1, self.weapon2)
      
# plane1= Passenger_palne()
# plane1.fly()
# plane1.landing()
# plane1.carry()

      
# plane2= Cargo_plane()
# plane2.fly()
# plane2.landing()
# plane2.carry()

      
# plane3= Fighter_plane('AKM', 'UMP')
# plane3.fly()
# plane3.landing()
# plane3.carry()


# another program for library system

tfi_1000 = ['rrr', 'kalki', 'bahubali 2', 'pushpa']
tfi_500 = ['bahubali 1 ', 'animal', 'salar', 'devara']
tfi_flop = ['adipurush', 'sahoo', 'nakshatram']
            
def display(list):
      print('1000 cr films')
      for film in list:
            print(film)
class Club500:
      def silver(self):
            print('this movie is a silver jublee')
class Club1000(Club500):
      def gold(self):
            print('this movie has a golden jublee')

# c1 = Club1000()
# c1.silver()
# c1.gold()
            
class Newfilm:
      def adding_1000(self, name):
            self.name = name
            tfi_1000.append(self.name)
            print('new film added====> ',name)
            display(tfi_1000) 
                       
      def adding_500(self, name):
            self.name = name
            tfi_500.append(self.name)
            print('new film added====> ', name)
            display(tfi_500)
            
      def adding_flop(self, name):
            self.name = name
            tfi_flop.append(self.name)
            print('new film added ====> ', name)
            display(tfi_flop)

cinima = Newfilm()

# cinima.adding_1000('puspha 2')
# cinima.adding_500('game changer')
while True:
      print('1. add film into 1000 club')
      print('2. add film into 500 club')
      print('3. add film into flop club')
      print('4. exit')

      user_input = int(input('enter user choice: '))
      cinima_name = input('enter cinima name: ')

      if(user_input == 1):
            print('adding film into 1000 club')
            cinima.adding_1000(cinima_name)
            
      elif(user_input == 2):
            print('adding film into 500 club')
            cinima.adding_500(cinima_name)
            
      elif(user_input == 3):
            print('adding film into flop club')
            cinima.adding_flop(cinima_name)
            
      elif(user_input == 4):
            print("EXIT")
            break
      
