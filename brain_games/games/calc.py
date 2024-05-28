import random
from brain_games.engine.start import start_game
# импорт двигателя игры

basic_question = "What is the result of the expression?"


# получаем рандомное выражение и его правильный результат
def task_conditions():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return (question, result)


# запуск двигателя игры с атрибутами из task_conditions и базовым вопросом
def calc_game():
    start_game(basic_question, task_conditions)
