import random
import math

QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


def get_task_conditions():
    '''Get 2 numbers and their greatest common divider'''
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = f'{num1} {num2}'
    result = str(math.gcd(num1, num2))
    return (question, result)
