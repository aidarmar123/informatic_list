sentence=input("Suntence is ")
sum=0
for i in sentence:
    if i.isdigit():
        sum+=int(i)
print(sum)