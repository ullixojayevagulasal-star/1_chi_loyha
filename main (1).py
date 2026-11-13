import random
from datetime import datetime


def salomlash(ism):
    soat = datetime.now().hour
    if soat < 12:
        vaqt = "Xayrli tong"
    elif soat < 18:
        vaqt = "Xayrli kun"
    else:
        vaqt = "Xayrli kech"
    return f"{vaqt}, {ism}!"


GAPLAR = [
    "Har bir katta dastur bitta print() dan boshlangan.",
    "Kod yozish - kompyuterga o'zbekcha emas, lekin juda aniq gapirishni o'rganish.",
    "Xato (bug) chiqsa xafa bo'lmang, bu dasturchining eng yaqin do'sti.",
    "Bugun Hello World, ertaga o'z botingiz va saytingiz!",
    "Dasturchi qahva ichadi, kod yozadi, xato topadi, yana qahva ichadi.",
]


def main():
    print("=" * 40)
    print("   HELLO, WORLD!  Salom, Dunyo!")
    print("=" * 40)

    ism = input("Ismingiz nima? ").strip() or "do'stim"
    print(salomlash(ism))
    print("Birinchi kodingiz ishladi!")
    print()
    print("Bugungi gap:", random.choice(GAPLAR))


if __name__ == "__main__":
    main()
