from modules.Colors import Colors


def hi():
    welcoming_text = str("Thank you for choosing our game! We wish you a lot of fun :)")
    print(f"{Colors.WELCOME}{welcoming_text}")
    print("*" * len(welcoming_text))
    print("To quit press ESC on your keyboard.")