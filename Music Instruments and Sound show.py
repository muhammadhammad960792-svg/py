from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class MusicalInstrument(ABC):

    @abstractmethod
    def sound(self):
        pass  # Must be implemented by all subclasses


# Child class 1 (Inheritance)
class Guitar(MusicalInstrument):
    def sound(self):
        return " Guitar sounds: Strum strum"

# Child class 2
class Piano(MusicalInstrument):
    def sound(self):
        return " Piano sounds: Plink plonk"

# Child class 3
class Drum(MusicalInstrument):
    def sound(self):
        return " Drum sounds: Boom boom"


# Function to show sounds
def show_instruments(instruments):
    for instrument in instruments:
        print(instrument.sound())


# Create objects
guitar = Guitar()
piano = Piano()
drum = Drum()

# Demonstration
instruments = [guitar, piano, drum]
show_instruments(instruments)