#!/usr/bin/env python3
import itertools
from pprint import pprint

images = [
    'boat',
    'person',
    'moose',
    'face',
]

# clockwise from top
pieces = [
    [
        ('face', 'left'),
        ('person', 'top'),
        ('boat', 'back'),
        ('boat', 'back'),
    ],
    [
        ('person', 'bottom'),
        ('boat', 'front'),
        ('face', 'right'),
        ('moose', 'back'),
    ],
    [
        ('face', 'left'),
        ('face', 'left'),
        ('moose', 'back'),
        ('boat', 'back'),
    ],
    [
        ('moose', 'front'),
        ('moose', 'back'),
        ('person', 'top'),
        ('person', 'bottom'),
    ],
    [
        ('moose', 'front'),
        ('boat', 'front'),
        ('person', 'top'),
        ('face', 'right'),
    ],
    [
        ('face', 'left'),
        ('face', 'left'),
        ('person', 'top'),
        ('boat', 'back'),
    ],
    [
        ('boat', 'front'),
        ('moose', 'front'),
        ('face', 'right'),
        ('moose', 'back'),
    ],
    [
        ('boat', 'front'),
        ('moose', 'front'),
        ('moose', 'back'),
        ('person', 'bottom'),
    ],
    [
        ('person', 'bottom'),
        ('boat', 'front'),
        ('person', 'top'),
        ('face', 'right'),
    ],
]

def left_right(left, right):
    lthing, lorientation = left[1]
    rthing, rorientation = right[3]
    return (lthing == rthing) & (lorientation != rorientation)

def up_down(top, bottom):
    tthing, torientation = top[2]
    bthing, borientation = bottom[0]
    return (tthing == bthing) & (torientation != borientation)

def check_row(row):
    left, middle, right = row
    return left_right(left, middle) & left_right(middle, right)

def check_column(column):
    top, middle, bottom = column
    return up_down(top, middle) & up_down(middle, bottom)

def rotations(cells):
    for iii in itertools.combinations_with_replacement(range(4), 9):
        yield [rotate(cell, i) for cell, i in zip(cells, iii)]

def rotate(cell, i):
    return [(cell*2)[i:(i+4)] for i in range(4)]

def check_grid(grid:list):
    rows = [grid[0:3], grid[3:6], grid[6:9]]
    columns = [grid[0::3], grid[1::3], grid[2::3]]
    return True
    for row in rows:
        if not check_row(row):
            return False
    for column in columns:
        if not check_column(column):
            return False
    return True

def main():
    for i, grid in enumerate(itertools.permutations(pieces, len(pieces))):
        for grid_rotation in rotations(grid):
            if check_grid(grid_rotation):
                pprint(grid_rotation, width = 40)
                return
    print('No solution found')

if __name__ == '__main__':
    main()
