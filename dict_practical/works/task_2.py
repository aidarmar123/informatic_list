word_1=input("Напишите страну на английском языке:")
english_words={"China":"你好，程序员",
               "USA":"Hello, programmer",
               "Russia":"Привет, программист",
               "France":"Bonjour programmeur",
               "Germany":"Hallo Programmierer"}
try:
    print(english_words[word_1])
except:
    print("Error")