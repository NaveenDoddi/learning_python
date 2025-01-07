import math
def deci(num):
    return str(num).rjust(4)
# ---------------------------------------------

def octal(num):
    arr = []
    while num > 0:
        
        arr.append(str(num % 8))
        num = math.floor(num / 8)
            
    result = ''.join(arr).ljust(4)
    return(result[::-1])
# ---------------------------------------------

def hexa(num):
    arr = []
    while num > 0:
        
        rem = (num % 16)
        
        if rem == 10:
            arr.append('A')
        elif rem == 11:
            arr.append('B')
        elif rem == 12:
            arr.append('C')
        elif rem == 13:
            arr.append('D')
        elif rem == 14:
            arr.append('E')
        elif rem == 15:
            arr.append('F')
        else:
            arr.append(str(rem))
            
        num =  math.floor(num / 16)
    result = ''.join(arr).ljust(4)
    return(result[::-1])
# ------------------------------------------------

def binary(num):
    arr = []
    while num > 0:
        arr.append(str(num % 2))
        num = math.floor(num / 2)
        
    result = ''.join(arr).ljust(6)
    return(result[::-1])
    
for i in range(1, 15):
    print(deci(i), octal(i), hexa(i), binary(i))
    