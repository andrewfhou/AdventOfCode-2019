import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 04 |')
print('+-------------------------+')

# START_READ = CURR_MS()
# print('\nREADING FILE... ',end='')
# with open("input.txt") as file:
#     inputs = file.read().strip().split()
# print('%.6fms\n' % (CURR_MS() - START_READ))

lowerBound = "165432"
upperBound = "707912"
# passRange = range(165432, 707912)
passRange = range(int(lowerBound), int(upperBound) + 1)

def increasing(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    for x in range(1, len(strpw)):
        if (int(strpw[x]) < prev):
            return False
        else:
            prev = int(strpw[x])
    return True

def hasConsec(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    for x in range(1, len(strpw)):
        if (int(strpw[x]) == prev):
            return True
        else:
            prev = int(strpw[x])
    return False

def pairedConsec(pw):
    strpw = str(pw)
    prev = int(strpw[0])
    
    for digit in range(0, 10):
        if strpw.count(str(digit)) == 2:
            return True
    return False

def partOne():
    validCount = 0
    for pw in passRange:
        if increasing(pw) and hasConsec(pw):
            validCount = validCount + 1
    return validCount


def partTwo():
    validCount = 0
    for pw in passRange:
        if increasing(pw) and pairedConsec(pw):
            validCount = validCount + 1
    return validCount

START_ONE = CURR_MS()

print('\nPART ONE: ' + str(partOne()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(partTwo()))
print('TIME TAKEN... %.6fms' % (CURR_MS() - START_TWO))

