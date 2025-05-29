MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def calculate_fahrenheit(celsius):
    """convert"""
    return celsius * 9 / 5 + 32

def calculate_celsius(fahrenheit):
    """convert"""
    return (fahrenheit - 32) * 5 / 9

print(MENU)


def main():
    """user input"""
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("fahrenheit: "))
            celsius =calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")
