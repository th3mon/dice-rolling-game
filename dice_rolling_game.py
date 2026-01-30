import random

messages = {
    "question": "Roll the dice? (y/n): ",
    "dice_quantity": "How many dice you want to roll? (number): ",
    "invalid": "Invalid choice!",
    "thanks": "Thanks for playing!",
}


def roll_dice(dice_quantity: str):
    messages = {"error": "Quantity should be a number"}
    try:
        dice_quantity_as_number = int(dice_quantity)
        results = {"values": []}

        for _ in range(dice_quantity_as_number):
            results.get("values").append(str(get_d6_result()))

        return results
    except Exception:
        return {"error": messages.get("error")}


def get_d6_result():
    return random.randint(1, 6)


while True:
    choice = input(messages.get("question")).lower()

    if choice == "y":
        dice_quantity = input(messages.get("dice_quantity"))
        results = roll_dice(dice_quantity)

        if results.get("error"):
            print(results.get("error"))
        else:
            dice = ", ".join(results.get("values"))
            print(f"({dice})")

    elif choice == "n":
        print(messages.get("thanks"))

        break

    else:
        print(messages.get("invalid"))
