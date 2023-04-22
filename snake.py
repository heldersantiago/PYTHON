import pygame
import random

# Initialize game window
pygame.init()
window_size = (500, 500)
window = pygame.display.set_mode(window_size)

# Color definitions
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Snake block size
block_size = 10

# Font for displaying score
font = pygame.font.SysFont(None, 25)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Function to display score
def display_score(score):
    value = font.render("Score: " + str(score), True, white)
    window.blit(value, [0,0])

# Initialize snake position and food position
def game_init():
    global snake_pos, food_pos
    snake_pos = [100,50]
    food_pos = [random.randrange(1, (window_size[0]//10)) * 10,
                random.randrange(1, (window_size[1]//10)) * 10]

# Function to check if food has been eaten
def food_eaten():
    global snake_pos, food_pos
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_pos = [random.randrange(1, (window_size[0]//10)) * 10,
                    random.randrange(1, (window_size[1]//10)) * 10]
        return True
    return False

# Function to check for game over
def game_over(snake_list):
    if snake_pos[0] >= window_size[0] or snake_pos[0] < 0:
        return True
    elif snake_pos[1] >= window_size[1] or snake_pos[1] < 0:
        return True
    for block in snake_list[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            return True
    return False

# Game loop
game_init()
snake_list = []
snake_length = 1
direction = 'right'
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 'up'
            elif event.key == pygame.K_DOWN:
                direction = 'down'
            elif event.key == pygame.K_LEFT:
                direction = 'left'
            elif event.key == pygame.K_RIGHT:
                direction = 'right'

    # Move snake in selected direction
    if direction == 'right':
        snake_pos[0] += block_size
