#!/usr/bin/env pyhton3
import brain_games.games.prime as prime_game
from brain_games.engine.game_engine import run_game


def main():
    run_game(prime_game)


if __name__ == '__main__':
    main()
