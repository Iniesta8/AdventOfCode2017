from collections import defaultdict

lines = open("input.txt").read().splitlines()
regs = defaultdict(int)

max_value = 0
for line in lines:
    reg, op, value, iff, creg, cop, cvalue = line.split()
    if eval("regs[creg]" + cop + cvalue):
        if op == "inc":
            regs[reg] += int(value)
            max_value = max(max_value, regs[reg])
        else:
            regs[reg] -= int(value)
            max_value = max(max_value, regs[reg])

print max(regs.values())  # Part a
print max_value  # Part b
