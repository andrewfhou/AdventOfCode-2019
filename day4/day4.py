import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 04 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    lowerBound, upperBound = file.read().strip().split('-')
    passRange = range(int(lowerBound), int(upperBound) + 1)
print('%.6fms' % (CURR_MS() - START_READ))

def increasing(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    for x in range(1, len(strpw)):
        if (int(strpw[x]) < prev):
            return False
        else:
            prev = int(strpw[x])
    return True

def has_consec(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    for x in range(1, len(strpw)):
        if (int(strpw[x]) == prev):
            return True
        else:
            prev = int(strpw[x])
    return False

def pair_consec(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    
    for digit in range(0, 10):
        if strpw.count(str(digit)) == 2:
            return True
    return False

def partOne():
    validCount = 0
    for pw in passRange:
        if increasing(pw) and has_consec(pw):
            validCount = validCount + 1
    return validCount


def partTwo():
    validCount = 0
    for pw in passRange:
        if increasing(pw) and pair_consec(pw):
            validCount = validCount + 1
    return validCount

START_ONE = CURR_MS()

print('\nPART ONE: ' + str(partOne()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(partTwo()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

