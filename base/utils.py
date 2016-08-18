def gen_random():
    import random
    import string
    random = random.SystemRandom()
    print(''.join(random.choice(string.ascii_letters) for _ in range(32)))


if __name__ == '__main__':
    gen_random()
