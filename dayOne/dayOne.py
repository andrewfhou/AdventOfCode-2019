import time

CURR_MS = lambda: time.time() * 1000

with open("input.txt") as file:
    inputs = file.read().strip().split()

def partOne():
    sum = 0
    for x in inputs:
        sum += int(int(x) / 3) - 2
    return sum

def partTwo():
    sum = 0
    for x in inputs:
        sum += computeFuel(int(x))
    return sum

def computeFuel(fuel):
    if fuel <= 0:
        return 0
    else:
        needed = (int(int(fuel) / 3) - 2)
        needed = 0 if needed < 0 else needed
        return needed + computeFuel(needed)

print("[ADVENT OF CODE - DAY01]\n")
start = CURR_MS()

print("PART ONE - " + str(partOne()))
print("PART ONE TIME - %.6fms\n" % (CURR_MS() - start))

twoStart = CURR_MS()
print("PART TWO - " + str(partTwo()))
print("PART TWO TIME - %.6fms" % (CURR_MS() - twoStart))

