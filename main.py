name_user = input("Привет тебе, Странник. Как тебя зовут? ")
print("Мне приятно знать твоё имя, ", name_user, "! Самое время отправится в путешествие!")

score = 0
artefact_one = False
artefact_two = False
artefact_three = False
list_of_arts = [artefact_three,
                artefact_two,
                artefact_one]

print (f""" {name_user} Ты начинаешь игру с 0 очков. В ходе игры ты будешь получать очки,
за которые ты сможешь приобрести не только интересные вещи, но и артефакты, которые 
помогут тебе достичь победы.

За каждый правильный ответ ты будешь получать очки:
За верный ответ на 1-ый вопрос:10 очков
За верный ответ на 2-ой вопрос:20 очков
За верный ответ на 3-ий вопрос:30 очков")

Итак, Первый вопрос: 
Два медвежонка нашли головку сыра. Они долго спорили, как её поделить, 
но никто не хотел уступать.Мимо пробегала Лиса. Узнав, в чем спор, она предложила 
помочь, разломив головку сыра на 2 части так, чтобы одна из них была полкилограмма, 
другая меньше. Затем она спросила, усмехаясь:
- Куски равны?
Жадные медвежата дали отрицательный ответ. Тогда лиса откусила от большей части , но так,
чтобы от неё остался кусок меньше,чем другая часть, и повторила вопрос.
И на этот раз медвежата сообщили, что получились неравные части. После этого лиса 
повторила откусывание еще 9 раз, каждый раз
откусывая одинаковое количество сыра. В результате остались маленькие кусочки, причем один
из них оказался на 20 граммов больше другого. Лиса заявила, что медвежатам трудно угодить.
Она отправила два кусочка в рот и, вильнув хвостом, скрылась в кустах.
Какова была масса головки сыра в граммах?""")
answer_one = input("Ваш ответ:")
if answer_one == "900":
    score += 10
    print("Не знаю, угадал ты или посчитал, но ты прав! Твои 10 очков и артефакт! Теперь твои очки:", score)
    artefact_one = True
else:
    print ("Неверно! Твои очки:", score)
print("""Теперь второй вопрос:
Сколько месяцев в году имеют 28 дней?""")
answer_two = input("Ваш ответ(число):")
if answer_two == "12":
    score += 20
    print("Не знаю, угадал ты или посчитал, но ты прав! Твои 20 очков и артефакт! Теперь твои очки:", score)
    artefact_two = True
else :
    print ("Неверно! Твои очки:", score)
print("""И, наконец, 3 вопрос:
Теннисные ракетка и мяч вместе стоят 1 евро и 10 центов. Теннисная ракетка на 1 евро дороже мяча.
Сколько стоит мяч?""")
answer_three = input("Ваш ответ(в центах):")
if answer_three == "5":
    score += 30
    print("Не знаю, угадал ты или посчитал, но ты прав! Твои 30 очков и артефакт! Теперь твои очки:", score)
    artefact_three = True
else :
    print ("Неверно! Твои очки:", score)
print("""Итак, игра закончилась. Твой счёт можешь увидеть выше. Можешь проследовать в магазин и купить 
себе что-нибудь ОДНО:
1. Молодильное яблоко - 13 points
2. Волшебный клубок - 27 points
3. Мороженное - 14 points
4. Ковер-самолёт - 30 очков.
5. Пропустить магазин""")
product = input("Вводите от 1 до 5:")
if product == "1" and score >= 13:
    score -= 13
    print("Хороший выбор! Твоя покупка - Яблоко! Теперь твой счёт:", score, ". Идём дальше!")
elif product == "2" and score >= 27:
    score -= 27
    print ("Хороший выбор! Твоя покупка - Волшебный клубок! Теперь твой счёт:", score, ". Идём дальше!")
elif product == "3" and score >= 14:
    score -= 14
    print ("Хороший выбор! Твоя покупка - Мороженное! Теперь твой счёт:", score, ". Идём дальше!")
elif product == "4" and score >= 30:
    score -= 30
    print ("Хороший выбор! Твоя покупка - Волшебный ковер! Теперь твой счёт:", score, ". Идём дальше!")
elif product == "5":
    print("Идём дальше!")
elif product == ("1","2","3","4"):
    print("У тебя не хватает денег!")
else:
    print("Ты не понял условия!")
if artefact_one and artefact_two and artefact_three:
    print("Ты победил! твой счёт:", score)
elif artefact_one and artefact_three:
    print("К сожалению, ты не собрал 2 артефакт! Твои очки",score)
elif artefact_one and artefact_two:
    print("Ты не собрал 3 артефакт. Твой счёт:", score)
elif artefact_two and artefact_three:
    print("Ты собрал всего 1 артефакт. Твой счёт:", score)
elif any(list_of_arts) == True :
    print("Собрал всего 1 артефакт...")
else:
    print("Ты проиграл. Иди учись!")
