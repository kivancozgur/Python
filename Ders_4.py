s1=input("Sınav1 : ")
s2=input("Sınav2 : ")
ort=(int(s1)+int(s2))/2
print("Ortalama : ",ort)
vize=int(s1)*0.40
final=int(s2)*0.60
yeniort=int(vize)+int(final)
print("Yeni Ortalama : ",yeniort)
if yeniort>50 and yeniort<60:
    yeniort+=5
elif yeniort>60 and yeniort<80:
    yeniort+=7
elif yeniort>80 and yeniort<100:
    yeniort+=10
elif yeniort<50:
    yeniort-=10
print("EKSTRALI ORTALAMA : ",yeniort)