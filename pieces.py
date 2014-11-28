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
    return lthing == rthing & (lorientation != rorientation)

def up_down(top, bottom):
    tthing, torientation = top[2]
    bthing, borientation = bottom[0]
    return tthing == bthing & (torientation != borientation)

def check_row(row):
    left, middle, right = row
    return left_right(left, middle) & left_right(middle, right)

def check_column(column):
    top, middle, bottom = column
    return up_down(top, middle) & top_down(middle, bottom)

def check_grid(grid:list):
    rows = [grid[0:3], grid[3:6], grid[6:9]]
    columns = [grid[0::3], grid[1::3], grid[2::3]]
    for row in rows:
        if check_row(row):
            return True
    for column in columns:
        if check_column(column):
            return True
    return False

def main():
    for grid in itertools.permutations(pieces, len(pieces)):
        if check_grid(grid):
            pprint(grid, width = 40)
            break

if __name__ == '__main__':
    main()
