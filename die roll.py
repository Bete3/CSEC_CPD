def solve():
  y, w = map(int, input().split())
  wins = 6 - max(y, w) + 1
  
  if wins <= 0:
    print("0/1")
  else:
    def gcd(a, b):
      while b:
        a, b = b, a % b
      return a

    common_divisor = gcd(wins, 6)
    print(f"{wins // common_divisor}/{6 // common_divisor}")

solve()
