#!/usr/bin/env pyhton3
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def main():
    welcome_user()


if __name__ == "__main__":
    main()
