import random


def create_list(count):
    empty_list=list(range(1,101))
    list_random = random.sample(empty_list, count)
    return list_random
