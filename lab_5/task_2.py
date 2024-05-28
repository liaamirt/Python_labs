n = 7

matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if j + i + 1 < n:
      matrix[i][j] = 0
    else:
     matrix[i][j] = j + 1 - (n - i - 1)

for i in range(n):
  for j in range(n):
    print(matrix[i][j], end=" ")
  print()
