import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Platformer - Basic")

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Player attributes
player_width, player_height = 50, 50
player_x, player_y = 100, HEIGHT - 150
player_vel_x = 0
player_vel_y = 0
speed = 5
gravity = 0.5
jump_strength = -10
on_ground = False

# Platforms (x, y, width, height)
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 450, 100, 20),
    pygame.Rect(400, 350, 100, 20),
    pygame.Rect(600, 250, 100, 20),
]

def handle_movement(keys):
    global player_vel_x, player_vel_y, on_ground

    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -speed
    if keys[pygame.K_RIGHT]:
        player_vel_x = speed

    if keys[pygame.K_SPACE] and on_ground:
        player_vel_y = jump_strength
        on_ground = False

def apply_gravity():
    global player_vel_y
    player_vel_y += gravity

def move_and_collide(player_rect):
    global player_vel_y, on_ground
    player_rect.x += player_vel_x
    for plat in platforms:
        if player_rect.colliderect(plat):
            if player_vel_x > 0:
                player_rect.right = plat.left
            elif player_vel_x < 0:
                player_rect.left = plat.right

    player_rect.y += int(player_vel_y)
    on_ground = False
    for plat in platforms:
        if player_rect.colliderect(plat):
            if player_vel_y > 0:
                player_rect.bottom = plat.top
                player_vel_y = 0
                on_ground = True
            elif player_vel_y < 0:
                player_rect.top = plat.bottom
                player_vel_y = 0

    return player_rect

def draw(player_rect):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player_rect)
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)
    pygame.display.update()

def main():
    global player_x, player_y
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        handle_movement(keys)
        apply_gravity()
        player_rect = move_and_collide(player_rect)
        draw(player_rect)

if __name__ == "__main__":
    main()
