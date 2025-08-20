# Bölüm 1 - Soru 1

ad = str(input("Adiniz: "))
yas = float(input("Yasiniz: "))
boy = float(input("Boyunuz (cm): "))

print(ad , yas , boy)


# Bölüm 1 - Soru 2

matematikNotu1 = float(input("Ilk sinav matematik notunuzu giriniz: "))
matematikNotu2 = float(input("Ikinci sinav matematik notunuzu giriniz: "))
matematikNotu3 = float(input("Ucuncu sinav matematik notunuzu giriniz: "))

matematik_ortalama = (matematikNotu1 + matematikNotu2 + matematikNotu3) / 3
print("Matematik ortalamaniz: " + str(matematik_ortalama) + "\n")

fizikNotu1 = float(input("Ilk sinav fizik notunuzu giriniz: "))
fizikNotu2 = float(input("Ikinci sinav fizik notunuzu giriniz: "))
fizikNotu3 = float(input("Ucuncu sinav fizik notunuzu giriniz: "))

fizik_ortalama = (fizikNotu1 + fizikNotu2 + fizikNotu3) / 3
print("Fizik ortalamaniz: " + str(fizik_ortalama) + "\n")

kimyaNotu1 = float(input("Ilk sinav kimya notunuzu giriniz: "))
kimyaNotu2 = float(input("Ikinci sinav kimya notunuzu giriniz: "))
kimyaNotu3 = float(input("Ucuncu sinav kimya notunuzu giriniz: "))

kimya_ortalama = (kimyaNotu1 + kimyaNotu2 + kimyaNotu3) / 3
print("Kimya ortalamaniz: " + str(kimya_ortalama) + "\n")

genel_ortalama = (fizik_ortalama + kimya_ortalama + matematik_ortalama) / 3

print("Genel Ortalamaniz: " + str(genel_ortalama))

# Bölüm 1 - Soru 3

ad_soyad = "Yusuf Buyukkartal"

ilk_harf = ad_soyad[0]
son_harf = ad_soyad[-1]
uzunluk = len(ad_soyad)
terstenYaz = ad_soyad[::-1]

print(ilk_harf)
print(son_harf)
print(uzunluk)
print(terstenYaz)





