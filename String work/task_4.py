sentence= input("Sentence is ")
words = sentence.strip()
words = [chr(ord(word)-10) for word in words]
print(" ".join(words))
