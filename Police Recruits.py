num = int(input())
nums = list(map(int,input().split()))
officers = 0
crimes = 0
 
for event in nums:
    if event == -1:
        if officers > 0:
            officers -= 1 
        else:
            crimes += 1  
    else:
        officers += event 
print(crimes)
