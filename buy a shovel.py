n, m = map(int, input().split())
for shovels in range(1, 11):
    total_co = shovels * n
    if total_co % 10 == 0 or total_co % 10 == m:
        print(shovels)
        break
