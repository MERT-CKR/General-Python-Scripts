def fibonacci():
    # İlk iki Fibonacci sayısı
    a, b = 0, 1
    print(a)
    print(b)
    # Döngü, 100'e kadar Fibonacci sayılarını hesaplar ve yazdırır
    for i in range(2, 101):
        c = a + b
        print(c)
        # Diziyi bir sonraki adıma hazırlar
        a, b = b, c

fibonacci()
