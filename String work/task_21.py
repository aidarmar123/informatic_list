sentence=input("Sentence is ")
longestword=max(sentence.split(),key=len)
print(sentence.replace(longestword," "))