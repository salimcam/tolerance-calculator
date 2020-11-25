from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile
import pandas
import random
from tolerenceCalculator import *


class HomeworkView():
    def __init__(self, master, frame):
        self.master = master
        self.master.geometry("300x50")
        self.frame = frame
        self.frame.pack()
        self.master.title("Tolerans Ödevi")

        self.btn = Button(frame, text='Öğrenci Listesini Ekleyin',
                          command=lambda: self.open_file())
        self.btn.pack(side=TOP, pady=10)

    def open_file(self):
        file = askopenfile(filetypes=[("Excel files", ".xlsx .xls")])
        #file = askopenfile(mode='r')
        if file is not None:
            students = pandas.read_excel(file.name, usecols=[
                'Öğrenci No', ' Adı Soyadı'])
            cap = random.randint(31, 81)
            delikToleransBolgesi = "H"
            milToleransBolgeleri = ["c", "d", "e",
                                    "f", "g", "r", "s", "t", "u", "v"]
            kaliteler = [6, 7, 8, 9]
            # print(cap)
            sorular = []
            gecmeTipi = []
            DMax = []
            DMin = []
            dMax = []
            dMin = []
            delikAA = []
            delikAU = []
            milAA = []
            milAU = []
            sonuc = []

            for i in range(43):
                cap = random.randint(31, 80)
                milToleransBolgesi = random.choice(milToleransBolgeleri)
                delikKalitesi = random.choice(kaliteler)
                milKalitesi = delikKalitesi - 1
                sorular.append(
                    f"{cap} {delikToleransBolgesi} {delikKalitesi} / {milToleransBolgesi} {milKalitesi}")
                soru = tolerence_calculator(
                    cap, delikKalitesi, milKalitesi, milToleransBolgesi)
                soru.delik_td()
                soru.mil_td()
                soru.mil_deger()
                soruResult = soru.calculate_tolerance()
                gecmeTipi.append(soruResult[0])
                DMax.append(soruResult[1])
                DMin.append(soruResult[2])
                dMax.append(soruResult[3])
                dMin.append(soruResult[4])
                sonuc.append(soruResult[5])
                delikAA.append(soruResult[6]/1000)
                delikAU.append(soruResult[7]/1000)
                milAA.append(soruResult[8]/1000)
                milAU.append(soruResult[9]/1000)

            print(sorular)

            students["Ödev"] = sorular
            students["Geçme Tipi"] = gecmeTipi
            students["Delik Alt Tolerans Sınırı (mm)"] = delikAA
            students["Delik Üst Tolerans Sınırı (mm)"] = delikAU
            students["Mil Alt Tolerans Sınırı (mm)"] = milAA
            students["Mil Üst Tolerans Sınırı (mm)"] = milAU
            students["Maksimum Delik Çapı (mm)"] = DMax
            students["Minimum Delik Çapı (mm)"] = DMin
            students["Maksimum Mil Çapı (mm)"] = dMax
            students["Minimum Mil Çapı (mm)"] = dMin
            students["Sonuç"] = sonuc

            students.to_excel("tolerans_odev.xlsx", columns=[
                'Öğrenci No', ' Adı Soyadı', 'Ödev', "Geçme Tipi",
                "Delik Alt Tolerans Sınırı (mm)", "Delik Üst Tolerans Sınırı (mm)",
                "Mil Alt Tolerans Sınırı (mm)", "Mil Üst Tolerans Sınırı (mm)",
                "Maksimum Delik Çapı (mm)", "Minimum Delik Çapı (mm)",
                "Maksimum Mil Çapı (mm)", "Minimum Mil Çapı (mm)", "Sonuç"])
            messagebox.showinfo("showinfo", "Ödev Listesi Oluşturuldu.")
