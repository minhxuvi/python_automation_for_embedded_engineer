"""Loop in python."""

# for loop
for i in range(10):
    print(i)

# while loop
i = 0
while i < 10:
    print(i)
    i += 1

# break and continue
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    if i == 5:
        continue
    print(i)

# nested loop
for i in range(10):
    for j in range(10):
        print(i, j)

# enumerate
for i, j in enumerate(range(10)):
    print(i, j)

# zip
for i, j in zip(range(10), range(10)):
    print(i, j)
