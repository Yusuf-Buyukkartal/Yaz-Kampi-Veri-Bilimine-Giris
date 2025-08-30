# Soru 1 – Sayı Analizi 

sayi = int(input("sayi giriniz: "))

if sayi > 0:
    if sayi % 2 == 0:
        print("Girdiginiz sayi pozitif bir çift sayidir.")
    else:
        print("Girdiginiz sayi pozitif bir tek sayidir.")
elif sayi < 0:
    if sayi % 2 == 0:
        print("Girdiginiz sayi negatif bir çift sayidir.")
    else:
        print("Girdiginiz sayi negatif bir tek sayidir.")
else:
    print("Girdiginiz sayi sifirdir.")

# Soru 2 – Harf Frekansı (String)

kelime = input("kelime giriniz: ")
harfler = {
    "a": 0 , "b": 0 ,"c": 0 ,"ç": 0 ,"d": 0 ,"e": 0 ,"f": 0 , "g": 0 ,"ğ": 0 ,
    "h": 0 ,"ı": 0 ,"i": 0 ,"j": 0 , "k": 0 ,"l": 0 ,"m": 0 ,"n": 0 ,"o": 0 ,
    "ö": 0 , "p": 0 ,"r": 0 ,"s": 0 ,"ş": 0 ,"t": 0 ,"u": 0 , "ü": 0 ,"v": 0 ,
    "y": 0 ,"z": 0 ,
    
}

for harf in harfler:
    for eleman in kelime:
        if harf == eleman:
            harfler[harf] += 1

data = {}
for harf, adet in harfler.items():
    if adet > 0:
        data[harf] = adet

print(data)

# Soru 3 – Şifre Kontrolü (String Metotları)

password = input("sifrenizi olusturunuz: ")


# Koşullar için başlangıç değerleri
min_uzunluk = 8
has_upper = False
has_digit = False

# Her karakteri tek tek kontrol et
for harf in password:
    if harf.isupper():   # Büyük harf mi?
        has_upper = True
    if harf.isdigit():   # Rakam mı?
        has_digit = True

# Uzunluk kontrolü
uzunluk_ok = len(password) >= min_uzunluk

# Sonuç
if uzunluk_ok and has_upper and has_digit:
    print("Şifre kabul edildi ✅")
else:
    print("Şifre reddedildi ❌ Eksik olan koşullar:")
    if not uzunluk_ok:
        print(f"- En az {min_uzunluk} karakter olmalı (şu an {len(password)} karakter).")
    if not has_upper:
        print("- En az 1 büyük harf olmalı.")
    if not has_digit:
        print("- En az 1 rakam olmalı.")

# Soru 4 – Liste İşlemleri 

sayilar = [12, 4, 9, 25, 30, 7, 18]

toplam = 0

for sayi in sayilar:
    toplam = toplam + sayi
   
ortalama = toplam / len(sayilar)

print(ortalama)

ortalamadanBuyukler = []
for sayi in sayilar:
    if sayi > ortalama:
         ortalamadanBuyukler.append(sayi)

print(ortalamadanBuyukler)

# Soru 5 – Nested Loop (Desen) 

yıldız = 1
sınır = 6

while yıldız < sınır:
    print("*" * yıldız)
    yıldız += 1

    




   


    
