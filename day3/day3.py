import time

CURR_MS = lambda: time.time() * 1000

with open("input.txt") as file:
    wire_a,wire_b = file.read().strip().split()

wire_a, wire_b = [x.split(',') for x in [wire_a, wire_b]]

mov_x = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
mov_y = {'U': 1, 'D': -1, 'L': 0, 'R': 0}

def trace_wire(wire):
    x = 0
    y = 0
    steps = 0
    pts = dict()

    for mov in wire:
        direction = mov[0]
        mag = int(mov[1:])
    
        for _ in range(mag):
            x = x + mov_x[direction]
            y = y + mov_y[direction]
            steps = steps + 1
            
            if (x,y) not in pts:
                pts[(x,y)] = steps
    return pts


points_a = trace_wire(wire_a)
points_b = trace_wire(wire_b)

def partOne():
    intersections = points_a.keys() & points_b.keys()
    minDist = float('inf')
    for (x,y) in intersections:
        minDist = min(minDist, abs(x) + abs(y))
    return minDist

def partTwo():
    intersections = points_a.keys() & points_b.keys()
    minSteps = float('inf')
    for x in intersections:
        minSteps = min(minSteps, points_a[x] + points_b[x])
    return minSteps

print("[ADVENT OF CODE - DAY03]\n")
start = CURR_MS()

print("PART ONE - " + str(partOne()))
print("PART ONE TIME - %.6fms\n" % (CURR_MS() - start))

twoStart = CURR_MS()
print("PART TWO - " + str(partTwo()))
print("PART TWO TIME - %.6fms" % (CURR_MS() - twoStart))

