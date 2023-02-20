from random import randint

def gen_token():
    code = ""
    for i in range(6):
        x = randint(0, 9)
        code = code + str(x)
    return code