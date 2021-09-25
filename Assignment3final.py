from random import randrange
pets = ['sam', 'kitty']
user_pets = {'sam': 'dog', 'kitty': 'cat'}

class Pet:
    hunger_threshold = 10
    boredom_threshold = 5
    hunger_decrement = 4
    boredom_decrement = 3
    sounds = ['Hello!', ' Hai']

    def __init__(self, name):
        self.name = name
        self.hunger = randrange(self.hunger_threshold)
        self.boredom = randrange(self.boredom_threshold)
        self.sounds = self.sounds[:]

    def __str__(self) -> str:
        return " I'm  " + self.name + " current mood is  " + self.mood() + "."

    def clock_tick(self):
        self.boredom += 1
        self.hunger += 1

    def mood(self):
        if self.boredom <= self.boredom_threshold and self.hunger <= self.hunger_threshold:
            return "happy"
        elif self.boredom >= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry & bored"
        elif self.boredom <= self.boredom_threshold and self.hunger >= self.hunger_threshold:
            return "hungry"
        else:
            return "bored"

    def teach(self, word):
        if word not in self.sounds:
            print('\nI learned a new word: {}'.format(word.title()))
            self.sounds.append(word.title())
        else:
            print('Word already taught!')
        self.reduce_boredom()

    def hi(self):
        print(self.sounds[randrange(len(self.sounds))]+' {}.'.format(self.name))
        self.reduce_boredom()

    def feed(self):
        self.reduce_hunger()
        print("\nArf! Thanks!")

    def reduce_boredom(self):
        self.boredom = max(0, self.boredom - self.boredom_decrement)

    def reduce_hunger(self):
        self.hunger = max(0, self.hunger - self.hunger_decrement)

class Dog1(Pet):
    def __init__(self):
        print("Dog 1 successfully created!")

class Dog2(Pet):
    def __init__(self):
        print("Dog 2 successfully created!")

class Dog3(Dog1, Dog2):
    def __init__(self):
        print("Dog 3 successfully created!")

class Cat(Pet):
    def __init__(self):
        print("Cat successfully created!")

def users_pets():
        print("\nMy Pets")
        print('............')
        for pet, type in user_pets.items():
            p1 = Pet(pet)
            print(f"Hi I'm {pet} my current mood is {p1.mood()} and I'm a {type}!!")

print('WELCOME')
print('__________')
game = 1
d1 = Dog1()
d2 = Dog2()
d3 = Dog3()
c1 = Cat()
while game:
    print('\nMENU \n 1. Adopt \n 2. Greet \n 3. Teach \n 4. Feed \n 5. Display pets \n 6. Exit')
    ch = int(input("\nEnter the choice: "))
    if ch == 1:
        print('\nAdopt a new pet!')
        a_pet_name = input('Enter the pet name: ')
        a_pet_type = input('Enter the pet type: ')
        pets.append(a_pet_name)
        user_pets[a_pet_name] = a_pet_type
    elif ch in range(2, 5):
        name = input('Enter pet name: ')
        p1 = Pet(name)
        flag = 0
        for i in range(len(pets)):
            if pets[i] == name:
                if ch == 2:
                    p1.hi()
                elif ch == 3:
                    print(f'The pet you want to teach is {name}!!')
                    word = input(f'Enter the word you wish to teach {name}: ')
                    p1.teach(word)
                elif ch == 4:
                    print(f'The pet you want to feed is {name}!!')
                    p1.feed()
                flag = 1
                p1.clock_tick()
        if flag == 0:
            print("\nInvalid pet choice!!!!")
            print(f"You don't have a pet named {name}!")
    elif ch == 5:
        users_pets()
    else:
        exit()
