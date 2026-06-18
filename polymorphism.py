class Cricket:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score 
    def info(self):
        print(f"Cricket  _ Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} hits a six!")
    def get_score(self):
        return self.__score
    def set_score(self, new_score):
        if new_score >=0:
            print(f"Score Updated to {self.__score}")
        else:
            print("Score cannot be nagative.")

class Football:
    def __init__(self,player,score):
        self.__player=player
        self.__score=score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")
    def play(self):
        print(f"{self.__player} score a goal!")
    def get_score (self):
        return self.__score
    def set_score (self, new_score):
        if new_score >=0:
            self.__score+new_score
            print(f"Score updated to {self.__score}")
        else:
            print("Score cannot be nagative.")

Cricket=Cricket("Virat Kohli",18)
football=Football("Lionel Messi",10)

print("=== Sports Scoreboard ===\n")
for sport in (Cricket, football):
    sport.info()
    sport.play()
    print()

print("===Direct Change attempt  ===")
Cricket.__score =999
print(f"get_score()still shows: {Cricket.get_score()}")

print("\n === updating scores ===")
Cricket.set_score(100)
football.set_score(3)
