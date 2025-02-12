s = input()
cur = 'a'
mov = 0
for char in s:
    diff = abs(ord(char) - ord(cur))
    mov += min(diff, 26 - diff)
    cur = char
print(mov)
