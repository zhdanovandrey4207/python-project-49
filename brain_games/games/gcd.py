import random
import math
from brain_games.engine.start import start_game
# импорт двигателя игры

basic_question = "Find the greatest common divisor of given numbers."


# получаем рандомное выражение и его правильный результат
def task_conditions():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    result = math.gcd(num1, num2)
    return (question, result)


# запуск двигателя игры с атрибутами из task_conditions и базовым вопросом
def gcd_game():
    start_game(basic_question, task_conditions)
