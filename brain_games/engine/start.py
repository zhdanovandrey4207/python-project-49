import prompt


# greeting and introduction
def start_game(BASIC_QUESTION, task_conditions):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    print(f"Hello, {name}!")
    # basic question of the game, each game has its own
    print(BASIC_QUESTION)
    right_answer_count = 0
    wrong_answer_count = 0
    # starting a question cycle
    while wrong_answer_count == 0 and right_answer_count < 3:
        question, result = task_conditions()
        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")
        if answer == str(result):
            right_answer_count += 1
            print("Correct!")
        else:
            wrong_answer_count += 1
            print(f"'{answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{result}'."
                  f"Let's try again, {name}!")
    if right_answer_count == 3:
        print(f"Congratulations, {name}!")
