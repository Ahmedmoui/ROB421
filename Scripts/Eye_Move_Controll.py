import os
import pygame
import math
import sys

# Set position (optional, in case you need to target a specific screen)
os.environ['SDL_VIDEO_WINDOW_POS'] = "1920,0"

# Initialize
pygame.init()
screen = pygame.display.set_mode((480, 800), pygame.NOFRAME)
pygame.display.set_caption("Blinking Eyes - Portrait")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Eye positions and dimensions (rotated 90°, so vertical rectangles)
eye_width = 80
eye_height = 200
left_eye_pos = [120, 100]  # x, y
right_eye_pos = [310, 100]

# Base Y position
eye_y = 100

# Eye oscillation parameters
amplitude = 40     # Max horizontal movement in pixels
speed = 0.002      # Movement speed (lower is slower)

# Main loop
running = True
start_time = pygame.time.get_ticks()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Time since start
    now = pygame.time.get_ticks()
    t = (now - start_time)

    # Oscillate x position using sine wave
    offset = amplitude * math.sin(speed * t)

    # Compute new eye positions
    left_eye_pos = [120 + offset, eye_y]
    right_eye_pos = [310 + offset, eye_y]

    # Draw
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (left_eye_pos[0], left_eye_pos[1], eye_width, eye_height))
    pygame.draw.rect(screen, BLACK, (right_eye_pos[0], right_eye_pos[1], eye_width, eye_height))
    pygame.display.flip()
    clock.tick(2)

pygame.quit()
sys.exit()
