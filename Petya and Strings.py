num1 = input().lower()
num2 = input().lower()
num1.lower()
num2.lower()
if len(num1) == len(num2):
  if num1 == num2:
    print(0)
  for i in range(len(num1)):
    if ord(num1[i]) < ord(num2[i]):
      print (-1)
      break
    elif ord(num1[i]) > ord(num2[i]):
      print (1)
      break
