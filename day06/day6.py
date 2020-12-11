import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 06 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nREADING FILE... ',end='')
with open("input.txt") as file:
    inputs = file.read().strip().split()
print('%.6fms' % (CURR_MS() - START_READ))

def part_one():
    orbits = {}
    count = 0
    for x in inputs:
        centr, obj = x.split(')')
        orbits[obj] = centr
    for x in orbits.keys():
        if x == "COM": continue
        curr_planet = x
        while curr_planet != "COM":
            curr_planet = orbits[curr_planet]
            count = count + 1
    return count



def part_two():
    orbits = {}
    you_trav = {}
    path_len = 0
    for x in inputs:
        centr, obj = x.split(')')
        orbits[obj] = centr

    curr_planet = orbits["YOU"]
    you_count = 0
    while curr_planet != "COM":
        you_trav[curr_planet] = you_count
        curr_planet = orbits[curr_planet]
        you_count = you_count + 1

    curr_planet = orbits["SAN"]
    san_count = 0
    not_found = True
    while not_found:
        if curr_planet in you_trav.keys():
            not_found = False
            path_len = san_count + you_trav[curr_planet]
        else:
            san_count = san_count + 1
            curr_planet = orbits[curr_planet]
    return path_len

START_ONE = CURR_MS()
print('\nPART ONE: ' + str(part_one()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()
print('PART TWO: ' + str(part_two()))
print('TIME TAKEN... %.6fms\n' % (CURR_MS() - START_TWO))

