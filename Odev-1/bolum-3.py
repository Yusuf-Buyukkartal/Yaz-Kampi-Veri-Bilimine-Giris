# Bolum 3 - Soru 9

# urun1 = float(input("ilk urunun fiyatini giriniz: "))
# urun2 = float(input("ikinci urunun fiyatini giriniz: "))
# urun3 = float(input("ucuncu urunun fiyatini giriniz: "))

# toplam_fiyat = urun1 + urun2 + urun3

# indirim = (toplam_fiyat > 200) * (toplam_fiyat * 0.10)


# son_fiyat = toplam_fiyat - indirim


# print("Toplam fiyat:", toplam_fiyat, "TL")
# print("Ödenecek tutar:", son_fiyat, "TL")

# Bölüm 3 - Soru 10

guncel_yil = 2025
dogumYili = int(input("Dogum yilinizi giriniz: "))

yas = guncel_yil - dogumYili

sonuc = (yas < 12) * 0 + (13 <= yas <= 17) * 1 + (yas >= 18) * 2


mesajlar = ["Çocuksunuz" , "Ergensiniz" , "Yetişkinsiniz"]

print(mesajlar[sonuc])