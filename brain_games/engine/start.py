import prompt
import time


# приветствие и знакомство
def start_game(basic_question, task_conditions):
    name = prompt.string("Welcome to the Brain Games!\n"
                         "May I have your name? ")
    time.sleep(1)
    print(f"Hello, {name}!")
    time.sleep(1)
# базовый вопрос игры (задается один раз, в каждом виде игры - свой
    time.sleep(1)
    print(basic_question)
# счетчики правильных и неправильных ответов
    right_ans_count = 0
    wrong_ans_count = 0
# запуск цикла вопросов
    while wrong_ans_count == 0 and right_ans_count < 3:
        time.sleep(1)
        question, result = task_conditions()
        print(f"Question: {question}")
        time.sleep(1)
        answer = prompt.string("Your answer: ")
        time.sleep(1)
        if answer == str(result):
            right_ans_count += 1
            print("Correct!")
        else:
            wrong_ans_count += 1
            print(f"'{answer}' is wrong answer ;(.\n"
                  f"Correct answer was '{result}'.")
            time.sleep(1)
            print(f"Let's try again, {name}!")
    if right_ans_count == 3:
        time.sleep(1)
        print(f"Congratulations, {name}!")
