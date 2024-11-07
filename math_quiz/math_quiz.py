import random


def random_integer(min, max):
    """
    Generates a random integer from the given range

    args:
        min : lower bound of the range
        max : the upper bound of the range for the randint function

    returns:
        int: an random integer between min and max
    """
    return random.randint(min, max)


def random_operator():
    """
    Selects a random operator

    returns:
        str: A operator from the list (['+', '-', '*'])
    """
    return random.choice(['+', '-', '*'])


def calculator(num1, num2, operator):
    """
    Solves the problem for the given numbers with the operator

    Args:
        num1: 1st number
        num2: 2nd number
        operator: an arthmatic operator
    return:
        tuple: a tuple containing the answer(int) and problem(string)
    """
    #
    problem = f"{num1} {operator} {num2}"
    if operator == '+': answer = num1 + num2
    elif operator == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    The main function where the user answers the quetions and the functions checks the ans and gives the score at end.
    """
    score = 0
    turns = 5 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(turns):
        #generating random int values and selecting a random operator
        num1 = random_integer(1, 10); num2 = random_integer(1, 5); operator = random_operator() 

        problem, answer = calculator(num1, num2, operator)
        #Displaying the question
        print(f"\nQuestion: {problem}")

        #Checking if the input is int or not
        try:
            user_answer = int(input("Your answer: "))
        except:
            print("\nEnter an integer")
            continue #avoids the iteration if userInput is not integer
        
        #Check the ans and increments the score or not
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
            
    print(f"\nGame over! Your score is: {score}/{turns}")

if __name__ == "__main__":
    math_quiz()
