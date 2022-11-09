

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

    
deger_sayisi = int(input("""Kaç değer gireceksiniz?
                        2 değer için: 2'ye
                        3 değer için: 3'e
                        basınız: """))

if deger_sayisi == 2:

    deger_1=int(input("Birinci değeri giriniz:"))
    print(f"Birinci değer: {deger_1}")

    while True:
        deger_2=int(input("İkinci değeri giriniz:"))
        print(f"İkinci değer: {deger_2}")

        if islem == "/" and deger_2 == 0:
            print("Hatalı işlem. Bir sayıyı 0'a bölemezsiniz. Lütfen sıfırdan farklı bir değer giriniz.")
        else:
            break

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

            
elif deger_sayisi == 3:
    deger_1=int(input("Birinci değeri giriniz:"))
    print(f"Birinci değer: {deger_1}")

    while True:
        deger_2=int(input("İkinci değeri giriniz:"))
        print(f"İkinci değer: {deger_2}")

        deger_3=int(input("Üçüncü değeri giriniz:"))
        print(f"Üçüncü değer: {deger_3}")

        if islem == "/" and deger_2 == 0 or deger_3 == 0:
            print("Hatalı işlem. Bir sayıyı 0'a bölemezsiniz. Lütfen sıfırdan farklı bir değer giriniz.")
        else:
            break
            

        
    if islem == "+":
            sonuc=deger_1 + deger_2 + deger_3
            print("Sonuç:", sonuc)
    elif islem == "-":
            sonuc=deger_1 - deger_2 - deger_3
            print("Sonuç:", sonuc)
    elif islem == "*":
            sonuc=deger_1 * deger_2 * deger_3
            print("Sonuç:", sonuc)
    elif islem == "/":
            sonuc=deger_1 / deger_2 / deger_3
            print("Sonuç:", sonuc)