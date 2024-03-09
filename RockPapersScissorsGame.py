import random

def main():
    user_win_count = 0
    sys_win_count = 0

    print("Welcome User! This is Rock, Paper, Scissors game :)")
    print("If you don't know how to play Rock, Paper, Scissors,")
    print("Checkout Wikipedia for Game Rules and information: https://en.wikipedia.org/wiki/Rock_paper_scissors")
    print("Rules:")
    print("The game will be played 5 times; the one with a higher score at the end will win the game!")
    print("You have to choose any one option from the below options, and the computer will choose its own "
          "number hence resulting in the final conclusion of who won.")
    print("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors:")

    for i in range(1, 6):
        while True:
            try:
                user_in = int(input())
                if user_in not in [1, 2, 3]:
                    raise ValueError("Invalid input. Please choose 1, 2, or 3.")
                break
            except ValueError as e:
                print(e)

        sys_in = random.randint(1, 3)

        if sys_in == user_in:
            print("Draw")
        elif (user_in == 1 and sys_in == 3) or (user_in == 2 and sys_in == 1) or (user_in == 3 and sys_in == 2):
            print("You won this time!")
            user_win_count += 1
        else:
            print("You lost this time!")
            sys_win_count += 1

    if user_win_count > sys_win_count:
        print("\nCongratulations! You won the game :)")
    elif sys_win_count > user_win_count:
        print("\nYou lost the game :(")
    else:
        print("\nGame is a draw!")

if __name__ == "__main__":
    main()
