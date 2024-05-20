def caching_fibonacci():
    #Створити порожній словник cache
    cache = dict()
    def fibonacci(n):
        # n <= 0, 0
        # n == 1, 1
        # n у cache, cache[n]
        if n<=0: return 0
        if n==1: return 1
        if n in cache: return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

def main():
    # Отримуємо функцію Фібонначі
    fibb = caching_fibonacci()

    # Використовуємо функцію Фібонначі для обчислення чисел Фібоначчі
    print(fibb(10))  # Виведе 55
    print(fibb(15))  # Виведе 610

if __name__ == "__main__":
    main()
