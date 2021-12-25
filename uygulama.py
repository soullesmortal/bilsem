#kullanıcıdan 10 sayı isteyerek bunları bir listeye atıp küçükten büyüğe doğru sıralayınız
liste=[]
for i in range (10):
    e=int(input("bir sayı giriniz"))
    print(e)
    liste.append(e)
sıralama=input("a-z,z-a")
if sıralama=="a-z":
    liste.sort(reverse=False)
    print(liste)
elif sıralama=="z-a":
    liste.sort(reverse=True)
    print(liste)
else:
    print("hatalı giriş")

