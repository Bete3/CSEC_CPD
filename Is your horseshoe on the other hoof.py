s1, s2, s3, s4 = map(int, input().split())
distinct_colors = {s1, s2, s3, s4}
needed_to_buy = 4 - len(distinct_colors)
print(needed_to_buy)
