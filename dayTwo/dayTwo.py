import time

CURR_MS = lambda: time.time() * 1000

with open("input.txt") as file:
    input_data = file.read().strip().split(',')

def partOne():
    input_data[1] = '12' # noun
    input_data[2] = '2' # verb
    runIntcode(input_data)
    return input_data[0]

def runIntcode(inputs):
    for i in range (0, len(inputs), 4):
        opcode = int(inputs[i])

        if opcode == 99:
            break

        input1_i = int(inputs[i+1])
        input2_i = int(inputs[i+2])
        out_i = int(inputs[i+3])

        input1 = int(inputs[input1_i])
        input2 = int(inputs[input2_i])

        if opcode == 1:
            inputs[out_i] = input1 + input2
        elif opcode == 2:
            inputs[out_i] = input1 * input2

def partTwo():
    for noun in range(0, 100):
        for verb in range(0, 100):
            with open("input.txt") as file:
                inputtxt = file.read().strip().split(',')

            inputtxt[1] = noun
            inputtxt[2] = verb

            try:
                runIntcode(inputtxt)
            except Exception as e:
                pass

            if int(inputtxt[0]) == 19690720:
                return "noun: " + str(noun) + " verb: " + str(verb) +\
                    "\nsolution: " + str(100 * noun + verb)


print("[ADVENT OF CODE - DAY02]\n")
start = CURR_MS()

print("PART ONE - " + str(partOne()))
print("PART ONE TIME - %.6fms\n" % (CURR_MS() - start))

twoStart = CURR_MS()
print("PART TWO - " + str(partTwo()))
print("PART TWO TIME - %.6fms" % (CURR_MS() - twoStart))

