a = int(input("Введіть а: "))

while (a <= 0):
  a = int(input("Значення 'а' має бути більше 0. Введіть а: "))

b = int(input("Введіть b: "))
while (b <= 0):
  b = int(input("Значення 'b' має бути більше 0. Введіть b: "))

if a > b:
  result = a * b + 1
  print("a > b")

elif a == b:
  result = 25
  print("a = b")

elif (a < b):
  result = (a - 5) / b
  print("a < b")

print("result = ", format(result, '.2f'))
