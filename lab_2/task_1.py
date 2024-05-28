import math
import random

def calculate_z(alpha):
    cos_alpha = math.cos(alpha)
    z = cos_alpha ** 2 + cos_alpha ** 4
    return z

def guess_number():
    number_to_guess = random.randint(1, 100)
    guessed = False

    while not guessed:
        user_guess = int(input("Введіть ваше число: "))
        if user_guess < number_to_guess:
            print("Моє число більше")
        elif user_guess > number_to_guess:
            print("Моє число менше")
        else:
            print("Ви вгадали!")
            guessed = True

alpha = float(input("Введіть значення α: "))
z = calculate_z(alpha)
print(f"Значення z: {z:.4f}")

print("Гра 'Вгадай число': комп'ютер загадав число від 1 до 100. Спробуйте вгадати!")
guess_number()
