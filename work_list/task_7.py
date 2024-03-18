import random

new_list = list(range(1,101))
random_list = random.sample(new_list,10)
random_list.sort()
print(random_list)