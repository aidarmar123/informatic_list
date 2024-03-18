new_list = list(range(1,21))
remove_pos= int(input("Position: "))

if remove_pos < len(new_list):
    new_list.pop(remove_pos)
print(new_list)