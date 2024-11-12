# elif condition
# this is used for more than one condition.

# note: we can write n noof elif blocks inside or btween 'if else'
# there is a school, in the exams are completed for that examination, now we have to give a grade based on hte persons
# if the percentage < 35,
# if the percentage range between 35 to 50 then C,
# if the percentage range between 50 to 90 then B,
# if the percentage range between 90 to 100 then A
# if the percentage > 100 invalid marks

# name = "Naveen"
# marks = int(input('enter marks: '))
# per = (marks/600)*100
# if per < 35:
#       grade = 'F'
# elif per >= 35 and per < 50:
#       grade = 'C'
# elif per >= 50 and per < 90:
#       grade = 'B'
# elif per >= 90 and per < 100:
#       grade = 'A'
# else:
#       grade = 'invalid'
# print('grade: '+ grade)
 
# -----------------------------------------------------------------------------------------------------
# there is a company need to pay owners based on the experience
# if the person having 1 to 5 the salary hike become 5%
# if the person having 5 to 10 the salary hike become 10%
# if the person having more than 10  15%
# if the person having less than 1  no hike

salary = int(input('enter salary: '))
exp = float(input('enter experience: '))

if exp >= 1 and exp < 5 :
      hike_per = 5
elif exp >= 5 and exp < 10:
      hike_per = 10
elif exp >= 10:
      hike_per = 15
elif exp < 1:
      hike_per = 0

hike = (hike_per/100) * salary
total_salary = salary + hike
print(hike, 'hike')
print(total_salary, 'total')