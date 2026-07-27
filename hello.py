#!/usr/bin/env python3
"""
A simple Hello World program
"""

def greet(name):
    """Print a greeting message"""
    print(f"Hello, {name}! Welcome to your first program.")


def main():
    """Main function"""
    print("=== Welcome to My First Program ===\n")
    
    # Get user input
    user_name = input("What's your name? ")
    
    # Call the greeting function
    greet(user_name)
    
    # Simple calculation
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print(f"\nResults:")
    print(f"  Addition: {num1} + {num2} = {num1 + num2}")
    print(f"  Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"  Multiplication: {num1} * {num2} = {num1 * num2}")
    print(f"  Division: {num1} / {num2} = {num1 / num2:.2f}")
    
    print("\nThank you for using this program!")


if __name__ == "__main__":
    main()
