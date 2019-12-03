import time

CURR_MS = lambda: time.time() * 1000

print('+-------------------------+')
print('| ADVENT OF CODE - DAY 03 |')
print('+-------------------------+')

START_READ = CURR_MS()
print('\nPROCESSING FILE... ', end='')
with open("input.txt") as file:
    wire_a,wire_b = file.read().strip().split()
wire_a, wire_b = [x.split(',') for x in [wire_a, wire_b]]
print('%.6fms\n' % (CURR_MS() - START_READ))

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

def partOne(points_a, points_b):
    intersections = points_a.keys() & points_b.keys()
    minDist = float('inf')
    for (x,y) in intersections:
        minDist = min(minDist, abs(x) + abs(y))
    return minDist

def partTwo(points_a, points_b):
    intersections = points_a.keys() & points_b.keys()
    minSteps = float('inf')
    for x in intersections:
        minSteps = min(minSteps, points_a[x] + points_b[x])
    return minSteps

START_ONE = CURR_MS()

pts_a = trace_wire(wire_a)
pts_b = trace_wire(wire_b)
print("PART ONE: " + str(partOne(pts_a, pts_b)))
print("TIME TAKEN... %.6fms\n" % (CURR_MS() - START_ONE))

START_TWO = CURR_MS()

pts_a = trace_wire(wire_a)
pts_b = trace_wire(wire_b)
print("PART TWO: " + str(partTwo(pts_a, pts_b)))
print("TIME TAKEN... %.6fms" % (CURR_MS() - START_TWO))

