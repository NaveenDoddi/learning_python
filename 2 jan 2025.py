# the process of inheritence the properties form parent class to child class is called inheritance

# types
#       single 
      
#       multilevel
      
#       multiple
      
#       hyrechicle
      
#       hybrid

#       cyclic (python will not allowed)

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
tfi_flop = ['adipurush', 'sahoo', 'devara']

def display1000():
      print('1000 cr films')
      for film in tfi_1000:
            print(film)

def display500():
      print('500 cr films')
      for film in tfi_500:
            print(film)

class Newfilm:
      def adding_1000(self, name):
            self.name = name
            tfi_1000.append(self.name)
            print('new film added into club====>',name)
            display1000()
            
      def adding_500(self, name):
            self.name = name
            tfi_500.append(self.name)
            print('new film added into club====>', name)
            display500()

cinima = Newfilm()
# cinima.adding_1000('puspha 2')
# cinima.adding_500('game changer')
while True:
      print('1. add film into 1000 club')
      print('2. add film into 500 club')

      user_input = int(input('enter user choice: '))
      ciima = int(input('enter cinima name: '))

      if(user_input == 1):
            print('adding film into 1000 club')
            cinima.adding_1000(cinima)
      elif(user_input == 2):
            print('adding film into 500 club')
            cinima.adding_1000(cinima)
      elif(user_input == 3):
            print('adding film into flop club')
            cinima.adding_flop(cinima)
            


            
      