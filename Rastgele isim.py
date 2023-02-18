import random
 
def rastgeleCevirici():
    isim = ["İpek", "Hilal" , "Sukran" ,"Buse" , "Beyza", "Hazel", "Belgin", "Meryem", "Elif", "Zehra"]
    soyisim = ["Beyaz", "Doruk", "Kır", "Yerli", "Kaya", "Yıldız", "Yurttaş"]
    return "{} {}".format(random.choice(isim), random.choice(soyisim))
 
for i in range(8):
    print(rastgeleCevirici())

