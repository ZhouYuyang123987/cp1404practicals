"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when enter not a number
2. When will a ZeroDivisionError occur?
when denominator is zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
       fraction = numerator / denominator
       print(fraction)
    else:
        print("Denominator can't be zero")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")