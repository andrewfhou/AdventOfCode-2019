import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY XX |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms\n' % (CURR_MS() - START_READ))

def partOne():
    return 0

def partTwo():
    return 0

START_ONE = CURR_MS()

print('PART ONE: ' + str(partOne()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(partTwo()))
print('TIME TAKEN... %.6fms' % (CURR_MS() - START_TWO))

