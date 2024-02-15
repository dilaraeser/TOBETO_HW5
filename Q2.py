sayi = int(input("Lütfen bir sayi giriniz: "))

toplam = 0

for x in range(1, sayi + 1):
    if sayi % x == 0: #pozitif bolenleri bulma
        toplam += x

if(sayi == toplam / 2):
    print("Mukemmel sayidir.")
else:
    print("Mukemmel sayi degildir.")