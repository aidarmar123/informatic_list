import random


def create_list(count):
    list = random.sample(list(range(1, 100)), count)
    return list
