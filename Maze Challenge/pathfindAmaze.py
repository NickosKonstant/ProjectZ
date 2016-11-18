#######################      Maze pathfinding        ###########################
#######################      Version: beta 1.0       ###########################

### In this version the user can choose from a maze gallery given as a
### collection of .txt files.
### All mazes have at least one solution.
### The main procedure finds the shortest path from a unique start point to a
### unique end point.
### In case of multiple solutions ( two or more minimun length paths) the
### algorithm will choose an arbitry one.

### The option to let the user load his own maze in txt-file can be considered
### in future updates

###############################################################################
######################              Input           ###########################
###############################################################################

# Maze gallery
mazes = ['maze1.txt','maze2.txt','maze3.txt','maze4.txt','maze5.txt']

# Choose from gallery
i = 0

while i not in range(1,len(mazes) + 1):
    print("Available mazes: ")
    print([i for i in range(1,len(mazes) + 1)])
    i = int(input("Choose maze: "))

maze_chosen = mazes[i - 1]

# Open maze file
with open(maze_chosen) as f:
    grid_data = [i for i in f.readlines()]

grid = [i[:-1] for i in grid_data]              # remove /n

# Print the Maze
for line in grid:
    print(line)

###############################################################################
########################    Procedures    #####################################
###############################################################################
def get_start_point(maze):
    '''
    (list of lists) -> list
    maze -> a list of strings composing the maze

    Returns the coordinates of the starting point(denoted as 'S' in the maze).
    '''
    end_points = [el.find("S") for el in maze]
    x = [x for x in end_points if x != -1][0]
    y = end_points.index(x)
    return [x,y]

def get_end_point(maze):
    '''
    (list of lists) -> list
    maze -> a list of strings composing the maze

    Returns the coordinates of the end point(denoted as '0' in the maze) and
    initializes a counter=0 as a third coordinate.
    '''
    end_points = [el.find("0") for el in maze]
    x = [x for x in end_points if x != -1][0]
    y = end_points.index(x)
    return [x,y,0]

def find_adjacent(point):
    '''
    list -> list
    point -> a list of current point (x,y) coordinates

    Returns a list of lists with the coordinates of the adjacect points to the
    current point.
    '''
    adj = []
    adj.extend([[point[0]+1,point[1]],[point[0]-1,point[1]],[point[0],point[1]+1],[point[0],point[1]-1]])
    return adj

def add_counter(coordinates,counter):
    '''
    (list, int) -> None
    coordinates -> a list of lists with the coordinates of grind points
    counter -> # of steps so far

    Adds a counter as a third coordinate to every element on points
    '''
    for p in coordinates:
        p.append(counter)


def remove_wall_points(adj_points, maze):
    '''
    (list, list) -> None
    adj_points -> a list of lists with the coordinates of points
    maze -> a list of strings composing the maze

    Removes the points in adj_points that colide with walls (denoted by 'x')
    in maze
    '''
    adj = adj_points[:]
    for point in adj:
        #print(point)
        if maze[point[1]][point[0]] == 'x':
            #print('remove', point)
            adj_points.remove(point)


def remove_backsteps(new_points, path):
    '''
    (list, list) -> list
    new_points -> a list of lists with the coordinates of new points
    path -> a list of lists with the coordinates of current points

    Removes dublicates found in path from new_points.
    '''
    adj_points = new_points[:]
    coordinates = [[coordinate[0],coordinate[1]] for coordinate in path]
    for point in new_points:
        if point in coordinates:
            new_points.remove(point)

def update_path(path, new_points):
    '''
    (list,list) -> list
    path -> a list of points (x,y)
    new_points -> a list of lists with the coordinates of points

    Returns path after updating with new_points.
    '''
    return path.extend(new_points)

###############################################################################
##############################    Main     ####################################
###############################################################################

steps = [get_end_point(grid)]                   # steps so far (all posible routes)

start_point = get_start_point(grid)
end_point = get_end_point(grid)[:-1]            # drop the counter

### Moving to every reachable adjacent point starting from finish-point (GOAL)
### until one of the paths reaches starting point (S)

new_points = [end_point]                        #
counter = 1
while start_point not in [[coordinate[0],coordinate[1]] for coordinate in steps]:
    # find adjacent points
    adjacent_points = []
    for point in new_points:
        adj=find_adjacent(point)
        adjacent_points.extend(adj)

    # remove points on walls and points where been before
    remove_wall_points(adjacent_points,grid)
    remove_backsteps(adjacent_points, steps)
    # update new points
    new_points = adjacent_points
    # add counters to new points and update steps list
    add_counter(new_points,counter)
    counter += 1
    update_path(steps,new_points)

### Reversing the shortest path
### Starting from start_point (denoted by "S" in maze) and going backwards till
### the end_point (denoted by '0' in maze)

amount_of_steps = steps[-1][-1]                 # the biggest counter
path = [start_point]                            # Initiate path with stating point

while amount_of_steps - 1 >= 0:
    # Find subset of one step behind points
    previous_steps = [item[:2] for item in steps if item[2] == amount_of_steps - 1]
    for step in previous_steps:
        # check which one is reachable and add it to path
        # for ties choose the first one comes out (the length of the path won't
        # change)
        if step in find_adjacent(path[-1]):
            path.append(step)
            break
    amount_of_steps -= 1
################################################################################
############################      Output      ##################################
################################################################################
### Print out the solution
### Draw the shortest path from start_point to end_point

print("\nThe shortest path from", start_point, "to", end_point, "is:")
print(path[0], end='')
for point in path[1:]:
    print(' ->',point, end='')
