a = int(input("Birinci Sayıyı Giriniz : "))
b = int(input("İkinci Sayıyı Giriniz : "))
 
if (a > b):
    kucuksayi = b
else:
    kucuksayi = a
for i in range(1,kucuksayi+1):
    if (a  % i==0) and (b %i ==0):
        ebob = i
        ekok = (a*b)//ebob

print ("EBOB:", ebob)
print ("EKOK:", ekok)