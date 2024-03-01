import random


battles = [
    "Grundwald",
    "Hastings",
    "Antioch",
    "Bannockburn",
    "Mohi",
    "Constantinople",
    "Grenada",
    "Saule"
]

player_name = input("Enter your name or nickname " )
print(f"Welcome {player_name} to medieval battles hangman!")

def print_rules():
    """
    Rules and tips for the game
    """
    print("Rules and tips for medieval battles hangman are as follow: ")
    print("1. Battles chosen are in medieval era.")
    print("2. Battles are chosen are based in europe and are mostly city or town names")
    print("3. Letters that has been correctly selected will apear on the word")
    print("4. Incorrect guesses will reduce your remaning attempts by one until it hits 0")
    print("5. If you run out of attempts the game will be over.")

def choose_random_battle():
    """
    Function for random battle choice.
    """
    return random.choice(battles)

def main():
    rules = print_rules()
    word = choose_random_battle()
    

main()