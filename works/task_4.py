n=int(input("Введите переменную n:"))
sum=0
for i in range (1,n+1):
    sum+=1/2**i
print(round(sum, 2))