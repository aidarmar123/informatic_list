sentence=input("Sentence is ")
answer = True
for i in range(len(sentence)):
    if sentence[i] != "(" or ")" != sentence[-(i+1)]:
        answer = False

print(answer)


