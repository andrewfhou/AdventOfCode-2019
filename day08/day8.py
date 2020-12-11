import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 08 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.readline()
print('%.6fms\n' % (CURR_MS() - START_READ))

def part_one(w,h):
    num_layers = int(len(inputs)/(w*h))
    layers = [inputs[x:x+w*h] for x in range(0, len(inputs), w*h)]
    min_zero = float('inf')

    for layer in layers:
        zeroes = layer.count('0')
        if zeroes < min_zero:
            min_zero = zeroes
            target = layer
    return target.count('1') * target.count('2')

def part_two(w,h):
    num_layers = int(len(inputs)/(w*h))
    layers = [inputs[x:x+w*h] for x in range(0, len(inputs), w*h)]

    for y in range(h):
        for x in range(w):
            for layer in range(num_layers):
                pxl = layers[layer][y*w + x]
                if pxl == '0':
                    print(' ',end='')
                    break
                elif pxl == '1':
                    print('█',end='')
                    break
        print('')

START_ONE = CURR_MS()
print('PART ONE: ' + str(part_one(25,6)))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: \n')
part_two(25,6)
print('\nTIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

