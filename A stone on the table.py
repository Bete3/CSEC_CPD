num = int(input())
stone = input()
count = 0
l = 0
r = l+1
while r < num:
    if stone[l] == stone[r]:
        count += 1
    l = r
    r += 1
print(count)
