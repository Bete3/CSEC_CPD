num = int(input())
count = 0
for i in range(num):
  petya, vasya, tonya = map(int,input().split())
  if petya and  vasya and tonya == 1:
    count += 1
  elif petya and vasya == 1:
    count += 1
  elif petya and tonya == 1:
    count +=1
  elif tonya and vasya == 1:
    count += 1
print(count)
    
  
    
