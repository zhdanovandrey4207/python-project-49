#!/usr/bin/env pyhton3
import prompt
from random import randint


def parity_check(number):
    return True if number % 2 == 0 else False


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    count_wrong_ans = 0
    count_right_ans = 0
    while count_wrong_ans == 0 and count_right_ans < 3:
        next_number = randint(1, 100)
        print(f"Question: {next_number}")
        answer = prompt.string("Your answer: ")
        if parity_check(next_number) and answer == 'yes':
            count_right_ans += 1
            print("Correct!")
        elif parity_check(next_number) == False and answer == 'no':
            count_right_ans += 1
            print("Correct!")
        else:
            count_wrong_ans += 1
            if parity_check(next_number):
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
    if count_wrong_ans == 1:
        print(f"Let's try again, {name}!")
    else:
        print(f"Congratulations, {name}!")

def main():
    brain_even()

if __name__  == "__main__":
    main()
