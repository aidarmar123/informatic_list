
word_1=input("Введите слово: банан, яблоко, рыба, мясо. Вводите с маленькой буквы.")
english_words={"банан":"banana",
               "яблоко":"apple",
               "рыба":"fish",
               "мясо":"meat"}
try:
    print(english_words[word_1])
except:
    print("Error")