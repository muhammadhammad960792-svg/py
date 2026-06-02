class Robot:
    def __init__(self, name, model, purpose, year):
        self.name = name
        self.model = model
        self.purpose = purpose
        self.year = year

    def introduce(self):
        print(" Hello! I am a Robot.")
        print(f"My name is {self.name}.")
        print(f"I am model {self.model}.")
        print(f"My purpose is {self.purpose}.")
        print(f"I was created in {self.year}.")

    def perform_task(self):
        print(f"{self.name} is now performing its task: {self.purpose}.")


# Creating an object of Robot class
robot1 = Robot("RoboX", "RX-2026", "Assisting humans in daily work", 2026)

# Using methods
robot1.introduce()
print()
robot1.perform_task()