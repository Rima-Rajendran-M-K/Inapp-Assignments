from random import randrange

class Pet():

    hunger_threshold = 10
    boredom_threshold = 10
    hunger_decrement = 6
    boredom_decrement = 9
    sounds = ['Mmp']

    def __init__(self, name = 'Sammy'):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.hunger <= self.hunger_threshold and self.boredom <= self.boredom_threshold:
            return "happy"
        elif self.hunger > self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood() + ". "
        return state

    def teach(self, word):
        print("I learned a new word!")
        self.sounds.append(word)
        self.reduce_boredom()

    def hi(self):
        print("Hi I'm {}".format(self.name))
        print(self.sounds[randrange(len(self.sounds))])
        self.reduce_boredom()

    def feed(self):
        print('Thanks for feeding me!')
        self.reduce_hunger()

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

class Dog(Pet):
    sounds = ['Woof', 'Ruff']

    def mood(self):
        if (self.hunger > self.hunger_threshold) and (self.boredom > self.boredom_threshold):
            return "bored and hungry"
        else:
            return "happy"

    def feed(self):
        Pet.feed(self)
        print("Thanks!")

class Cat(Pet):
    sounds = ['Meow']

    def mood(self):
        if self.hunger > self.hunger_threshold:
            return "hungry"
        if self.boredom <2:
            return "disturbed so leave me alone"
        elif self.boredom > self.boredom_threshold:
            return "bored"
        elif randrange(2) == 0:
            return "annoyed"
        else:
            return "happy"


p1 = print('Enter pet name: ')
my_p1 = Pet(p1)
ch = ''
while ch != '0':
    print('\n 1. Greet \n 2. Teach \n 3. Feed \n 4. Exit')
    ch = int(input("\n Enter the choice:"))
    if ch == '1':
        my_p1.hi()
    elif ch == '2':
        word = input("Enter the word: ")
        my_p1.teach()
    elif ch == '3':
        my_p1.feed()
    elif ch == '4':
        exit()
    else:
        print("Invalid choice!")




