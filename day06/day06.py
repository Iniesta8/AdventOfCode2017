banks = map(int, open("input.txt", "r").read().split())
seen = []
total = 0

while banks not in seen:
    seen.append(banks[:])  # copy by value!!
    index = banks.index(max(banks))
    value = banks[index]
    banks[index] = 0

    while value > 0:
        index = index + 1 if index < len(banks) -1 else 0
        banks[index] += 1
        value -= 1
    total += 1

print "Total cycles: " + str(total)
print "Cycles since last seen state: " + str(len(seen) - seen.index(banks))
