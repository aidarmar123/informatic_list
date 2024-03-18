import random
new_list = list(range(1,21))
remove_el= int(input("Number: "))
print(new_list)
if remove_el in new_list:
    new_list.remove(remove_el)
print(new_list)
