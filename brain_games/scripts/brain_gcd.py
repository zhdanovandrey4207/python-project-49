#!/usr/bin/env pyhton3
from brain_games.games.gcd import BASIC_QUESTION, get_task_conditions
from brain_games.engine.start import start_game


def main():
    get_task_conditions()
    start_game(BASIC_QUESTION, get_task_conditions)


if __name__ == "__main__":
    main()
