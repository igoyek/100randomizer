import random

table = []
i = 0
while i < 100:
    x = random.randint(-100, 100)

    if table.count(x) == 0 and x % 2 == 0:
        table.append(x)
        i += 1

print("In table are", table.count(0), "zeros")
print(sum(table))
