from collections import defaultdict

with open("intcode_test.txt") as file:
    inputs = file.read().strip().split(',')

def run_intcode(prog_inputs):
    # OPCODES                                            1  2  3  4  5  6  7  8  9
    arg_sizes = defaultdict(lambda:0, dict(enumerate([0, 3, 3, 1, 1, 2, 2, 3, 3, 1])))

    code = list(map(int, inputs))
    prog_inputs = list(prog_inputs)
    outputs = []
    instr_pt = 0
    rel_base = 0

    def get_arg(arg_idx, instr_pt, write):
        arg_param = int(instr[-(2+arg_idx)])

        if write:
            wrt_idx = code[instr_pt + arg_idx]
            if wrt_idx + rel_base >= len(code): # expand allocated mem if needed
                code.extend([0] * int((wrt_idx - len(code) + rel_base) * 1.5))
            if arg_param == 2:
                wrt_idx = wrt_idx + rel_base
            return wrt_idx
        elif arg_param == 0:
            pos = code[instr_pt+arg_idx]
            try: return code[pos]
            except IndexError: return 0 # out of existing mem, return default
        elif arg_param == 1:
            immediate = instr_pt + arg_idx
            try: return code[immediate]
            except IndexError: return 0 # out of existing mem, return default
        elif arg_param == 2:
            rel_pos = rel_base + code[instr_pt+arg_idx]
            try: return code[rel_pos]
            except IndexError: return 0 # out of existing mem, return default

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
        elif opcode == 9: # ADJUST RELATIVE BASE OFFSET
            arg1 = get_arg(1, instr_pt, False)
            rel_base = rel_base + arg1
        if not jump: instr_pt = instr_pt + (argsize + 1)

print(run_intcode(inputs, [5]))