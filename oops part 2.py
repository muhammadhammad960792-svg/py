class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []
        print(f"Playlist '{self.name}' ({self.genre}) is ready!")

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed.")
        else:
            print(f"'{song}' not found in playlist.")

    def display(self):
        print(f"\n--- {self.name} ({self.genre}) ---")

        if self.songs:
            for i, song in enumerate(self.songs, 1):
                print(f"{i}. {song}")
        else:
            print("No songs in the playlist.")

    def __del__ (self):
     print(f"playlist  '{self.name}' has been deleted .Goodbye!")
my__playlists=Playlist("Road Trip Mix","pop")
while True:
    print("\n1.add song 2.remove song 3.View playlist 4.Delete and Quit")
    choice=input("Enter your choice:")
    if choice =="1":
        song=input("Enter your song name:")
        my__playlists.add_song(song)
    elif choice=="2":
        song=input("Enter song to remove")
        my__playlists.remove_song(song)
    elif choice =="3":
        my__playlists.display()
    elif choice =="4":
        del my__playlists
        break
    else:
        print("Invalid Choice.Enter 1,2,3,or 4.")
