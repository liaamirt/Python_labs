def generate_fibonacci_up_to(n):
    fib_set = set()
    a, b = 0, 1
    while a <= n:
        fib_set.add(a)
        a, b = b, a + b
    return fib_set

given_set = set(range(1, 51))

fibonacci_set = generate_fibonacci_up_to(50)

intersection_set = given_set.intersection(fibonacci_set)

count_fibonacci_numbers = len(intersection_set)

print("Числа Фібоначчі в множині:", intersection_set)
print("Кількість чисел Фібоначчі в заданій множині:", count_fibonacci_numbers)
