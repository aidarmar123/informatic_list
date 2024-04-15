sentence=input("Sentence is ")
letter_gl=["a","e","i","o","u"]
count_gl=0
count_sl =0
for letter in sentence.lower().replace(" ",""):
    if letter in letter_gl:
        count_gl+=1
    elif letter.isdigit():
        continue
    else:
        count_sl+=1
print("Гласных" if count_gl>count_sl else "Согласных")