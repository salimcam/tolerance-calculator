from tkinter import *
from tolerenceCalculator import *
from tkinter import messagebox


class CalculatorView():
    def __init__(self, master, frame):
        self.master = master
        self.master.geometry("400x500")
        self.frame = frame
        self.frame.pack()
        self.master.title("Tolerans Hesabı")

        self.cap = IntVar()
        self.delikKalite = IntVar()
        self.milKalite = IntVar()
        self.mil_tolerans_bolgesi = [
            "c", "d", "e", "f", "g", "r", "s", "t", "u", "v"]

        self.l1 = Label(frame, text="Çap:", font=('Times', 15, 'bold'))
        self.l2 = Label(frame, font=('Times', 15))
        self.l3 = Label(frame, text="Delik Kalitesi:",
                        font=('Times', 15, 'bold'))
        self.l4 = Label(frame, font=('Times', 15))
        self.l5 = Label(frame, text="Mil Tolerans Bölgesi:",
                        font=('Times', 15, 'bold'))
        self.l6 = Label(frame, font=('Times', 15))

        self.cap_secim = Scale(frame, from_=31, to=80, orient=HORIZONTAL,
                               variable=self.cap, length=250, command=self.capSecimi)
        self.delik_kalitesi = Scale(frame, from_=5, to=9, orient=HORIZONTAL,
                                    variable=self.delikKalite, length=250, command=self.delikKalitesiSecimi)
        self.mil_kalitesi = Scale(frame, from_=5, to=9, orient=HORIZONTAL,
                                  variable=self.milKalite, length=250)

        self.lb = Listbox(frame, height=4, selectmode=SINGLE)
        for i in self.mil_tolerans_bolgesi:
            self.lb.insert(END, i)
        self.lb.bind('<<ListboxSelect>>', self.milToleransBolgesiSecimi)

        self.b = Button(frame, text="Calculate", command=self.calculate)

        self.l1.grid(row=0, column=0, sticky='', pady=2)
        self.l2.grid(row=1, column=0, sticky='', pady=2)
        self.cap_secim.grid(row=2, column=0, sticky=W, pady=2)
        self.l3.grid(row=3, column=0, sticky='', pady=2)
        self.l4.grid(row=4, column=0, sticky='', pady=2)
        self.delik_kalitesi.grid(row=5, column=0, sticky=W, pady=2)
        self.l5.grid(row=6, column=0, sticky='', pady=2)
        self.l6.grid(row=7, column=0, sticky='', pady=2)
        self.lb.grid(row=8, column=0, sticky='', pady=2)
        self.mil_kalitesi.grid(row=9, column=0, sticky=W, pady=2)
        self.b.grid(row=10, column=0, sticky='', pady=2)

    def capSecimi(self, *args):
        self.l2.config(text=str(self.cap.get()) + " mm")

    def delikKalitesiSecimi(self, *args):
        self.l4.config(text="H " + str(self.delikKalite.get()))

    def milToleransBolgesiSecimi(self, event):
        w = event.widget
        idx = int(w.curselection()[0])
        value = w.get(idx)
        self.secilen_mil_tolerans_bolgesi = value
        self.l6.config(text=value + str(self.milKalite.get()))

    def calculate(self):
        #print(cap.get(), delikKalite.get(),milKalite.get(), secilen_mil_tolerans_bolgesi)
        soru1 = tolerence_calculator(
            self.cap.get(), self.delikKalite.get(), self.milKalite.get(), self.secilen_mil_tolerans_bolgesi)
        soru1.delik_td()
        soru1.mil_td()
        soru1.mil_deger()
        result = soru1.calculate_tolerance()
        resultText = [f"Geçme Tipi: {result[0]}",
                      f"Delik Maksimum Çapı: {result[1]}mm", f"Delik Minimum Çapı: {result[2]}mm", f"Mil Maksimum Çapı: {result[3]}mm", f"Mil Minimum Çapı: {result[4]}mm", f"Sonuç: {result[5]}"]
        messagebox.showinfo("showinfo", "\n".join(resultText))
