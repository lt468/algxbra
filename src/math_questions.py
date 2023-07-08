"""The file to create questions and answers for the game"""
# Importing modules
import random

def question_generator_easy():
    MAX = 20
    MIN = 1

    ans = random.randint(MIN, MAX)
    y = random.randint(MIN, ans)
    x = ans - y

    # Generate options list
    opts = [x]
    while len(opts) < 4:
        opt = random.randint(MIN, MAX)
        if opt not in opts:
            opts.append(opt)

    # Fun learning point: I was previously using this method of generating the options list
    # no_opts = 4
    # opts = {x}
    # while len(opts) < no_opts:
    #     opts.add(random.randint(MIN, ans))
    # Which caused an infinite loop and I believe it is to do with shuffling the opts as it was set (a set is always ordered by definition)

    random.shuffle(opts)

    return (x, y, ans, opts)
