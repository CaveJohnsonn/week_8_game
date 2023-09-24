import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1200, 400
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Don't Click the Red Button")

# Button dimensions and position
button_radius = 50
button_x, button_y = WIDTH // 2, HEIGHT // 2

# Reset button dimensions and position
reset_button_width, reset_button_height = 100, 40
reset_button_x, reset_button_y = (WIDTH - reset_button_width) // 2, HEIGHT - 60

# Game variables
clicked = False
message = ""
button_color = RED

# List of funny responses
funny_responses = [
    "Oops! You triggered the Doomsday Button! Now we wait for the zombie apocalypse.",
    "Congratulations! You just started World War Z! Grab your survival kit!",
    "You pressed the forbidden button! Prepare for the alien invasion!",
    "Don't worry, you just launched the Potato Cannon of Doom. Spuds are raining from the sky!",
    "You've unlocked the Pandemic Mode. Wash your hands and stay indoors!"
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - button_x) ** 2 + (mouse_y - button_y) ** 2) ** 0.5
            if distance <= button_radius:
                # User clicked the red button
                clicked = True
                message = random.choice(funny_responses)
                button_color = WHITE
            elif reset_button_x <= mouse_x <= reset_button_x + reset_button_width and \
                 reset_button_y <= mouse_y <= reset_button_y + reset_button_height:
                # User clicked the reset button
                clicked = False
                message = ""
                button_color = RED

    # Clear the screen
    window.fill(WHITE)

    # Draw the button (circle)
    pygame.draw.circle(window, button_color, (button_x, button_y), button_radius)

    # Draw a message if the button is clicked
    if clicked:
        text = FONT.render(message, True, RED)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        window.blit(text, text_rect)

    # Draw the reset button when the red button is clicked
    if clicked:
        pygame.draw.rect(window, RED, (reset_button_x, reset_button_y, reset_button_width, reset_button_height))
        reset_text = FONT.render("Reset", True, WHITE)
        reset_text_rect = reset_text.get_rect(center=(reset_button_x + reset_button_width // 2, reset_button_y + reset_button_height // 2))
        window.blit(reset_text, reset_text_rect)

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
