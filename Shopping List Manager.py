# Shopping List Manager using File Handling

FILE_NAME = "shopping_list.txt"

def add_item():
    item = input("Enter item to add: ")
    with open(FILE_NAME, "a") as file:  # append mode
        file.write(item + "\n")
    print(f"'{item}' added successfully!")

def view_items():
    try:
        with open(FILE_NAME, "r") as file:  # read mode
            items = file.readlines()

        if not items:
            print("Shopping list is empty.")
        else:
            print("\n--- Shopping List ---")
            for i, item in enumerate(items, start=1):
                print(f"{i}. {item.strip()}")
    except FileNotFoundError:
        print("No shopping list found yet.")

def clear_list():
    with open(FILE_NAME, "w") as file:  # write mode (clears file)
        pass
    print("Shopping list cleared!")

def remove_item():
    try:
        with open(FILE_NAME, "r") as file:
            items = file.readlines()

        if not items:
            print("Shopping list is empty.")
            return

        view_items()
        choice = int(input("Enter item number to remove: "))

        if 1 <= choice <= len(items):
            removed = items.pop(choice - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(items)

            print(f"Removed: {removed.strip()}")
        else:
            print("Invalid item number!")

    except FileNotFoundError:
        print("No shopping list found.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== Shopping List Manager =====")
        print("1. Add Item")
        print("2. View Items")
        print("3. Remove Item")
        print("4. Clear List")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            clear_list()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()