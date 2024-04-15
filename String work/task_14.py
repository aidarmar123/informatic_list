sentence=input("Введите строку ")
count=0
for word in sentence.split():
    if word.lower().count("е")==3:
        count+=1
print(count)