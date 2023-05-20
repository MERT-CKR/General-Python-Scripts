def fibonacci():
    # İlk iki Fibonacci sayısı
    a, b = 0, 1
    print(a)
    print(b)
    
    for i in range(2, 101):
        c = a + b
        print(c)
        a, b = b, c

fibonacci()
