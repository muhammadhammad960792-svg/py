# Smart Note Organizer

while True:
    print("\n===== SMART NOTE ORGANIZER =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter Note Title: ")
        note = input("Enter Note: ")

        file = open("notes.txt", "a")
        file.write("Title: " + title + "\n")
        file.write("Note : " + note + "\n")
        file.write("--------------------------\n")
        file.close()

        print("Note Saved Successfully!")

    elif choice == "2":
        file = open("notes.txt", "r")
        data = file.read()
        print("\n===== YOUR NOTES =====")
        print(data)
        file.close()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")