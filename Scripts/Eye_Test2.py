#!/usr/bin/env python3
# Eye_Test2.py
import os
import pygame
import sys
import math

# Set position (optional, in case you need to target a specific screen)
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

# Initialize
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

pygame.mouse.set_pos((800, 480))
pygame.display.set_caption("Blinking Eyes")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Eye positions and dimensions (rotated 90°, so vertical rectangles)
eye_width = 80
eye_height_max = 200
left_eye_pos = [120, 100]  # x, y
right_eye_pos = [310, 100]

# Mouth position and dimensions
mouth_pos = [230, 450]  # x, y
mouth_width = 100
mouth_height_base = 20
mouth_amplitude = 5  # How much the mouth "wiggles"
mouth_freq = 2       # How fast the mouth wiggles (Hz)

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

    # Animate mouth height using sine wave
    mouth_time = now / 1000.0  # convert ms to seconds
    mouth_height = mouth_height_base + mouth_amplitude * math.sin(2 * math.pi * mouth_freq * mouth_time)

    # Draw the mouth as a horizontal rectangle with animated height
    pygame.draw.rect(screen, BLACK, (mouth_pos[0], mouth_pos[1], mouth_width, mouth_height))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
