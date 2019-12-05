import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 05 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split(',')
print('%.6fms' % (CURR_MS() - START_READ))

def run_intcode(code):
    code = list(map(int, code))

    instr_pt = 0
    while True:
        instr = str(code[instr_pt])
        opcode = int(instr[-2:]) # last 2 digits define the opcode

        if opcode == 99: # HALT
            return
        elif opcode == 1: # ADD
            argsize = 3
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]
            arg3 = code[instr_pt+3] # write target
            code[arg3] = arg1 + arg2

            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 2: # MULTIPLY
            argsize = 3
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]
            arg3 = code[instr_pt+3] # write target
            code[arg3] = arg1 * arg2
            
            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 3: # INPUT
            argsize = 1

            arg1 = code[instr_pt+1] # write target
            print('INPUT: ', end='') 
            console_in = int(input()) # input from console
            code[arg1] = console_in

            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 4: # OUTPUT
            argsize = 1
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            print(str(arg1) + ' ', end='') # output to console

            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 5: # JUMP IF TRUE
            argsize = 2
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]

            instr_pt = arg2 if arg1 != 0 else instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 6: # JUMP IF FALSE
            argsize = 2
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]

            instr_pt = arg2 if arg1 == 0 else instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 7: # LESS THAN
            argsize = 3
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]
            arg3 = code[instr_pt+3] # write target
            code[arg3] = 1 if arg1 < arg2 else 0

            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer
        elif opcode == 8: # EQUALS
            argsize = 3
            instr = instr.zfill(argsize + 2)

            arg1 = code[code[instr_pt+1]] if int(instr[-3]) == 0 else code[instr_pt+1]
            arg2 = code[code[instr_pt+2]] if int(instr[-4]) == 0 else code[instr_pt+2]
            arg3 = code[instr_pt+3] # write target
            code[arg3] = 1 if arg1 == arg2 else 0

            instr_pt = instr_pt + (argsize + 1) # increment instruction pointer

def part_one():
    run_intcode(inputs)

def part_two():
    run_intcode(inputs)

START_ONE = CURR_MS()
print('\nPART ONE: ')
part_one()
print('\nTIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ')
part_two()
print('\nTIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

