sentence=input("Sentence is ")
letter=input("Letter is ")
answer= list()
for word in sentence.split():
    if word[0].lower()==letter.lower():
        answer.append(word)
print(f"Count word started a {letter.upper()} is {len(answer)}")