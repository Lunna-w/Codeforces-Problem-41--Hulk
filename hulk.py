n = int(input())

# Strings
hate = "I hate"
love = "I love"
it = "it"
that = "that"

output = [hate]

for i in range(1, n):
    if i % 2 == 1:
        output.extend([that, love])
    else:
        output.extend([that, hate])

output.append(it)

print(" ".join(output))