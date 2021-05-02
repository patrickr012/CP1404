"""
Patrick Robinson
12251568
CP1404

"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

print("Lets Drive ")
print(MENU)


def main():
    """A taxi simulator that makes use of the Taxi and SilverServiceTaxi classes. The user is presented with the available
    taxis. They can choose which one to drive, how far to drive and are presented with their current and total bill.  When
    they choose to quit they are shown the total bill and distance travelled."""
    list_of_taxis = [Taxi("Prius", 100), SilverServiceTaxi(2, "Limo", 100), SilverServiceTaxi(4, "Hummer", 100)]
    menu_choice = input().lower()
    bill = 0
    current_taxi = None
    total_distance = 0

    while menu_choice != "q":

        if menu_choice == "c":

            show_taxis(list_of_taxis)
            try:
                taxi_choice = input("Choose taxi")

                current_taxi = list_of_taxis[int(taxi_choice)]
                print("You have chosen: ", current_taxi)
                print(MENU)
                menu_choice = input().lower()
            except ValueError:
                print("Incorrect Input")
                for count, taxi in enumerate(list_of_taxis):
                    print(count, taxi)
                taxi_choice = input("Choose taxi")
            except IndexError:
                print("Incorrect Option")
                for count, taxi in enumerate(list_of_taxis):
                    print(count, taxi)
                taxi_choice = input("Choose taxi")

        if menu_choice == "d":
            try:
                drive_distance = float(input("Drive how far"))
                current_taxi.drive(drive_distance)
                total_distance += drive_distance
                print(current_taxi)
                print("Your trip of {}km has cost you ${}".format(drive_distance, current_taxi.get_fare()))
                bill += current_taxi.get_fare()
                print("Your current bill is: ${:.2f}".format(bill))
                print(MENU)
                menu_choice = input().lower()
            except AttributeError:
                print("Taxi has not been chosen yet")
                print(MENU)
                menu_choice = input().lower()
        else:
            print("Incorrect Choice")
            print(MENU)
            menu_choice = input().lower()

        print("Your total bill is : ${:.2f}".format(bill))
        print("Your total distance travelled is: {:.2f}km".format(total_distance))


def show_taxis(list_of_taxis):
    """Displaying a numbered list of taxis
    :param: list_of_taxis: the list of taxis created at the start of the program"""
    for count, taxi in enumerate(list_of_taxis):
        print(count, taxi)


main()
