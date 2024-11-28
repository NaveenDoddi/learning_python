celsius = float(input("Enter temperature in Celsius: "))
print("Choose conversion:")
print("1. Convert to Fahrenheit")
print("2. Convert to Kelvin")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, "°C is equal to", fahrenheit, "°F.")
elif choice == 2:
    kelvin = celsius + 273.15
    print(celsius, "°C is equal to", kelvin, "°F.")
else:
    print("Invalid choice. Please enter 1 or 2.")

