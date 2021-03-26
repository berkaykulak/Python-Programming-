#list()

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90, notlar]

len(list_genis)

print(list_genis[0])
print(list_genis[1])
print(list_genis[3])



type(list_genis[3])

tum_liste = [liste, list_genis]


liste = [10,20,30,40,50]

print(liste[0])
print(liste[1])
print(liste[6])
print(liste[0:2])
print(liste[:2])
print(liste[2:])


yeni_liste = ["a",10,[20,30,40,50]]
print(yeni_liste)
print(yeni_liste[2])
print(yeni_liste[0:2])
print(yeni_liste[2][1])


liste = ["ali","veli","berkcan","ayse"]

print(liste)


liste[1] = "velinin_babasi"

print(liste)

liste[1] = "veli"

liste[0:3] = "alinin_babasi","velinin_babasi","berkcanin_babasi"

print(liste)

liste = ["ali","veli","berkcan","ayse"]
print(liste)

liste = liste + ["kemal"]
print(liste)

#del liste[2]
print(liste)

liste = ["ali","veli","isik"]

dir(liste)

print(liste)

#append & remove

liste.append("berkcan")

print(liste)

liste.remove("berkcan")
print(liste)

# insert

liste = ["ali","veli","isik"]

print(liste)

liste.insert(0,"ayse")

print(liste)

liste = ["ali","veli","isik"]

liste[0] = "ayse"

print(liste)

liste.insert(0,"ayse")
print(liste)

liste[1] = "ali"

print(liste)

liste.insert(2,"mehmet")
print(liste)

liste.insert(5,"berk")
print(liste)

len(liste)


liste.insert(len(liste),"beren")
print(liste)

#pop


liste.pop(0)
print(liste)

liste.pop(4)
print(liste)

#count

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")

#copy

liste_yedek = liste.copy()

#extend

liste.extend(["a","b",10])
print(liste)

#index()

liste.index("ali")

#reverse()

liste.reverse()
print(liste)

#sort()

liste = [10,40,5,90]
liste.sort()
print(liste)

#clear

liste.clear()
print(liste)



