import random

gizli = random.randint(1, 100)

while True:
    tahmin = int(input("1-100 arasında tahmin et: "))

    if tahmin < gizli:
        print("Daha büyük söyle!")

    elif tahmin > gizli:
        print("Daha küçük söyle!")

    else:
        print("🎉 Tebrikler, doğru bildin!")
        break
