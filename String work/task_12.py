sentence=input("Sentence is ")
letter="е"
answer= list()
for word in sentence.split():
    if word.__contains__(letter):
        answer.append(word)
print(f"Count word started a {letter.upper()} is {len(answer)}")