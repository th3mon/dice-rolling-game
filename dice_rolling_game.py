import random

messages = {
    "question": "Roll the dice? (y/n): ",
    "invalid": "Invalid choice!",
    "thanks": "Thanks for playing!",
}


def get_d6_result():
    return random.randint(1, 6)


while True:
    choice = input(messages.get("question")).lower()

    if choice == "y":
        dice1 = get_d6_result()
        dice2 = get_d6_result()

        print(f"({dice1} {dice2})")

    elif choice == "n":
        print(messages.get("thanks"))

        break

    else:
        print(messages.get("invalid"))
