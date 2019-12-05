from collections import defaultdict

with open("input.txt") as file:
    inputs = file.read().strip().split(',')

def run_intcode(code):
    # OPCODES                                            1  2  3  4  5  6  7  8
    arg_sizes = defaultdict(lambda:0, dict(enumerate([0, 3, 3, 1, 1, 2, 2, 3, 3])))

    def get_arg(arg, instr_pt, write):
        return code[instr_pt+arg] if write \
            else (code[code[instr_pt+arg]] if int(instr[-(2+arg)]) == 0 else code[instr_pt+arg])

    code = list(map(int, code))
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
            console_in = int(input('INPUT>'))
            code[arg1] = console_in
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

print(run_intcode(inputs))