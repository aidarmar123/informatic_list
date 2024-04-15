sentence=input("Sentence is ")
print(sentence.replace(sentence.__getitem__(slice(sentence.index("'",sentence.rindex("'")))),"  "))