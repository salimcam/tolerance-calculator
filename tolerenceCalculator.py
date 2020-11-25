from peewee import *

db = SqliteDatabase("tolerans.db")


class Deliktd(Model):
    cap = IntegerField()
    TD5 = IntegerField()
    TD6 = IntegerField()
    TD7 = IntegerField()
    TD8 = IntegerField()
    TD9 = IntegerField()

    class Meta:
        database = db


class Milaa(Model):
    cap = IntegerField()
    r = IntegerField()
    s = IntegerField()
    t = IntegerField()
    u = IntegerField()
    v = IntegerField()

    class Meta:
        database = db


class Milau(Model):
    cap = IntegerField()
    c = IntegerField()
    d = IntegerField()
    e = IntegerField()
    f = IntegerField()
    g = IntegerField()

    class Meta:
        database = db


db.connect()

db.create_tables([Deliktd, Milaa, Milau])


class tolerence_calculator:
    def __init__(self, cap, delik_kalitesi, mil_kalitesi, mil_harf, mil_kalite=0, delik_kalite=0, mil_Aa_Au=0):
        self.cap = cap
        self.delik_kalitesi = delik_kalitesi
        self.mil_kalitesi = mil_kalitesi
        self.mil_harf = mil_harf
        self.mil_kalite = mil_kalite
        self.delik_kalite = delik_kalite
        self.mil_Aa_Au = mil_Aa_Au

    def delik_td(self):
        item = Deliktd.select().where(Deliktd.cap == self.cap).get()
        #delik_kalite = None
        if self.delik_kalitesi == 5:
            self.delik_kalite = item.TD5
        elif self.delik_kalitesi == 6:
            self.delik_kalite = item.TD6
        elif self.delik_kalitesi == 7:
            self.delik_kalite = item.TD7
        elif self.delik_kalitesi == 8:
            self.delik_kalite = item.TD8
        elif self.delik_kalitesi == 9:
            self.delik_kalite = item.TD9
        return self.delik_kalite

    def mil_td(self):
        item = Deliktd.select().where(Deliktd.cap == self.cap).get()
        #mil_kalite = None
        if self.mil_kalitesi == 5:
            self.mil_kalite = item.TD5
        elif self.mil_kalitesi == 6:
            self.mil_kalite = item.TD6
        elif self.mil_kalitesi == 7:
            self.mil_kalite = item.TD7
        elif self.mil_kalitesi == 8:
            self.mil_kalite = item.TD8
        elif self.mil_kalitesi == 9:
            self.mil_kalite = item.TD9
        return self.mil_kalite

    def mil_deger(self):
        #mil_Aa_Au = None
        if (self.mil_harf == "r" or self.mil_harf == "s" or self.mil_harf == "t" or self.mil_harf == "u" or self.mil_harf == "v"):
            item = Milaa.select().where(Milaa.cap == self.cap).get()
            if self.mil_harf == "r":
                self.mil_Aa_Au = item.r
            elif self.mil_harf == "s":
                self.mil_Aa_Au = item.s
            elif self.mil_harf == "t":
                self.mil_Aa_Au = item.t
            elif self.mil_harf == "u":
                self.mil_Aa_Au = item.u
            elif self.mil_harf == "v":
                self.mil_Aa_Au = item.v
            return self.mil_Aa_Au
        else:
            item = Milau.select().where(Milau.cap == self.cap).get()
            if self.mil_harf == "c":
                self.mil_Aa_Au = item.c
            elif self.mil_harf == "d":
                self.mil_Aa_Au = item.d
            elif self.mil_harf == "e":
                self.mil_Aa_Au = item.e
            elif self.mil_harf == "f":
                self.mil_Aa_Au = item.f
            elif self.mil_harf == "g":
                self.mil_Aa_Au = item.g
            return self.mil_Aa_Au

    def calculate_tolerance(self):
        delik_aa = 0
        delik_au = self.delik_kalite
        mil_aa = None
        mil_au = None
        tip = ""
        result = ""
        if (self.mil_Aa_Au > 0):
            mil_aa = self.mil_Aa_Au
            mil_au = self.mil_kalite + mil_aa
        else:
            mil_au = self.mil_Aa_Au
            mil_aa = mil_au - self.mil_kalite

        if (mil_aa > delik_au):
            tip = "Sıkı Geçme"
            print(tip)

        elif(mil_au > delik_aa and mil_aa < delik_au):
            tip = "Ara Geçme"
            print(tip)

        elif(mil_au < delik_aa):
            tip = "Boşluklu Geçme"
            print(tip)

        Dmax = self.cap + (delik_au)/1000
        Dmin = self.cap + (delik_aa)/1000
        print(f"Delik maksimum çapı: {Dmax}mm, Delik minimum çapı: {Dmin}mm")

        dmax = self.cap + (mil_au)/1000
        dmin = self.cap + (mil_aa)/1000
        print(f"Mil maksimum çapı: {dmax}mm, Mil minimum çapı: {dmin}mm")

        if (tip == "Sıkı Geçme"):
            Sb = (mil_au - delik_aa)/1000
            Sk = (mil_aa - delik_au)/1000
            result = f"Maksimum sıkılık: {Sb}mm, Minimum sıkılık: {Sk}mm"
            print(f"Maksimum sıkılık: {Sb}mm, Minimum sıkılık: {Sk}mm")

        elif (tip == "Boşluklu Geçme"):
            Bb = (delik_au - mil_aa)/1000
            Bk = (delik_aa - mil_au)/1000
            result = f"Maksimum boşluk: {Bb}mm, Minimum boşluk: {Bk}mm"
            print(f"Maksimum boşluk: {Bb}mm, Minimum boşluk: {Bk}mm")

        return([tip, Dmax, Dmin, dmax, dmin, result, delik_aa, delik_au, mil_aa, mil_au])


#soru1 = tolerence_calculator(40, 7, 6, "s")
# soru1.delik_td()
# soru1.mil_td()
# soru1.mil_deger()
# soru1.calculate_tolerance()


# print(soru1.delik_td())
# print(soru1.mil_td())
# print(soru1.mil_deger())
#tolerence_calculator(40, 5)
