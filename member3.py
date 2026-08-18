def display_menu():
    print("\n===== Home Energy Consumption Tracker =====")
    print("1. Calculate Appliance Consumption")
    print("2. Calculate Electricity Cost")
    print("3. Energy Saving Tips")
    print("4. View Summary")
    print("5. Exit")
    print("=============================================")


def get_user_choice():
    choice = input("Enter your choice (1-5): ")

    # Basic input validation: must be a number
    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

    choice = int(choice)

    # Basic input validation: must be within menu range
    if choice < 1 or choice > 5:
        print("Invalid choice. Please select a number between 1 and 5.")
        return None

    return choice


def main():
    choice = None

    while choice != 5:
        display_menu()
        choice = get_user_choice()

        if choice is None:
            continue  # invalid input, show menu again

        if choice == 1:
            print("[Calculate Appliance Consumption] - to be implemented by Member 1")
            # calculate_appliance_consumption()

        elif choice == 2:
            print("[Calculate Electricity Cost] - to be implemented by Member 1/2")
            # calculate_electricity_cost()

        elif choice == 3:
            print("[Energy Saving Tips] - to be implemented by Member 2")
            # show_energy_saving_tips()

        elif choice == 4:
            print("[View Summary] - to be implemented by Member 4")
            # view_summary()

        elif choice == 5:
            print("Exiting program. Goodbye!")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
