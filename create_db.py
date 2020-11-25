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

# Genel TD
'''
for i in range(11, 19):
    item = Deliktd(cap=i, TD5=8, TD6=11, TD7=18, TD8=27, TD9=43)
    item.save()

for i in range(19, 31):
    item = Deliktd(cap=i, TD5=9, TD6=13, TD7=21, TD8=33, TD9=52)
    item.save()
'''

for i in range(31, 51):
    item = Deliktd(cap=i, TD5=11, TD6=16, TD7=25, TD8=39, TD9=62)
    item.save()

for i in range(51, 81):
    item = Deliktd(cap=i, TD5=13, TD6=19, TD7=30, TD8=46, TD9=74)
    item.save()

# Mil Aa
for i in range(31, 41):
    item = Milaa(cap=i, r=34, s=43, t=48, u=60, v=68)
    item.save()

for i in range(41, 51):
    item = Milaa(cap=i, r=34, s=43, t=54, u=70, v=81)
    item.save()

for i in range(51, 66):
    item = Milaa(cap=i, r=41, s=53, t=66, u=87, v=102)
    item.save()

for i in range(66, 81):
    item = Milaa(cap=i, r=43, s=59, t=75, u=102, v=120)
    item.save()

# Mil Au
for i in range(31, 41):
    item = Milau(cap=i, c=-120, d=-80, e=-50, f=-25, g=-9)
    item.save()

for i in range(41, 51):
    item = Milau(cap=i, c=-130, d=-80, e=-50, f=-25, g=-9)
    item.save()

for i in range(51, 66):
    item = Milau(cap=i, c=-140, d=-100, e=-60, f=-30, g=-10)
    item.save()

for i in range(66, 81):
    item = Milau(cap=i, c=-150, d=-100, e=-60, f=-30, g=-10)
    item.save()


db.close()
