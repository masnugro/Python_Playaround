import random
geheime_zahl = random.randint(1, 10)
print("Ich denke an eine nummer zwischen 1 und 10.")
while True:
    ratte = int(input("dein ratte: "))
    if ratte == geheime_zahl:
        print("richtig!")
        break
    elif ratte < geheime_zahl:
        print("zu niedrig")
    else:
        print("zu hoch")
