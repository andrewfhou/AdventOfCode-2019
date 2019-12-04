import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 04 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    lower_bound, upper_bound = file.read().strip().split('-')
    pass_range = range(int(lower_bound), int(upper_bound) + 1)
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

def part_one():
    valid_count = 0
    for pw in pass_range:
        if increasing(pw) and has_consec(pw):
            valid_count = valid_count + 1
    return valid_count


def part_two():
    valid_count = 0
    for pw in pass_range:
        if increasing(pw) and pair_consec(pw):
            valid_count = valid_count + 1
    return valid_count

START_ONE = CURR_MS()
print('\nPART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

