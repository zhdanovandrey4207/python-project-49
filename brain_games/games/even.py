import random


BASIC_QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


# find out if number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# get random number and find out if it's even
def get_task_conditions():
    num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(num):
        result = 'yes'
    else:
        result = 'no'
    question = num
    return (question, result)
