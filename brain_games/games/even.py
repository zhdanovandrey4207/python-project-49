import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_even(number):
    '''Find out if number is even'''
    if number % 2 == 0:
        return True
    else:
        return False


def get_task_conditions():
    '''Get random number and find out if it's even'''
    num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    if is_even(num):
        result = 'yes'
    else:
        result = 'no'
    question = num
    return (question, result)
