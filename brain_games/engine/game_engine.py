import prompt
ROUNDS_COUNT = 3


def run_game(game):
    '''Greet and get know.'''
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!')
    # basic question of the game, each game has its own
    print(game.QUESTION)
    # starting a question cycle
    for i in range(ROUNDS_COUNT):
        question, result = game.get_task_conditions()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;( '
                  f'Correct answer was \'{result}\'.\n'
                  f'Let\'s try again, {name}!')
            break
        if i == 2:
            print(f'Congratulations, {name}!')
