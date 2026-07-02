

import os

def create_notes(filename):
    print("\nEnter your study notes (type 'END' to finish):")

    with open(filename, "w") as f:
        while True:
            line = input()
            if line.upper() == "END":
                break
            f.write(line + "\n")

    print(f"\nNotes saved in '{filename}'.")



def display_notes(filename):
    if os.path.exists(filename):
        print("\n----- Study Notes -----")
        with open(filename, "r") as f:
            print(f.read())
    else:
        print("File does not exist.")

def count_words(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            text = f.read()
            words = text.split()   # Using split()
            print("\nTotal Words:", len(words))
    else:
        print("File does not exist.")

def merge_files(file1, file2, merged_file):
    if os.path.exists(file1) and os.path.exists(file2):
        with open(merged_file, "w") as out:
            with open(file1, "r") as f1:
                out.write(f1.read())

            out.write("\n")

            with open(file2, "r") as f2:
                out.write(f2.read())

        print(f"\nFiles merged successfully into '{merged_file}'.")
    else:
        print("One or both files do not exist.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)   # Using os.remove()
        print(f"'{filename}' deleted successfully.")
    else:
        print("File does not exist.")



def main():
    while True:
        print("\n===================================")
        print("      Study Notes Organizer")
        print("===================================")
        print("1. Create Notes File")
        print("2. Display Notes")
        print("3. Count Words")
        print("4. Merge Two Files")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter filename: ")
            create_notes(filename)

        elif choice == "2":
            filename = input("Enter filename: ")
            display_notes(filename)

        elif choice == "3":
            filename = input("Enter filename: ")
            count_words(filename)

        elif choice == "4":
            file1 = input("Enter first filename: ")
            file2 = input("Enter second filename: ")
            merged = input("Enter merged filename: ")
            merge_files(file1, file2, merged)

        elif choice == "5":
            filename = input("Enter filename to delete: ")
            delete_file(filename)

        elif choice == "6":
            print("\nThank you for using Study Notes Organizer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()