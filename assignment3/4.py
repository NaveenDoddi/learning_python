current_light = input("Enter the current traffic light color (red, yellow, green): ")
if current_light == "red":
    print("The next light is green.")
elif current_light == "green":
    print("The next light is yellow.")
elif current_light == "yellow":
    print("The next light is red.")
else:
    print("Invalid input. Please enter red, yellow, or green.")
