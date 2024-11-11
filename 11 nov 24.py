# tv = int(input("enter tvs"))
# hrs = int(input("enter hrs"))

# if hrs > 9 and tv > 5:
#       salary = 2000* tv
# else:
#       salary = 500* tv
# print(salary)

#     there is a company its givinig bonus to the employees based on certain criteria
#     if the employee having more than 5 years of exprerience then his salary becomes 20% hike or if having the cetification of python then also 20% 
#     of hike if both the condition is not match ethen 5% of hike. 
#     calculate hike emaount and print the final paymeent by taking the inputs of the 
#     1. noof year of experience
#     2. saalary
#     3. certification

exp_y = int(input("enter years: "))
cert = input('enter certifications: ')
salary = int(input('enter salary: '))

if(exp_y > 5 or cert == "python"):
      hike_salary = (20/100)* salary
else:
      hike_salary = (5/100) * salary

print("only hike",hike_salary)

print("total salary",hike_salary + salary)

# note: strings are always represents in single, double, triple cotes