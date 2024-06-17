import random
import math

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def is_prime(num):
    '''Find out if number is prime'''
    square_root = round(math.sqrt(num))
    for i in range(2, square_root + 1):
        if num % i == 0:
            return False
    return True


def get_task_conditions():
    '''Get random number and find out if it's prime'''
    num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = num
    if is_prime(num):
        result = 'yes'
    else:
        result = 'no'
    return (question, result)
