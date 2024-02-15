sayi = int(input("Lütfen bir sayi giriniz: "))
if sayi > 1:
    for i in range (2,sayi):
       if (sayi % i) == 0: #tam bolen
           print(sayi," Asal Sayi Değildir.")
           break
    else:
       print(sayi," Asal Sayidir.")
else:
   print(sayi," Asal Sayi Değildir.") 