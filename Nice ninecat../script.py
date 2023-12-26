code = []
with open ('ninecat.txt', 'r') as f:
    for line in f:
        code.append(chr(int(line)))

print("".join(code))
