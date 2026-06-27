print("=== Hesap Makinesi ===")

sayi1 = float(input("Birinci sayıyı gir: "))
islem = input("İşlem (+, -, *, /): ")
sayi2 = float(input("İkinci sayıyı gir: "))

if islem == "+":
    print(sayi1 + sayi2)

elif islem == "-":
    print(sayi1 - sayi2)

elif islem == "*":
    print(sayi1 * sayi2)

elif islem == "/":
    if sayi2 != 0:
        print(sayi1 / sayi2)
    else:
        print("0'a bölünemez!")

else:
    print("Geçersiz işlem!")
