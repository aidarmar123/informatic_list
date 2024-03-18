n=int(input("Введите переменную n:"))
numbers=[1,5,10,16,23]
def max_number(input_num):
    for number in numbers:
        while number>input_num:
            return number

print(max_number(n))