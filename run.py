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
    "Agincourt"
    "Bouvines"
    "Falkirk"
    "Hattin"
    "Carham"
    "Tours"
    "Oribetello"
    "Clontarf"
    "Bordeaux"
]


def print_rules():
    """
    Rules and tips for the game
    """
    print("Rules and tips for medieval battles hangman are as follow:\n ")
    print("1. Battles chosen are in medieval era.\n")
    print("2. Battles are chosen and based in europe and named after areas.\n")
    print("3. If letter guessed right it will apear on board.\n")
    print("4. Wrong guess will reduce your remaning attempts by 1.\n")
    print("5. If you attempts remaining become 0 its game over.\n")
    print("6. If you run out of attempts the game will be over.\n ")
    print("7. If name not provided it be left as blank.\n")


def choose_random_battle(battles):
    return random.choice(battles).upper()
    """
    Function for random battle choice.
    """


def display_word(word, guessed_letters):
    """
    Function for playing the game
    """
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")
    return "".join(display)


def get_user_guess(battles):

    """
With every guess a Letter either remains hidden and player reduces amount of
attempts has, if guessed correctly remain same.
Second loop of the where most logic is stored.
 """
    guessed_letters = []
    attempts = 6
    choose_battle = choose_random_battle(battles)

    while attempts > 0:
        print("Your word:\n", display_word(choose_battle, guessed_letters))
        print("Remanining attempts:\n", attempts)
        guess = input("Your guess:\n ").upper()
        if guess in guessed_letters:
            print("You already guessed this!\n")
            continue

        guessed_letters.append(guess)
        if guess not in choose_battle:
            print("You are incorrect!\n")
            attempts -= 1
        else:
            print("Well done! You guessed a correct letter!\n")
        if display_word(choose_battle, guessed_letters) == choose_battle:
            print("Congratulations! You guessed the word:\n", choose_battle)
            break
        elif attempts == 0:
            print("You've run out of attempts! The word was:\n", choose_battle)
            break


def main():
    """
    First loop when enterering the game.
    """
    player_name = input("Enter your name or nickname \n")
    print(f"Welcome {player_name} to medieval battles hangman!")
    print_rules()
    choose_battle = choose_random_battle(battles)
    guessed_letters = []
    while True:
        play_game = input(f"Would you like to continue? y or n  \n")
        if play_game.lower() == "y":
            input(f"If you are ready press enter: \n")
            get_user_guess(battles)
            break
        elif play_game.lower() == "n":
            print(f"{player_name} chose not to play! Returning to start")
            main()
            exit()


main()
