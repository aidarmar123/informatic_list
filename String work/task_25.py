slovo=input("Введите слово с буквой А:")
if slovo.__contains__("а"):
    print(slovo.replace("а","о"))
else:
    print("Буквы А нет")