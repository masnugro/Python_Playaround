# Converts between Celsius, Fahrenheit, and Kelvin

def celsius_to_fahrenheit(c):
	return (c * 9/5) + 32
	
def celsius_to_kelvin(c):
	return c + 273.15
	
def fahrenheit_to_celsius(f):
	return (f - 32) * 5/9
	
def fahrenheit_to_kelvin(f):
	return fahrenheit_to_celsius(f) + 273.15
	
def kelvin_to_celsius(k):
	return k - 273.15
	
def kelvin_to_fahrenheit(k):
	return (k - 2732.15) * 9/5 + 32
	
print("🌡️  Welcome to Temperature Converter!\n")
print("Units available:")
print("  1. Celsius (C)")
print("  2. Fahrenheit (F)")
print("  3. Kelvin (K)")

units = {"1": "Celsius", "2": "Fahrenheit", "3": "Kelvin"}

from_choice = input("\nConvert FROM (1/2/3): ").strip()
to_choice = input("Convert TO   (1/2/3): ").strip()

if from_choice not in units or to_choice not in units:
	print("Invalid choice! Please enter 1, 2, or 3.")
elif from_choice == to_choice:
	print("You picked the same unit! Nothing to convert !")
else:
	try:
		value = float(input(f"Enter temperature in {units[from_choice]}: "))
		
		# Conversion logic
		if from_choice == "1" and to_choice == "2":
			result = celsius_to_fahrenheit(value)
		elif from_choice == "1" and to_choice == "3":
			result = celsius_to_kelvin(value)
		elif from_choice == "2" and to_choice == "1":
			result = fahrenheit_to_celsius(value)
		elif from_choice == "2" and to_choice == "3":
			result = fahrenheit_to_kelvin(value)
		elif from_choice == "3" and to_choice == "1":
			result = kelvin_to_celsius(value)
		elif from_choice == "3" and to_choice == "2":
			result = kelvin_to_fahrenheit(value)
			
		print(f"\n✅ {value}° {units[from_choice]} = {result:.2f}° {units[to_choice]}")
		
	except ValueError:
		print("Please enter a valid number!")
		
	again = input("Do you want to convert again? (y/n): ").lower()
	if again == "n":
		print("Thank you and good bye !")
