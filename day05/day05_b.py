# Day 5: A Maze of Twisty Trampolines, All Alike

with open("input.txt", "r") as f:
    instructions = f.readlines()
    instructions = [int(s.strip()) for s in instructions]
    instructions.append(9999)  # termination criterion

    pc = 0
    steps_2_do = 0
    jumps_done = 0

    while (True):
        # print "Before value: " + str(instructions[pc])
        steps_2_do = instructions[pc]
        if steps_2_do == 9999:  # end
            break
        # print "Steps to do: " + str(steps_2_do)
        if steps_2_do >= 3:
            instructions[pc] = instructions[pc] - 1
        else:
            instructions[pc] = instructions[pc] + 1
        # print "After value: " + str(instructions[pc])
        pc = pc + steps_2_do
        jumps_done = jumps_done + 1
        # if jumps_done == 100:
        #     break

    print "Jumps done: " + str(jumps_done)
