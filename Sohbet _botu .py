print("Merhaba! Ben basit bir sohbet botuyum.")

while True:
    mesaj = input("Sen: ").lower()

    if mesaj == "merhaba":
        print("Bot: Merhaba!")

    elif mesaj == "nasılsın":
        print("Bot: İyiyim, teşekkür ederim.")

    elif mesaj == "adın ne":
        print("Bot: Ben Python Botuyum.")

    elif mesaj == "çık":
        print("Bot: Görüşürüz!")
        break

    else:
        print("Bot: Bunu anlayamadım.")
