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



    
def print_rules():
    """
    Rules and tips for the game
    """
    print("Rules and tips for medieval battles hangman are as follow:\n ")
    print("1. Battles chosen are in medieval era.")
    print("2. Battles are chosen are based in europe and are mostly city or town names")
    print("3. Letters that has been correctly selected will apear on the word")
    print("4. Incorrect guesses will reduce your remaning attempts by one until it hits 0")
    print("5. If you run out of attempts the game will be over.\n ")


def display_word(word, guessed_letters):
    displayed_word = " "
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ""
        else: 
                displayed_word += ""
                return displayed_word.strip()



def get_user_guess(display_word,):
    while True:

        guess = input("Your guess:  ").upper()
        if guess in guessed_letters:
            print("You already tried this!")
        elif guess in display_word:
           print("You are correct!")
           display += guess + " "
        else:
            attempts -= 1
            print("Game over! You have been hanged!")


"""
def guessed_letters(display_word,):
    if guess is display_word:
        print("You are correct!") 
"""



def choose_random_battle():
    """
    Function for random battle choice.
    """
    return random.choice(battles).upper()

def main():
    player_name = input("Enter your name or nickname \n" )
    print(f"Welcome {player_name} to medieval battles hangman!") 
    print_rules()
    word = choose_random_battle()
    display_word = "_" * len(word)
    get_user_guess(display_word)
    attempts = 6
    while True:
        play_game = input(f"Would you like to continue? y or n  \n")
        if play_game.lower() == "y":
            print(f"This is your word: ", display_word )
            break
        elif play_game.lower() == "n":
            print(f"{player_name} chose not to play! Returning to start")
            main()
            exit()
    print("Code after loop")
    """
    get_user_guess()
    """
    
   
    """
    display_word = word + "_"  len(word)
 """
"""
display_word(word,guessed_letters):
"""

main()