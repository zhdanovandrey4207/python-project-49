import random

BASIC_QUESTION = 'What is the result of the expression?'
MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 100


# get arithmetic expression with random numbers
def get_task_conditions():
    num1 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    num2 = random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{num1} {operator} {num2}'
    if operator == '+':
        result = str(num1 + num2)
    elif operator == '-':
        result = str(num1 - num2)
    elif operator == '*':
        result = str(num1 * num2)
    return (question, result)
