import math
import mod;

def calculate_z(alpha):
    cos_alpha = math.cos(alpha)
    z = cos_alpha ** 2 + cos_alpha ** 4
    return z

alpha = float(input("Введіть значення α: "))
z = calculate_z(alpha)
print(f"Значення z: {z:.4f}")

print("Гра 'Вгадай число': комп'ютер загадав число від 1 до 100. Спробуйте вгадати!")
mod.guess_number()
