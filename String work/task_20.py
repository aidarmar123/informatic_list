sentence=input("Sentence is ")
print("".join([word for word in sentence if not word.isdigit()]))
