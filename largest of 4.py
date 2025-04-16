
# Find the Largest of Four Numbers
# Forked and Enhanced by Sania Irshad


def get_largest_number():
    print("🔢 Find the Largest of Four Numbers\n")

    try:
        # Get four numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))

        # Find the largest number using max()
        largest = max(num1, num2, num3, num4)

        # Display result
        print(f"\n✅ The largest number is: {largest}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values only.")

# Run the function
if __name__ == "__main__":
    get_largest_number()
