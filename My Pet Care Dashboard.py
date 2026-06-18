class Pet:
    def __init__(self, name, age):
        self.__name = name        # Encapsulation (private data)
        self.__age = age          # Encapsulation

    # Getter methods (controlled access)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Method to be overridden (Polymorphism)
    def care_plan(self):
        return "General pet care required"


# Dog class (Subclass)
class Dog(Pet):
    def care_plan(self):  # Polymorphism (method overriding)
        return f"{self.get_name()} needs walking, grooming, and high-protein food."


# Cat class (Subclass)
class Cat(Pet):
    def care_plan(self):  # Polymorphism (method overriding)
        return f"{self.get_name()} needs indoor care, litter cleaning, and light playtime."


# Dashboard System
class PetCareDashboard:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def show_care_plans(self):
        print("\n PET CARE DASHBOARD \n")
        for pet in self.pets:
            print(f"Name: {pet.get_name()}, Age: {pet.get_age()}")
            print("Care Plan:", pet.care_plan())
            print("-" * 40)


# Main Program
dashboard = PetCareDashboard()

# Adding pets
dashboard.add_pet(Dog("Bruno", 3))
dashboard.add_pet(Cat("Misty", 2))
dashboard.add_pet(Dog("Rocky", 5))

# Display dashboard
dashboard.show_care_plans()