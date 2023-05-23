# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются 
# друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если 
# с ритмом все не в порядке.

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

# А теперь коротко Суть(ТМ) задачи:
# С клавиатуры вводят поочередно строки, состоящие из подстрок, разделенных пробелом.
# Надо всего лишь подсчитать количество гласных в каждой подстроке.

# def is_our_word_cyrillic(our_word, points_cyril, points_latin):
#     kirillitsa = ("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
#     is_our_word_cyrillic_char = [char for char in kirillitsa if char in our_word]
#     if is_our_word_cyrillic_char:
#         points = points_cyril
#     else:
#         points = points_latin
#     return points

russian_vowels_characters = ("АЕЁИОУЫЭЮЯ")
our_phrases = input("Вводи кричалку, Винни: ").upper().split()
how_many_vowels = []
for phrase in our_phrases:
    vowels_in_phrase = 0
    for char in phrase:
        if char in russian_vowels_characters:
            vowels_in_phrase += 1
    how_many_vowels.append(vowels_in_phrase)
print(how_many_vowels)
if 0 in how_many_vowels:
    raise ValueError("Нет гласных в одной из фраз!")
if len(set(how_many_vowels)) == 1: 
    print("Парам пам-пам")
else:
    print("Пам парам" )