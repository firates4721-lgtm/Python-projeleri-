import random

secenekler = ["taş", "kağıt", "makas"]

bilgisayar = random.choice(secenekler)

oyuncu = input("Taş, Kağıt veya Makas seç: ").lower()

print("Bilgisayar:", bilgisayar)

if oyuncu == bilgisayar:
    print("Berabere!")

elif (oyuncu == "taş" and bilgisayar == "makas") or \
     (oyuncu == "kağıt" and bilgisayar == "taş") or \
     (oyuncu == "makas" and bilgisayar == "kağıt"):
    print("Kazandın!")

elif oyuncu in secenekler:
    print("Kaybettin!")

else:
    print("Geçersiz seçim!")
