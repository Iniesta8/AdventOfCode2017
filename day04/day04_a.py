valids = 0;
valid_line = False

with open("input.txt", "r") as f:
    for line in f:
        valid_line = True
        words = line.split(' ')
        words[-1] = words[-1][:-1]  # eliminate newlines
        for word in words:
            if words.count(word) > 1:
                # print words
                # print word
                valid_line = False
                break;
        if valid_line:
            valids = valids + 1

print valids
