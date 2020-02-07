import os
# From https://stackoverflow.com/questions/36834505/creating-a-spiral-array-in-python
from math import ceil, sqrt
from itertools import cycle, count, chain    #https://docs.python.org/2/library/itertools.html#
from pprint import pprint
from tkinter import Tk
from tkinter.filedialog import askdirectory

# input folder
#file_list=os.listdir(r"C:\DATA\Efil\plate_02_8bits\A01\t01")
path = askdirectory(title='Select Folder') # shows dialog box and return the path
#print(path)
file_list=os.listdir(path)
#print (file_list)

#matrix = spiral(range(1, 82))
matrix = spiral(file_list)
#pprint(matrix)
ordered_file_list = list(chain.from_iterable(matrix))
#print(ordered_file_list)

start_nr = 0 
for filename in ordered_file_list:
    pathTofile = os.path.join(path, filename)
    number = '{0:02}'.format(start_nr)
    filenameWithoutExt, file_extension = os.path.splitext(pathTofile)
    #new_filename = "{}_{}{}".format(filenameWithoutExt, number,file_extension.lower())
    new_filename = "{}_{}{}".format("FOV", number,file_extension.lower())
    oldfile = os.path.join(path, filename)
    newfile = os.path.join(path, new_filename)
    os.rename(oldfile, newfile)
    print("Done :{}".format(filename))
    start_nr += 1

def spiral_distances():
    """
    Yields 1, 1, 2, 2, 3, 3, ...
    """
    for distance in count(1):
        for _ in (0, 1):
            yield distance

def clockwise_directions():
    """
    Yields right, down, left, up, right, down, left, up, right, ...
    """
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    return cycle((right, down, left, up))

def anticlockwise_directions():
    """
    Yields left, down, right, up, left, down, right, up, ...
    """
    left = (-1, 0)
    right = (1, 0)
    up = (0, -1)
    down = (0, 1)
    return cycle((left, down, right, up))

def spiral_movements():
    """
    Yields each individual movement to make a clockwise spiral:
    right, down, left, left, up, up, right, right, right, down, down, down, ...
    or an anticlockwise spiral:
    left, down, right, right, up, up, left, left, left, down, down, down, ...
    """
    #for distance, direction in zip(spiral_distances(), clockwise_directions()): #Python 3 izip -> zip
    for distance, direction in zip(spiral_distances(), anticlockwise_directions()): #Python 3 izip -> zip
        for _ in range(distance):
            yield direction

def square(width):
    """
    Returns a width x width 2D list filled with Nones
    """
    return [[None] * width for _ in range(width)]

def spiral(inp):
    width = int(ceil(sqrt(len(inp))))
    result = square(width)
    x = width // 2
    y = width // 2
    for value, movement in zip(inp, spiral_movements()): #Python 3 izip -> zip
        result[y][x] = value
        dx, dy = movement
        x += dx
        y += dy
    return result