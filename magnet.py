num = int(input())
magnets = []
for i in range(num):
    mag = input()
    magnets.append(mag)
counted = 1
for j in range(1,len(magnets)):
    if magnets[j] != magnets[j-1]:
        counted += 1
print(counted)
