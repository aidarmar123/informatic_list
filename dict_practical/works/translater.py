from googletrans import Translator
input_word = input("Слово: ")

input_country = input("Страна ")

en_word = Translator().translate(input_word,dest=input_country)
print(en_word.extra_data['translation'][0][0])