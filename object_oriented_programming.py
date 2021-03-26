# Sinif Ozellikleri (Class attributes)

class VeriBilimci():
    bolum = ''
    sql = 'Evet'
    deneyim_yili = 0
    bildigi_diller = []


# Siniflarin ozelliklerine erismek
print(VeriBilimci.bolum)
print(VeriBilimci.sql)





# siniflarin ozelliklerini degistirmek
VeriBilimci.sql = "Hayir"
print(VeriBilimci.sql)

# Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()


print(ali.sql)

print(ali.deneyim_yili)

print(ali.bolum)
ali.bildigi_diller.append("Python")

print(ali.bildigi_diller)

veli = VeriBilimci()

print(veli.sql)


print(veli.bildigi_diller)


# Ornek ozellikleri

class VeriBilimci():
    bildigi_diller = ["R" ,"PYTHON"]
    bolum = ''
    sql = ''
    deneyim_yili = 0
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''

ali = VeriBilimci()
print(ali.bildigi_diller)


veli = VeriBilimci()
print(veli.bildigi_diller)


ali.bildigi_diller.append("Python")
print(ali.bildigi_diller)

print(veli.bildigi_diller)

veli.bildigi_diller.append("R")
print(veli.bildigi_diller)

print(VeriBilimci.bildigi_diller)

print(ali.bolum)



print(VeriBilimci.bolum)
ali.bolum = "istatistik"

print(VeriBilimci.bolum)

print(veli.bolum)
veli.bolum = "end_muh"

print(veli.bolum)

print(ali.bolum)

print(VeriBilimci.bolum)


# Ornek Metodlari

class VeriBilimci():
    calisanlar = []
    def __init__(self):
        self.bildigi_diller = []
        self.bolum = ''
    def dil_ekle(self, yeni_dil) :
        self.bildigi_diller.append(yeni_dil)


ali = VeriBilimci()
print(ali.bildigi_diller)
print(ali.bolum)


veli = VeriBilimci()
print(veli.bildigi_diller)
print(veli.bolum)


dir(VeriBilimci)
print(VeriBilimci.dil_ekle)

VeriBilimci.dil_ekle("R")

ali.dil_ekle("R")
print(ali.bildigi_diller)


veli.dil_ekle("Python")
print(veli.bildigi_diller)



# Miras Yapilari (inheritance)

class Employees():
    def __init__(self):
        self.FirstName = ""
        self.LastName = ""
        self.Address = ""

class DataScience(Employees):
    def __init__(self):
        self.Programming = ""

veribilimci1 = DataScience()


# veribilimci1.

class Marketing(Employees):
    def __init__(self):
        self.StoryTelling = ""

mar1 = Marketing()


# mar1.


class Employee_yeni():
    def __init__(self, FirstName ,LastName ,Address):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Address = Address


ali = Employee_yeni("a" ,"b" ,"c")
print(ali.FirstName)



A = 9

def impure_sum(b):
    return b + A

def pure_sum(a ,b):
    return a + b


impure_sum(6)
pure_sum(3 ,4)
