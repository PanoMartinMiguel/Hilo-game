import random as r

play_again = "y"

while play_again == "y":
    random_num = r.randint(1, 100)

    guess = input("Enter a Number: ")

    while int(guess) != random_num:
        print("Incorrect")
        if int(guess) > random_num:
            print("Too High")
        else:
            print("Too Low")

        guess = input("Enter a Number: ")
    print("Congratulations! You got it!")
    play_again = input("Do you want to play again? (Y/N)")