from tkinter import *

def show_entry_fields():
    a = e1.get().replace(" ", "")
    s = e2.get().replace(" ", "")
    ak = a.lower()
    sk = s.lower()
    akt = ak.replace("ğ", "g")
    skt = sk.replace("ğ", "g")
    akt1 = akt.replace("ı", "i")
    skt1 = skt.replace("ı", "i")
    akt2 = akt1.replace("ç", "c")
    skt2 = skt1.replace("ç", "c")
    akt3 = akt2.replace("ü", "u")
    skt3 = skt2.replace("ü", "u")
    akt4 = akt3.replace("ş", "s")
    skt4 = skt3.replace("ş", "s")
    akt5 = akt4.replace("ö", "o")
    skt5 = skt4.replace("ö", "o")
    posta = (akt5 + skt5) + "@posta.mu.edu.tr"
    print("AD: %s\nSOYAD: %s\nMAIL: %s" % (e1.get(), e2.get(),posta))

pencere = Tk()
pencere.title("MSKU Öğrenci Kaydı")
pencere.geometry("300x150")
Label(pencere, text="AD").grid(row=0,pady=15,padx=25)
Label(pencere, text="SOYAD").grid(row=1)

e1 = Entry(pencere)
e2 = Entry(pencere)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(pencere, text='Kaydet', command=show_entry_fields).grid(columnspan=6,pady=15)

mainloop()
