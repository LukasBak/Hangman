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


def choose_random_battle():
    return random.choice(battles)

def main():
    word = choose_random_battle()
    print(word)

main()