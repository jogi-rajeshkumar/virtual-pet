import time
import random

class VirtualPet:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.health = 50
    
    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        self.happiness += 5
        if self.happiness > 100:
            self.happiness = 100
        print("Yum! Thank you for feeding me.")
    
    def play(self):
        self.happiness += 10
        if self.happiness > 100:
            self.happiness = 100
        self.hunger += 5
        if self.hunger > 100:
            self.hunger = 100
        print("Yay! That was fun.")
        
    def heal(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
        print("Thank you for healing me.")
        
    def status(self):
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")

def decrease_status(pet):
    pet.hunger += 5
    pet.happiness -= 5
    pet.health -= 5

def game_over(pet):
    if pet.health <= 0:
        print("Your pet died. Game Over.")
        return True
    else:
        return False

def random_event(pet):
    chance = random.randint(1, 5)
    if chance == 1:
        pet.health -= 10
        print("Oh no! Your pet got sick.")

pet = VirtualPet()
print("Welcome to the virtual pet game! Meet your new pet.")

while True:
    print("What would you like to do? (feed, play, heal, status, quit)")
    choice = input()
    if choice == "feed":
        pet.feed()
    elif choice == "play":
        pet.play()
    elif choice == "heal":
        pet.heal()
    elif choice == "status":
        pet.status()
    elif choice == "quit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please try again.")
    time.sleep(2)
    decrease_status(pet)
    if game_over(pet):
        break
    random_event(pet)
