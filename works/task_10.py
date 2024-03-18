number = input("Введите переменную n:")
sum = 0
factorial = 1
for char in number:
    if char.isdigit():
        sum += int(char)
        factorial*=int(char)
print(f"summa {sum} \nfactorial {factorial}")
