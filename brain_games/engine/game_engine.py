import prompt


# greeting and introduction
def run_game(specific_game):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!')
    # basic question of the game, each game has its own
    print(specific_game.BASIC_QUESTION)
    right_answer_count = 0
    # starting a question cycle
    while right_answer_count < 3:
        question, result = specific_game.get_task_conditions()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            right_answer_count += 1
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;( '
                  f'Correct answer was \'{result}\'.\n'
                  f'Let\'s try again, {name}!')
            break
        if right_answer_count == 3:
            print(f'Congratulations, {name}!')
