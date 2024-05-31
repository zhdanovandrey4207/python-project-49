import random
import math
from brain_games.engine.start import start_game
# импорт двигателя игры

basic_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# получаем число и ответ, простое ли оно
def task_conditions():
    result = 'yes'
    num = random.randint(1, 100)
    great_div = round(math.sqrt(num))
    for i in range(2, great_div + 1):
        if num % i == 0:
            result = 'no'
            break
    question = num
    return (question, result)


# запуск двигателя игры с атрибутами из task_conditions и базовым вопросом
def prime_game():
    start_game(basic_question, task_conditions)
