from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive\n>>>"


def main():
    """Main function controlling the taxi simulation process"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    choice = input(MENU).lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = get_valid_taxi_choice(taxis, taxi_choice)
        elif choice == "d":
            trip_cost = drive_taxi(current_taxi)
            total_bill += trip_cost
        else:
            print("Invalid choice")
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input(MENU).lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def get_valid_taxi_choice(taxis, taxi_choice):
    """Get valid choice number"""
    try:
        return taxis[taxi_choice]
    except IndexError:
        print("Invalid taxi choice")


def drive_taxi(current_taxi):
    """Drive a taxi and calculate the price"""
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    else:
        print("You need to choose a taxi before you can drive")
        return 0


main()
