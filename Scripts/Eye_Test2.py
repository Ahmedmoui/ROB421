import os
import pygame
import sys

# Set position (optional, in case you need to target a specific screen)
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

# Initialize
pygame.init()
screen = pygame.display.set_mode((480, 800), pygame.FULLSCREEN)
pygame.display.set_caption("Blinking Eyes - Portrait")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Eye positions and dimensions (rotated 90°, so vertical rectangles)
eye_width = 80
eye_height_max = 200
left_eye_pos = [120, 100]  # x, y
right_eye_pos = [310, 100]

# Blink animation settings
blink_interval = 3000      # Time between blinks (ms)
blink_duration = 600       # Total blink cycle time (ms)
blink_progress = 0         # Progress through blink cycle (0–1)
blinking = False
blink_start_time = 0

# Main loop
running = True
while running:
    now = pygame.time.get_ticks()
    
    screen.fill(WHITE)

    # Start blinking if time
    if not blinking and now - blink_start_time > blink_interval:
        blinking = True
        blink_start_time = now

    # Animate blink
    if blinking:
        elapsed = now - blink_start_time
        half = blink_duration // 2
        if elapsed < blink_duration:
            # First half: close, second half: open
            if elapsed < half:
                blink_progress = elapsed / half  # 0 → 1
            else:
                blink_progress = 1 - ((elapsed - half) / half)  # 1 → 0
        else:
            blinking = False
            blink_progress = 0

    # Compute eye height
    eye_height = eye_height_max * (1 - blink_progress)

    # Draw vertical eyes (portrait)
    pygame.draw.rect(screen, BLACK, (left_eye_pos[0], left_eye_pos[1], eye_width, eye_height))
    pygame.draw.rect(screen, BLACK, (right_eye_pos[0], right_eye_pos[1], eye_width, eye_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
