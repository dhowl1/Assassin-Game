import random
from Assassin import Assassin

def main():
    print("Welcome to the Assassin Manager")
    print()
    file_name = input("What name file do you want to use this time? ")

    try:
        with open(file_name) as f:
            names = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File not found")
        return

    if yes_to("Do you want the names shuffled?"):
        random.shuffle(names)
    
    manager = Assassin(names)
    print()

    while not manager.game_over():
        one_kill(manager)
    
    print("Game was won by", manager.winner())
    print("Final graveyard is as follows:")
    manager.print_graveyard()

def one_kill(manager):
    print("Current kill ring:")
    manager.print_kill_ring()
    print()
    print("Current graveyard:")
    manager.print_graveyard()
    print()
    name = input("next victim? ").strip()
    if manager.graveyard_contains(name):
        print(name, "is already dead.")
    elif not manager.kill_ring_contains(name):
        print("Unknown person.")
    else:
        manager.kill(name)
    print()

def yes_to(prompt):
    response = input(prompt + " (y/n)? ").strip().lower()
    while response not in ('y', 'n'):
        print("Please answer y or n.")
        response = input(prompt + " (y/n)? ").strip().lower()
    return response == 'y'

if __name__ == "__main__":
    main()
