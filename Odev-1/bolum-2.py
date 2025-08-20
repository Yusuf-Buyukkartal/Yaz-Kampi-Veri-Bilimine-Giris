# Bölüm 2 - Soru 4

sayi1 = int(input("1. sayiyi giriniz: "))
sayi2 = int(input("2. sayiyi giriniz: "))

toplama = sayi1 + sayi2
cikarma = sayi1 - sayi2
carpma = sayi1 * sayi2
bolme = sayi1 / sayi2
kalan = sayi1 % sayi2

print(toplama)
print(cikarma)
print(carpma)
print(bolme)
print(kalan)

# Bölüm 2 - Soru 5

ortalama = int(input("ortalamanizi giriniz: "))

sonuc = ["Kaldı", "Geçti"][ortalama > 50]


print("Sonuç:", sonuc)

# Bölüm 2 - Soru 6

yas = int(input("Yasinizi Giriniz: "))

sonuc = ["Ehliyet alamazsiniz." , "Ehliyet alabilirsiniz."][yas >= 18]

print(sonuc)
# Bölüm 2 - Soru 7

urun_fiyati = float(input("Urunun Fiyatini Giriniz: "))
indirim_orani = 0.20

indirimli_fiyat = urun_fiyati - (urun_fiyati * indirim_orani)

print("urunun indirimli fiyati: " + str(indirimli_fiyat))

# Bölüm 2 - Soru 8

devamsizlik_hakki = 5
gecer_not = True

devamsizlik = int(input("yaptiginiz devamsizligi giriniz: "))

dersten_gecer = (devamsizlik <= devamsizlik_hakki) and gecer_not
print("Dersten gecti mi?" , dersten_gecer)