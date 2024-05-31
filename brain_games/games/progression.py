import random
from brain_games.engine.start import start_game
# импорт двигателя игры

basic_question = "What number is missing in the progression?"


# получаем ряд чисел и значение пропущенного в нем элемента
def task_conditions():
    start_num = random.randint(1, 100)
    step = random.randint(1, 10)
    # определяем длину ряда чисел
    num_count = random.randint(5, 10)
    finish_num = start_num + step * (num_count - 1)
    num_list = []
    # формируем список из чисел, каждое принимается как строкa
    for n in range(start_num, finish_num + 1, step):
        num_list.append(str(n))
    # выбираем номер "секретного" элемента
    num_question = random.randint(0, len(num_list) - 1)
    result = num_list[num_question]
    num_list[num_question] = '..'
    question = f"{' '.join(num_list)}"
    return (question, result)


# запуск двигателя игры с атрибутами из task_conditions и базовым вопросом
def progression_game():
    start_game(basic_question, task_conditions)
