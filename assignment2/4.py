score=int(input("Enetr score:"))
if score<60:
    print("F Grade")
elif score>=60 and score<=69:
    print("D Grade")
elif score>=70 and score<79:
    print("C Grade")
elif score>=80 and score<89:
    print("B Grade")
elif score>=90 and score<=100:
    print("A Grade")
else:
    print("Invalid Marks")
    