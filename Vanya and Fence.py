person, hence = map(int,input().split())
a = list(map(int,input().split()))
result = 0 
for i in range(len(a)):
  if a[i] <= hence:
    result += 1
  else:
    result += 2
print(result)
