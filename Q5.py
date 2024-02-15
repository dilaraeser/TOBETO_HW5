sayi = int(input("Lütfen Bir sayi giriniz: "))
bölen = 2
for i in range (1,sayi):
    if(sayi % bölen == 0):
        print(bölen)
        sayi /= bölen
    else:
        bölen += 1