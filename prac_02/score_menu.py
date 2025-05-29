MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

def main():
    """Run the score menu program ."""
    score = get_valid_score()
    print(MENU)
    choice = input("Enter choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(f"Your final grade is: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")
        else:
            print("Error choice.")

        print(MENU)
        choice = input("Enter choice: ").upper()

def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Enter a valid score (0-100): "))
    return score

def print_result(score):
    """Determine the final grade ."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    print("*" * int(score))

main()