print("Select an operation:\n1. Add (+)\n2. Subtract (-)\n3. Multiply (*)\n4. Divide (/)")

while True:
    choice = input("Enter choice (1, 2, 3 or 4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculation
    if choice == '1':
        print(f"Result: {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1 * num2}")
    elif choice == '4':
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid input!")
    again = input("Would you like to try another one? (y/n): ")
    if again == "n":    
        print("Thank you for trying out calculator, cya")
        break
    print()
