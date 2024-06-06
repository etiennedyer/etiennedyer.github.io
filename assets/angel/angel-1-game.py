import pygame
import math
import random

resolution = (911, 911)
screen = pygame.display.set_mode(resolution)
map_size = (35, 35)  # (rows, columns)
line_width = 1
clock = pygame.time.Clock()  # to set max FPS
pos = [0,0]
burnt_squares = []
highlighted_squares = []
auto_burnt_squares = []
angel_quadrant = 1
position = [18,18]
next_step = [18, 18]
wall1 = [(6,1), (5,1), (4,1), (3,1), (2,1), (1,1), (1,2), (1, 3), (1,4), (1,5), (1,6)]
keys_let = ['q', 'w', 'e', 'a', 's', 'd', 'z', 'c']
keys = []

for i in keys_let:
    keys.append(getattr(pygame, "K_" + i))
    print(i)
    print(keys)

def quandrant_fn():
    global angel_quadrant
    if position[0] == 18 and position[1] == 18:
        angel_quadrant = 0
    elif position[0] < 18 and position[1] < 18:
        angel_quadrant = 1
    elif position[0] > 18 and position[1] < 18:
        angel_quadrant = 2
    elif position[0] > 18 and position[1] > 18:
        angel_quadrant = 3
    elif position[0] < 18 and position[1] > 18:
        angel_quadrant = 4
    elif position[0] == 18 and position[1] > 18:
        angel_quadrant = 5
    elif position[0] < 18 and position[1] == 18:
        angel_quadrant = 6
    elif position[0] == 18 and position[1] < 18:
        angel_quadrant = 7
    elif position[0] > 18 and position[1] == 18:
        angel_quadrant = 8

def change_position():
    global position
    if tuple(next_step) not in burnt_squares:
            position[0] = next_step[0]
            position[1] = next_step[1]

def keyboard():
    if event.key == pygame.K_q:
        next_step[0] -= 1
        next_step[1] -= 1
    if event.key == pygame.K_w:
        next_step[1] -= 1
    if event.key == pygame.K_e:
        next_step[0]+= 1
        next_step[1] -= 1
    if event.key == pygame.K_a:
        next_step[0]-= 1
    if event.key == pygame.K_d:
        next_step[0]+= 1
    if event.key == pygame.K_z:
        next_step[0]-= 1
        next_step[1] += 1
    if event.key == pygame.K_s:
        next_step[1] += 1
    if event.key == pygame.K_c:
        next_step[0]+= 1
        next_step[1] += 1

    change_position()
    
    next_step[0] = position[0]
    next_step[1] = position[1]

def l_click_pos():
    pos = pygame.mouse.get_pos()
    row = math.floor((pos[0]+25)/26)
    column = math.floor((pos[1]+25)/26)
    spot = (row, column)
    if spot not in burnt_squares and spot != tuple(position):
        burnt_squares.append(spot)
    elif spot in burnt_squares:
        burnt_squares.remove(spot)

def r_click_pos():
    pos = pygame.mouse.get_pos()
    row = math.floor((pos[0]+25)/26)
    column = math.floor((pos[1]+25)/26)
    spot = (row, column)
    if spot not in highlighted_squares and spot != tuple(position):
        highlighted_squares.append(spot)
    elif spot in highlighted_squares:
        highlighted_squares.remove(spot)

def evaluate_dimensions():
    # Evaluate the width and the height of the squares.
    square_width = (resolution[0] / map_size[0]) - line_width * ((map_size[0] + 1) / map_size[0])
    square_height = (resolution[1] / map_size[1]) - line_width * ((map_size[1] + 1) / map_size[1])
    return (square_width, square_height)

def convert_column_to_x(column, square_width):
    x = line_width * (column + 1) + square_width * column
    return x

def convert_row_to_y(row, square_height):
    y = line_width * (row + 1) + square_height * row
    return y

#def devil_auto():
    list = []
    if angel_quadrant == 1:
        r = random.randint(0, 10)
        auto_burnt_squares.append(wall1[r])
        list.append(r)
        
def draw_squares():
    square_width, square_height = evaluate_dimensions()
    for row in range(map_size[0]):
        for column in range(map_size[1]):
            color = (255, 255, 255)  # (R, G, B)
            x = convert_column_to_x(column, square_width)
            y = convert_row_to_y(row, square_height)
            geometry = (x, y, square_width, square_height)
            pygame.draw.rect(screen, color, geometry)
     
def draw_angel():
    square_width, square_height = evaluate_dimensions()
    color = (167, 199, 231)  # (R, G, B)
    x = (25*(position[0]-1)+position[0])
    y = (25*(position[1]-1)+position[1])
    geometry = (x, y, square_width, square_height)
    pygame.draw.rect(screen, color, geometry)

def burn_squares():
    for i in range(len(burnt_squares)):
        row = (burnt_squares[i])[0]
        column = (burnt_squares[i])[1]
        x = (25*(row-1)+row)
        y = (25*(column-1)+column)
        square_width, square_height = evaluate_dimensions()
        color = (0, 0, 0)  # (R, G, B)
        geometry = (x, y, square_width, square_height)
        pygame.draw.rect(screen, color, geometry)

def highlight_squares():
    for i in range(len(highlighted_squares)):
        row = (highlighted_squares[i])[0]
        column = (highlighted_squares[i])[1]
        x = (25*(row-1)+row)
        y = (25*(column-1)+column)
        square_width, square_height = evaluate_dimensions()
        color = (200, 200, 200)  # (R, G, B)
        geometry = (x, y, square_width, square_height)
        pygame.draw.rect(screen, color, geometry)

def burn_squares_auto():
    for i in range(len(auto_burnt_squares)):
        square_width, square_height = evaluate_dimensions()
        color = (0, 0, 0)  # (R, G, B)
        row_d = (auto_burnt_squares[i])[0]
        column_d = (auto_burnt_squares[i])[1]
        x = (25*(row_d-1)+row_d)
        y = (25*(column_d-1)+column_d)
        geometry = (x, y, square_width, square_height)
        pygame.draw.rect(screen, color, geometry)

while True:
    clock.tick(60)  # max FPS = 60
    screen.fill((0, 0, 0))  # draw grid
    draw_squares()
    draw_angel()
    quandrant_fn()
    burn_squares()
    highlight_squares()
    burn_squares_auto()

    pygame.display.flip()  # Update the screen.
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            l_click_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            r_click_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN and event.key in keys:
            keyboard()