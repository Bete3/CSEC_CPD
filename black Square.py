a1, a2, a3, a4 = map(int, input().split())
s = input()
 
calories = 0
for digit in s:
    if digit == '1':
        calories += a1
    elif digit == '2':
        calories += a2
    elif digit == '3':
        calories += a3
    else:
        calories += a4
 
print(calories)
