ad=input("AD : ")
soyad=input("SOYAD : ")
kacincikisi=int(input("Kaçıncı Kişi : "))
if kacincikisi==0 or kacincikisi==1:
    kacincikisi=""
a=ad.replace(" ","")
s=soyad.replace(" ","")
ad_kucuk = a.lower()
soyad_kucuk = s.lower()
ad_kucuk=ad.replace("ğ","g")
soyad_kucuk=soyad.replace("ğ","g")
ad_kucuk=ad.replace("ı","i")
soyad_kucuk=soyad.replace("ı","i")
ad_kucuk=ad.replace("ç","c")
soyad_kucuk=soyad.replace("ç","c")
ad_kucuk=ad.replace("ü","u")
soyad_kucuk=soyad.replace("ü","u")
ad_kucuk=ad.replace("ş","s")
soyad_kucuk=soyad.replace("ş","s")
ad_kucuk=ad.replace("ö","o")
soyad_kucuk=soyad.replace("ö","o")

posta = (ad_kucuk + soyad_kucuk + kacincikisi) + "@posta.mu.edu.tr"
print(posta)