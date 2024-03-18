from function.random_list import create_list
spisok=list(range(1,10))
ribka=int(input("Введите любое число:"))
spisok.append(ribka)
print(spisok)
print(create_list(3).append(ribka))