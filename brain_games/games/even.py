import random
from brain_games.engine.start import start_game
# импорт двигателя игры

basic_question = 'Answer "yes" if the number is even, otherwise answer "no".'


# получаем рандомное число и правильный ответ о его четности
def task_conditions():
    num = random.randint(1, 100)
    if num % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    question = str(num)
    return (question, result)


# запуск двигателя игры с атрибутами из task_conditions и базовым вопросом
def even_game():
    start_game(basic_question, task_conditions)
