user_name = input ()
arr = []
for i in user_name:
  if i not in arr:
    arr.append(i)
if len(arr) % 2 == 0:
  print ("CHAT WITH HER!")
else:
  print ("IGNORE HIM!")
