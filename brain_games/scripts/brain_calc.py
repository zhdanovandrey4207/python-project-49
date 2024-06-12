#!/usr/bin/env pyhton3
import brain_games.games.calc as calc_game
from brain_games.engine.game_engine import run_game


def main():
    run_game(calc_game)


if __name__ == '__main__':
    main()
