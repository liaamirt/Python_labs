def fibonacci_sequence(n):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    fib_sequence = [0, 1]
    
    for i in range(2, n):
        next_element = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_element)
    
    return fib_sequence

n = int(input("Введіть довжину масиву: "))
fib_sequence = fibonacci_sequence(n)
print(f"Послідовність Фібоначчі довжини {n}: {fib_sequence}")
