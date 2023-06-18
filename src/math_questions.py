"""The file to create questions and answers for the game"""
# Importing modules
import random

# For now, will just generate basic addition questions
def question_generator():
    # The equations will be in the form: x + y = ans; where x is the be found, y and ans are both randomly generated
    # Will keep it double digit for now
    MAX = 50
    MIN = 1

    ans = random.randint(MIN, MAX)

    # Will also keep x positive for now
    y = random.randint(MIN, ans)
    x = ans - y

    # Generate the total options including the real answer
    no_opts = 4
    opts = {x}
    while len(opts) < no_opts:
        opts.add(random.randint(MIN,ans))

    # Randomly organize the options
    opts = list(opts)
    random.shuffle(opts)

    return((x, y, ans, opts))
