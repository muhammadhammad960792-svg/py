# School Subjects Planner

subjects = []

while True:
    print("\n--- School Subjects Planner ---")
    print("1. Add subject")
    print("2. View subjects")
    print("3. Remove subject")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)
        print(subject, "added to your planner.")

    elif choice == "2":
        if len(subjects) == 0:
            print("No subjects in your planner.")
        else:
            print("Your subjects:")
            for i, sub in enumerate(subjects, start=1):
                print(i, sub)

    elif choice == "3":
        subject = input("Enter subject name to remove: ")
        if subject in subjects:
            subjects.remove(subject)
            print(subject, "removed from planner.")
        else:
            print("Subject not found.")

    elif choice == "4":
        print("Exiting planner. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")