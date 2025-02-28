def smart_calculator():
    while True:
        print("\n🔹 Welcome to Smart Calculator 🤖")
        print("🔹 Select an operation:")
        print("   1. Addition (+)")
        print("   2. Subtraction (-)")
        print("   3. Multiplication (*)")
        print("   4. Division (/)")
        print("   5. Exit ❌")
        
        choice = input("🔹 Enter the number of your choice (1/2/3/4/5): ")

        if choice == '5':
            print("🔹 Exiting... Thank you for using Smart Calculator! 🚀")
            break  # Exit the loop
        
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("🔹 Enter the first number: "))
            num2 = float(input("🔹 Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                operation = "+"
            elif choice == '2':
                result = num1 - num2
                operation = "-"
            elif choice == '3':
                result = num1 * num2
                operation = "*"
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    operation = "/"
                else:
                    print("❌ Error: Division by zero is not allowed!")
                    continue  # Skip the rest and ask again

            print(f"✅ Result: {num1} {operation} {num2} = {result}")
        else:
            print("❌ Invalid choice! Please select a valid operation.")

# Run the calculator
smart_calculator()
