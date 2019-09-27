""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    cnt = 0
    low = 1
    high = 1000

    while low <= high:
        cnt += 1
        guess = get_int(low, high)  # get integer input
        if guess == answer:  # if the input same with the answer, show the guess count and finish the loop
            print("You got it! The hidden number is " + str(answer))
            print("It took you " + str(cnt) + " guess(es).")
            break
        elif guess < low or guess > high:  # if the input is out of the range
            print("You put the number that is out of the range.")
        elif guess < answer:  # if the input is wrong, adjust the range
            low = guess + 1
        elif guess > answer:
            high = guess - 1
        print("Wrong! Guess count: " + str(cnt))


def get_int(start, end):
    while True:
        try:
            temp = int(input("Enter your guess from " + str(start) + " to " + str(end) + ": "))
            break
        except ValueError as e:
            print("Entered value is not correct, try again. It should be integer.")
            print(f"[System message] : {e}")
        except KeyboardInterrupt as e:
            print("\nNo input taken.\n")
            print(f"[System message] : {e}")
        except:
            print("Something wrong... Restart the program.")
    return temp


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()
