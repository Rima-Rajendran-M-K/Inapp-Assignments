dict =  {}
class Pet:
    def __init__(self, species="None", name=""):
        try:
            if species in ['dog', 'cat', 'horse', 'hamster']:
                self.species_str = species
                self.name_str = name
            else:
                raise Error()
        except Error():
            print("Invalid species")


    def __str__(self):
        if self.name_str= "":
            result = "Species of: {}, unnamed!".format(self.species_str)
        else:
            result = "Species of: {}, named {}.".format(self.species_str, self.name_str)
        return result
class Dog(Pet):
    def __init__(self, name="", chases="Cats"):
        super().__init__(name=name, chases=chases)
        self.name_str = name
        self.chases_str = chases
        self.species_str = "Dog"

    def __str__(self):
        if self.name_str="":
            result = "Species  of: {} unnamed chases {}".format(self.species_str,self.chases_str)
        else:
            result = "Species  of: {} named {} chases zzz {}".format(self.species_str, self.name_str, self.chases_str)
        return result

class Cat(Pet):
    def __init__(self, name="", hates="Dogs"):
        super().__init__(name=name, hates=hates)
        self.name_str = name
        self.hates_str = hates
        self.species_str = "Cat"

    def __str__(self):
        if self.name_str="":
            result = "Species  of: {} unnamed hates zzz {}".format(self.species_str, self.hates_str)
        else:
            result = "Species  of: {} named {} hates zzz {}".format(self.species_str, self.name_str, self.hates_str)
        return result

def main():
        D1 = Dog('hamster')
        D2 = Dog()
        D3 = Dog()
        D4 = Dog()
        D5 = Dog()
        C1 = Cat()
        C2 = Cat()
        C3 = Cat()
main()