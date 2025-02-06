matrix = [list(map(int, input().split())) for _ in range(5)]
for i in range(5):
  for j in range(5):
     if matrix[i][j] == 1:
        current_row, current_col = i + 1, j + 1  
moves = abs (current_row - 3) + abs (current_col - 3)
print(moves)
