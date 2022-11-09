

while True:
    islem=input("""Lütfen yapmak istediğiniz işlemi giriniz.
            Toplama için: +
            Çıkarma için: -
            Çarpma için: *
            Bölme için: /
            Yapmak istediğiniz işlem için belirtilen tuşlardan birine basınız:""")

    if islem == "+":
        print("Yapmak istediğiniz islem: {} işlemidir.".format("Toplama"))
        break
    elif islem == "-":
        print("Yapmak istediğiniz islem: {} işlemidir.".format("Çıkarma"))
        break
    elif islem == "*":
        print("Yapmak istediğiniz islem: {} işlemidir.".format("Çarpma"))
        break
    elif islem == "/":
        print("Yapmak istediğiniz islem: {} işlemidir.".format("Bölme"))
        break
    else:
        print("Hatalı işlem yapıldı. Lütfen belirtilen tuşlardan birine basınız.")

    

deger_1=int(input("Birinci değeri giriniz:"))
print(f"Birinci değer: {deger_1}")

deger_2=int(input("İkinci değeri giriniz:"))
print(f"İkinci değer: {deger_2}")


if islem == "+":
        sonuc=deger_1 + deger_2
        print("Sonuç:", sonuc)
elif islem == "-":
        sonuc=deger_1 - deger_2
        print("Sonuç:", sonuc)
elif islem == "*":
        sonuc=deger_1 * deger_2
        print("Sonuç:", sonuc)
elif islem == "/":
        sonuc=deger_1 / deger_2
        print("Sonuç:", sonuc)