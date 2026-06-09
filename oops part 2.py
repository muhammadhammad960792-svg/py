class playlist:
    def __init__(self,name,genre):
        self.name=name
        self.genere=self.genre
        self.songs=[]
        print(f"playlits",'{self.name}'((self.genre)) is ready!)
              
    def add_song(self,song):
        self.songs.append(song)
        print(f" '{song}' added to {self.name}.")
        
    def remove_song(remove,song):
        if song if in self.songs:
            self.songs.remove(song):
            print(f"'{song}'removed.")
        else
            print(f" '{song}'not found in playlist>")
    def display(self):
        print(f"/n---{self.name} ({self.genre})---")
        if self.songs:
            for i ,songs in enumarate (self.songs,1):
                print f" {i}. {songs}:
        else