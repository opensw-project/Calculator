r = 10
n = input()

for i in range(1, len(n)):
    if n[i] == n[i-1]:
        r += 5

    else:
        r += 10

print(r)
