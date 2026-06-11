artworks = []

while True:
    print("\n=== Art Gallery Collection Manager ===")
    print("1. Add Artwork")
    print("2. View Collection")
    print("3. Search Artwork")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Artwork Title: ")
        artist = input("Artist Name: ")

        artwork = {
            "title": title,
            "artist": artist
        }

        artworks.append(artwork)
        print("Artwork added successfully!")

    elif choice == "2":
        if len(artworks) == 0:
            print("No artworks in collection.")
        else:
            print("\nCollection:")
            for art in artworks:
                print(f"Title: {art['title']}, Artist: {art['artist']}")

    elif choice == "3":
        search = input("Enter artwork title: ")

        found = False
        for art in artworks:
            if art["title"].lower() == search.lower():
                print(f"Found: {art['title']} by {art['artist']}")
                found = True

        if not found:
            print("Artwork not found.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")