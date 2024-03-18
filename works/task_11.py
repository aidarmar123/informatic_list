sum=0
count=int(input("Введите колличество резисторов:"))
for i in range (count):
    resistance=int(input("Введите сопротивление резистора:"))
    sum+=1/resistance
print(sum)
