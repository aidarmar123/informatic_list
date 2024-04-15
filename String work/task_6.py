sentence=input("Sentence is ")
count = 0
longest_word = max(sentence.split(),key=len)
for word in sentence.split():
    if len(word)==len(longest_word):
        count+=1
print(f"The longest word is {longest_word}\nThe count similar longest word is {count}")
