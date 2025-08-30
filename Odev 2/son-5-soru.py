# Soru 6 – While Döngüsü

# liste = []
# while True:
#     sayi = int(input("sayı giriniz: "))
#     liste.append(sayi)
#     if sayi == 0:
#         break

# toplam = 0
# for sayi in liste:
#     toplam = toplam + sayi

# print(f" girdiginiz sayilarin listesi: {liste}")
# print(f" girdiginiz sayilarin toplami: {toplam}")


# Soru 7 – Palindrom Kontrolü

# kelime = input("kelime giriniz: ")

# if kelime == kelime[::-1]:
#     print("Girdiginiz kelime palindrom bir kelimedir")

# else:
#     print("Girdiginiz kelime palindrom bir kelime degildir.")

# Soru 8 – List Comprehension

# sayilar = 0
# birdenYuze = []

# while sayilar < 100:
#     sayilar += 1
#     birdenYuze.append(sayilar)
    

# uc_ve_bese_bolunenler = [sayi for sayi in birdenYuze if sayi % 3 == 0 and sayi % 5 == 0]

# sayilarin_karesi = []

# for eleman in uc_ve_bese_bolunenler:
#     karesi = eleman * eleman
#     sayilarin_karesi.append(karesi)


# print(sayilarin_karesi)

# Soru 9 – String İşlemleri

# cumle = input("Cümle giriniz: ")

# ayrilmis = cumle.split()

# yeniString = ""   # boş string ile başlıyoruz

# for kelime in ayrilmis:
#     yeniString = yeniString + kelime.capitalize() + " "

# print(yeniString)

# Mini Proje – Film Yorumu Analizi
yorumlar = []

i = 0
while i<5:
    yorum = input("yorumunuzu giriniz: ")
    yorumlar.append(yorum)
    i += 1

uzunluklar = []

for yorum in yorumlar:
    uzunluklar.append(len(yorum))

uzunluklar = sorted(uzunluklar ,reverse=True)

print(f"Toplam yorum sayısı: {len(yorumlar)}")




enUzun = uzunluklar[0]
enKısa = uzunluklar[-1]

for yorum in yorumlar:
    if len(yorum) == enUzun:
      print(f"en uzun yorum: {yorum}")

    if len(yorum) == enKısa:
      print(f"En kısa yorum: {yorum}")

toplam = 0
for sayi in uzunluklar:
   toplam = toplam + sayi
   
ortUzunluk = toplam / len(yorumlar)

print(f"Ortalama uzunluk: {ortUzunluk}")


sayac = 0

for yorum in yorumlar:
    # küçük harfe çevir (büyük/küçük farkı olmasın diye)
    yorum_kucuk = yorum.lower()
    
    # eğer 'iyi' geçiyorsa sayacı artır
    if "iyi" in yorum_kucuk:
        sayac += 1

print("İyi kelimesi geçen yorum sayısı:", sayac)


    
        



