str = "a1b10c7"
alphas = []
numbers = []
temp_alpha = ""
temp_num = ""

for i in str:
    if i.isalpha():
        if temp_num:
            numbers.append(temp_num)
            temp_num = ""
        temp_alpha += i
    else:
        if temp_alpha:
            alphas.append(temp_alpha)
            temp_alpha = ""
        temp_num += i
        
if(temp_num):
    numbers.append(temp_num)
if temp_alpha:
    alphas.append(temp_alpha)
        
print(alphas)
print(numbers)