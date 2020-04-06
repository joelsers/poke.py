'''
Pokemon Battle!
'''
from random import randint


x = randint(0,10)
poke_list = ['Charmander', 'Bulbasaur', 'Squirtle']

playing = True


class Attacks:
    #add variable type CRIT_CHANCE
    def __init__(self, attack_name, attack_type):

        self.attack_name = attack_name
        self.attack_type = attack_type

class Pokemon:

    def __init__(self, poketype, name, gender, hp = 100):

        self.poketype = poketype
        self.name = name
        self.gender = gender
        self.hp = hp

    def __str__(self):
        return f"My name is {self.name} and I have {self.hp}HP"


    def attack(self):
        attack_damage = 10
        crit_chance = 2

        if x <= crit_chance:
            self.hp = self.hp - attack_damage * 2
            print("It was a critical hit!")
            print(f'{self.name} has {self.hp}HP remaining')
            return self.hp
        else:
            self.hp = self.hp - attack_damage
            print(f'{self.name} has {self.hp}HP remaining')
            return self.hp


    def flamethrower(self):
        base_damage = 32
        crit_chance = 2
        if trainer2_poke == bulbasaur:
            base_damage *= 2
        def damage_calc():
            if x <= crit_chance:
                self.hp = self.hp - base_damage * 2
                print("It was a critical hit!")
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
            else:
                self.hp = self.hp - base_damage
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
        damage_calc()

    def razorleaf(self):
        base_damage = 32
        crit_chance = 2
        if trainer2_poke == squirtle:
            base_damage *= 2
        def damage_calc():
            if x <= crit_chance:
                self.hp = self.hp - base_damage * 2
                print("It was a critical hit!")
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
            else:
                self.hp = self.hp - base_damage
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
        damage_calc()

    def water_gun(self):
        base_damage = 32
        crit_chance = 2
        if trainer2_poke == charmander:
            base_damage *= 2
        def damage_calc():
            if x <= crit_chance:
                self.hp = self.hp - base_damage * 2
                print("It was a critical hit!")
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
            else:
                self.hp = self.hp - base_damage
                print(f'{self.name} has {self.hp}HP remaining')
                return self.hp
        damage_calc()





charmander = Pokemon(poketype='Fire', name='Charmander', hp=100, gender='Male')
bulbasaur = Pokemon(poketype='Grass', name='Bulbasaur', hp=100, gender='Male')
squirtle = Pokemon(poketype='Water', name='Squirtle', hp=100, gender='Female')

razorleaf = Attacks(attack_name = 'Razorleaf', attack_type = 'Grass')
flamethrower = Attacks(attack_name = 'Flamethrower', attack_type = 'Fire')
hydropump = Attacks(attack_name = 'Hydropump', attack_type = 'Water')


def player1_poke():

    pokemon1 = ''

    while pokemon1 != 'Charmander'.upper() and pokemon1 != 'Bulbasaur'.upper() and pokemon1 != 'Squirtle'.upper():

        pokemon1 = input('Trainer 1 please select a Pokemon. Your options are Charmander, Bulbasaur, or Squirtle. ').upper()

    if pokemon1 == 'Charmander'.upper():

        pokemon1 = charmander
        poke_list.pop(0)
        print('Trainer 1. You have chosen Charmander')
        return charmander

    elif pokemon1 == 'Bulbasaur'.upper():

        pokemon1 = bulbasaur
        poke_list.pop(1)
        print('Trainer 1. You have chosen Bulbasaur')
        return bulbasaur

    elif pokemon1 == 'Squirtle'.upper():

        pokemon1 = squirtle
        poke_list.pop(2)
        print('Trainer 1. You have chosen Squirtle')
        return squirtle


def player2_poke():

    pokemon2 = ''

    while pokemon2 != 'Charmander'.upper() and pokemon2 != 'Bulbasaur'.upper() and pokemon2 != 'Squirtle'.upper():

        pokemon2 = input(f'Trainer 2 please select a Pokemon. Your options are {poke_list[0]} or {poke_list[1]}. ').upper()

    if pokemon2 == 'Charmander'.upper():

        pokemon2 = charmander
        print('Trainer 2. You have chosen Charmander')
        return charmander


    elif pokemon2 == 'Bulbasaur'.upper():

        pokemon2 = bulbasaur
        print('Trainer 2. You have chosen Bulbasaur')
        return bulbasaur


    elif pokemon2 == 'Squirtle'.upper():

        pokemon2 = squirtle
        print('Trainer 2. You have chosen Squirtle')
        return squirtle


trainer1_poke = player1_poke()

trainer2_poke = player2_poke()

def trainer_action():
    action = ''

    while action != 'attack'.upper() and action != 'switch'.upper() and action != 'item':
        print(input("What will you do? Attack, switch Pokemon, or use an item?"))
    if action == 'attack'.upper() and turn == 'Trainer 1':
        return




def choose_first():
    flip = randint(0,1)

    if flip == 0:
        return 'Trainer 1'
    else:
        return 'Trainer 2'


trainer2_poke.water_gun()
