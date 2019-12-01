import time

CURR_MS = lambda: time.time() * 1000

with open("input.txt") as file:
    inputs = file.read().strip().split()

def partOne():
    return 0

def partTwo():
    return 0

print("[ADVENT OF CODE - DAY02]\n")
start = CURR_MS()

print("PART ONE - " + str(partOne()))
print("PART ONE TIME - %.6fms\n" % (CURR_MS() - start))

twoStart = CURR_MS()
print("PART TWO - " + str(partTwo()))
print("PART TWO TIME - %.6fms" % (CURR_MS() - twoStart))

