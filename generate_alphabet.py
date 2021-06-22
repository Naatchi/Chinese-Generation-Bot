import random
from lists import characters

def generate_alp():

    output = open("output.txt","w", encoding="utf-8")


    phrase_len = random.choice(range(1,8))

    char_len = random.choice(range(1,3))

    for _ in range(phrase_len):
        for _ in range(char_len):
            print(random.choice(characters))
            output.write(random.choice(characters))
generate_alp()