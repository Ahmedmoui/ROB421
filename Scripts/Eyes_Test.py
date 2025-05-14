import os
import pygame

# Set window position (e.g., place on second monitor)
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{1920},0"  # X,Y position in pixels

# Initialize Pygame
pygame.init()

# Set screen size (can be windowed or fullscreen on that region)
screen = pygame.display.set_mode((800, 480), pygame.NOFRAME)  # Example resolution

pygame.display.set_caption("Eyes on Second Monitor")

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, (0, 0, 0), (100, 100, 100, 150))  # Example eye
    pygame.display.flip()
    
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         running = False

pygame.quit()
