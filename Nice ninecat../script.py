code = []
with open ('ninecat.txt', 'r') as f:
    for line in f:
        code.append(chr(line))

print("".join(code))
