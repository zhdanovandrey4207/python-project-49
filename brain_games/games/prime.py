import random
import math

BASIC_QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


# find out if number is prime
def is_prime(num):
    square_root = round(math.sqrt(num))
    for i in range(2, square_root + 1):
        if num % i == 0:
            break
            return False
        else:
            return True


# get random number and find out if it's prime
def get_task_conditions():
    num = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    question = num
    if is_prime(num):
        result = 'yes'
    else:
        result = 'no'
    return (question, result)
