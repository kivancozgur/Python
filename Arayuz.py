from tkinter import *
import tkinter.messagebox
pencere = Tk()
pencere.title("Muğla Sıtkı Koçman Üniversite Kayıt Sistemi")
pencere.geometry('350x150+100+100')
Ad=Label(pencere,text="Ad")
Ad.grid(row=1,column=1,sticky=E)

Soyad=Label(pencere,text="Soyad")
Soyad.grid(row=2,column=1,sticky=E)


Kacinci=Label(pencere,text="Kaçıncı")
Kacinci.grid(row=3,column=1,sticky=E)

Adtext=Entry(pencere)
Adtext.grid(row=1,column=2)

Soyadtext=Entry(pencere)
Soyadtext.grid(row=2,column=2)


Kacincitext=Entry(pencere)
Kacincitext.grid(row=3,column=2)

def dialog():
    var = tkinter.messagebox.showinfo("Yeni Mail Oluşturuldu" , "Adtext hoi, dit is een test als je dit leest is het gelukt")
button2 = Button(pencere, text = " Mail ", command=dialog)
button2.grid(columnspan=4)

tkinter.messagebox.showinfo("Sistem Nasıl Çalışır", "Lorem Ipsum, dizgi ve baskı endüstrisinde kullanılan mıgır metinlerdir. Lorem Ipsum, adı bilinmeyen bir matbaacının bir hurufat numune kitabı oluşturmak üzere bir yazı galerisini alarak karıştırdığı 1500'lerden beri endüstri standardı sahte metinler olarak kullanılmıştır. Beşyüz yıl boyunca varlığını sürdürmekle kalmamış, aynı zamanda pek değişmeden elektronik dizgiye de sıçramıştır. 1960'larda Lorem Ipsum pasajları da içeren Letraset yapraklarının yayınlanması ile ve yakın zamanda Aldus PageMaker gibi Lorem Ipsum sürümleri içeren masaüstü yayıncılık yazılımları ile popüler olmuştur.")
pencere.mainloop()
