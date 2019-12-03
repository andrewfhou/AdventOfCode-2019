import time

CURR_MS = lambda: time.time() * 1000

with open("input.txt") as file:
    input_data = file.read().strip().split(',')

def partOne():
    return runIntcode(input_data, 12, 2)

def runIntcode(inputs, noun, verb):
    inputs = list(map(int, inputs))
    inputs[1] = noun
    inputs[2] = verb

    i = 0
    while True:
        opcode = int(inputs[i])

        if opcode == 99:
            return inputs[0]
        elif opcode == 1:
            argsize = 4

            arg1_i = inputs[i+1]
            arg2_i = inputs[i+2]
            out_i = inputs[i+3]

            arg1 = inputs[arg1_i]
            arg2 = inputs[arg2_i]

            inputs[out_i] = arg1 + arg2
            i += argsize
        elif opcode == 2:
            argsize = 4

            arg1_i = inputs[i+1]
            arg2_i = inputs[i+2]
            out_i = inputs[i+3]

            arg1 = inputs[arg1_i]
            arg2 = inputs[arg2_i]

            inputs[out_i] = arg1 * arg2
            i += argsize



def partTwo():
    for noun in range(0, 100):
        for verb in range(0, 100):
            with open("input.txt") as file:
                inputtxt = file.read().strip().split(',')

            try:
                result = runIntcode(inputtxt, noun, verb)
            except Exception as e:
                pass

            if int(result) == 19690720:
                return "noun: " + str(noun) + " verb: " + str(verb) +\
                    "\nsolution: " + str(100 * noun + verb)


print("[ADVENT OF CODE - DAY02]\n")
start = CURR_MS()

print("PART ONE - " + str(partOne()))
print("PART ONE TIME - %.6fms\n" % (CURR_MS() - start))

twoStart = CURR_MS()
print("PART TWO - " + str(partTwo()))
print("PART TWO TIME - %.6fms" % (CURR_MS() - twoStart))

