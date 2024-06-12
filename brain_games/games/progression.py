import random

BASIC_QUESTION = "What number is missing in the progression?"
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100
MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 10
MIN_SEQUENCE_LEN = 5
MAX_SEQUENCE_LEN = 10


# get sequence of numbers and value of missing number
def get_task_conditions():
    start_num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    step = random.randint(MIN_DIFFERENCE, MAX_DIFFERENCE)
    num_count = random.randint(MIN_SEQUENCE_LEN, MAX_SEQUENCE_LEN)
    finish_num = start_num + step * (num_count - 1)
    num_list = []
    # get list of numbers
    for n in range(start_num, finish_num + 1, step):
        num_list.append(str(n))
    # get position of "secret" number
    num_question = random.randint(0, len(num_list) - 1)
    result = str(num_list[num_question])
    num_list[num_question] = '..'
    # get sequence as sting
    question = f"{' '.join(num_list)}"
    return (question, result)
