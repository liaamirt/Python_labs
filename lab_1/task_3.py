n = int(input("Введіть значення n: "))

while n < 1 or n > 9:
  print("n має відповідати вимогам: 1 < n < 9")
  n = int(input("Введіть значееня n: "))

for i in range (n, 0, -1):
  for j in range (i, 0, -1):
    print('*', end = "")
  print("")
