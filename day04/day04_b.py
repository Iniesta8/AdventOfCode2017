valids = 0;
valid_line = False

with open("input.txt", "r") as f:
    for line in f:
        valid_line = True
        words = line.split(' ')
        words[-1] = words[-1][:-1]  # eliminate newlines
        words = [''.join(sorted(s)) for s in words]  # sort chars of each word
        for word in words:
            if words.count(word) > 1:
                valid_line = False
                break;
        if valid_line:
            valids = valids + 1

print valids
