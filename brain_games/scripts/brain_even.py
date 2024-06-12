#!/usr/bin/env pyhton3
import brain_games.games.even as even_game
from brain_games.engine.game_engine import run_game


def main():
    run_game(even_game)


if __name__ == '__main__':
    main()
