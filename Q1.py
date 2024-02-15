eleman = int(input("Lütfen 20 veya 20'den buyuk bir eleman sayisi giriniz: "))

fibonacci = [1, 1]  # İlk iki elemanı 1 olan Fibonacci serisi

while len(fibonacci) < eleman:  # En az 20 elemanlı olana kadar devam et
    next_fib = fibonacci[-1] + fibonacci[-2]  # Son iki elemanın toplamı
    fibonacci.append(next_fib)  # Yeni Fibonacci sayısını listeye ekle

print(fibonacci)