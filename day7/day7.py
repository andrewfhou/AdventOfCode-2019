import time
import itertools
from collections import defaultdict

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY XX |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split(',')
print('%.6fms\n' % (CURR_MS() - START_READ))

def run_intcode(code, prog_inputs):
    # OPCODES                                            1  2  3  4  5  6  7  8
    arg_sizes = defaultdict(lambda:0, dict(enumerate([0, 3, 3, 1, 1, 2, 2, 3, 3])))

    def get_arg(arg, instr_pt, write):
        return code[instr_pt+arg] if write \
            else (code[code[instr_pt+arg]] if int(instr[-(2+arg)]) == 0 else code[instr_pt+arg])

    code = list(map(int, code))
    prog_inputs = list(prog_inputs)
    outputs = []
    instr_pt = 0

    while True:
        jump =  False
        instr = str(code[instr_pt])
        opcode = int(instr[-2:])
        argsize = arg_sizes[opcode]
        instr = instr.zfill(argsize + 2)

        if opcode == 99: return outputs # HALT
        elif opcode == 1: # ADD
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            arg3 = get_arg(3, instr_pt, True)
            code[arg3] = arg1 + arg2
        elif opcode == 2: # MULTIPLY
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            arg3 = get_arg(3, instr_pt, True)
            code[arg3] = arg1 * arg2
        elif opcode == 3: # INPUT
            arg1 = get_arg(1, instr_pt, True)
            in_command = prog_inputs.pop(0)
            code[arg1] = in_command
        elif opcode == 4: # OUTPUT
            arg1 = get_arg(1, instr_pt, False)
            outputs.append(arg1)
        elif opcode == 5: # JUMP IF TRUE
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            if arg1 != 0:
                instr_pt = arg2
                jump = True
        elif opcode == 6: # JUMP IF FALSE
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            if arg1 == 0:
                instr_pt = arg2
                jump = True
        elif opcode == 7: # LESS THAN
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            arg3 = get_arg(3, instr_pt, True)
            code[arg3] = 1 if arg1 < arg2 else 0
        elif opcode == 8: # EQUALS
            arg1 = get_arg(1, instr_pt, False)
            arg2 = get_arg(2, instr_pt, False)
            arg3 = get_arg(3, instr_pt, True)
            code[arg3] = 1 if arg1 == arg2 else 0
        if not jump: instr_pt = instr_pt + (argsize + 1)

def part_one():
    max_thruster_sig = 0

    phases = list(itertools.permutations([0,1,2,3,4]))

    for phase in phases:
        thruster_sig = \
            run_intcode(inputs, [int(phase[4]), \
            run_intcode(inputs, [int(phase[3]), \
            run_intcode(inputs, [int(phase[2]), \
            run_intcode(inputs, [int(phase[1]), \
            run_intcode(inputs, [int(phase[0]), 0])[0]
                ])[0]   ])[0]   ])[0]   ])[0]
        # print(phase, thruster_sig)
        max_thruster_sig = max(thruster_sig, max_thruster_sig);
    return max_thruster_sig

def part_two():
    return 0

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))
