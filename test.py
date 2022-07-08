


d = [0.18, 0.18, 0.15, 0.06]


sums = []
new_div = 1.15 * (1 + d[0])
sums.append(new_div)
for i in d[1:]:
    growth = sums[-1] * (1 + i)
    sums.append(growth)

print(sums)
print(sums[-1])

ls = [1, 2, 3, 4]
ls.remove(2)
print(ls)
print(list(range(10, 1, -1)))