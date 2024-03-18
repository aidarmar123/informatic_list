import random

new_list = list(range(1,101))
random_list = random.sample(new_list,10)
remove_pos= int(input("Number: "))
print(random_list)
print(random_list.count(remove_pos))