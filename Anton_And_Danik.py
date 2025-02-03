num_games = input()
outcome = input() 

count_A = outcome.count("A")
count_B = outcome.count("D")

if count_A > count_B:
    print("Anton")
elif count_B > count_A:
    print("Danik")
else:
    print("Friendship")
