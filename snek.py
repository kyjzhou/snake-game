import pygame
import random

# initialize
pygame.init()

clock = pygame.time.Clock()

# Set display
game_screen_x = 800
game_screen_y = 600
game_screen = pygame.display.set_mode((game_screen_x, game_screen_y))

# Set display name
pygame.display.set_caption('Snek Game by Snakers')

# Set game over variable
game_over = False
collision = False

# Set colors that will be used
snek_color = (0, 0, 255)
food_color = (255, 0, 0)
score_color = (0, 255, 0)
game_screen_color = (0, 0, 0)
snek_head_color = (255,255,0)

# Snek Initial Position
snek_x = game_screen_x / 2
snek_y = game_screen_y / 2

# Snek Size
snek_w = 10
snek_h = 10

# Snek change in movement
snek_dx = 0
snek_dy = 0
snek_speed = 10

# Initialize snek body components
#snek_head = pygame.draw.rect(game_screen, snek_head_color, [snek_x, snek_y, snek_w, snek_h])
snek_body = []
snek_length = snek_w

# Set food variables
food_x = random.randrange(snek_w, game_screen_x - snek_w, snek_w)
food_y = random.randrange(snek_h, game_screen_y - snek_h, snek_h)
food_w = 10
food_h = 10
food = pygame.draw.rect(game_screen, food_color, [food_x, food_y, food_w, food_h])

# Set score
score = 0


def snake_not_in_bounds():
    return snek_x < 0 or snek_x > game_screen.get_width() or snek_y < 0 or snek_y > game_screen.get_height()


def restart_msg():
    font = pygame.font.SysFont(None, 30)
    msg = font.render("Game Over! Your score was: " + str(score) + " Press R to restart", True, food_color)
    msg_size = [game_screen.get_width() / 5, game_screen.get_height() / 3]
    game_screen.blit(msg, msg_size)


def display_score():
    font = pygame.font.SysFont(None, 30)
    msg = font.render("Score: " + str(score), True, food_color)
    game_screen.blit(msg, [0, 0])


# Game state
while not game_over:

    # Monitor game state
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        # On keydown event, move snek
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snek_dx = -snek_speed
                snek_dy = 0
            elif event.key == pygame.K_RIGHT:
                snek_dx = snek_speed
                snek_dy = 0
            elif event.key == pygame.K_UP:
                snek_dy = -snek_speed
                snek_dx = 0
            elif event.key == pygame.K_DOWN:
                snek_dy = snek_speed
                snek_dx = 0

    snek_x += snek_dx
    snek_y += snek_dy

    if abs(snek_y - food_y) < (snek_h + food_h) / 2 and abs(snek_x - food_x) < (snek_w + food_w) / 2:
        collision = True
        score += 1
        food_x = random.randrange(snek_w, game_screen_x - snek_w, snek_w)
        food_y = random.randrange(snek_h, game_screen_y - snek_h, snek_h)

        if snek_dx < 0:
            snek_length = snek_w * len(snek_body)
            new_part = pygame.draw.rect(game_screen, snek_color, [snek_x + snek_length, snek_y, snek_w, snek_h])
            snek_body.append(new_part)
        elif snek_dx > 0:
            snek_length = snek_w * len(snek_body)
            new_part = pygame.draw.rect(game_screen, snek_color, [snek_x - snek_length, snek_y, snek_w, snek_h])
            snek_body.append(new_part)
        elif snek_dy < 0:
            snek_length = snek_h * len(snek_body)
            new_part = pygame.draw.rect(game_screen, snek_color, [snek_x, snek_y + snek_length, snek_w, snek_h])
            snek_body.append(new_part)
        elif snek_dy > 0:
            snek_length = snek_h * len(snek_body)
            new_part = pygame.draw.rect(game_screen, snek_color, [snek_x, snek_y - snek_length, snek_w, snek_h])
            snek_body.append(new_part)

    game_screen.fill(game_screen_color)

    display_score()

    for i in range(len(snek_body)):
         snek_body[i][0] += snek_dx
         snek_body[i][1] += snek_dy

    for part in snek_body:
        pygame.draw.rect(game_screen, snek_color, [part.left + snek_dx , part.top + snek_dy, part.width, part.height])
        

    snek_head = pygame.draw.rect(game_screen, snek_head_color, [snek_x, snek_y, snek_w, snek_h])

    food = pygame.draw.rect(game_screen, food_color, [food_x, food_y, food_w, food_h])

    if snake_not_in_bounds():
        snek_speed = 0
        snek_dx = 0
        snek_dy = 0
        restart_msg()
        for event in pygame.event.get():
            if event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    snek_x = game_screen_x / 2
                    snek_y = game_screen_y / 2
                    snek_speed = 10
                    food_x = random.randrange(snek_w, game_screen_x - snek_w, snek_w)
                    food_y = random.randrange(snek_h, game_screen_y - snek_h, snek_h)
                    score = 0
                    snek_body = []

    pygame.display.update()
    clock.tick(snek_speed)

# Exit /  (2bi) if retry then set game_over == false
pygame.quit()
quit()
