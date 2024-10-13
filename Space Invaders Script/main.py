import pygame
import random
import time

clock = pygame.time.Clock()

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1050, 850
ENEMY_COUNT = 10
ENEMY_SIZE = 60
PLAYER_SIZE = 80

# Colors
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

# Backgrounds
intro_background_img = pygame.image.load("png-cosmos.png")  # Replace with your intro background image
intro_background_img = pygame.transform.scale(intro_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
game_over_background_img = pygame.image.load("png-cosmos.png")  # Replace with your game-over background image
game_over_background_img = pygame.transform.scale(game_over_background_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Player
player_img = pygame.image.load("png-pikot.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (PLAYER_SIZE, PLAYER_SIZE))
player_x = SCREEN_WIDTH // 2 - PLAYER_SIZE // 2
player_y = SCREEN_HEIGHT - 100
player_speed = 5

# Projectile
bullet_img = pygame.image.load("png-bullet.png").convert_alpha()
bullet_img = pygame.transform.scale(bullet_img, (10, 30))
bullets = []
bullet_speed = 10

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Enemies
enemies = []
ENEMY_INITIAL_SPEED = 1.5

for i in range(ENEMY_COUNT):
    enemy_img = pygame.image.load("png-enemyship.png").convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (ENEMY_SIZE, ENEMY_SIZE))
    enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
    enemy_y = random.randint(50, 200)
    enemy_speed = ENEMY_INITIAL_SPEED  # Initial speed
    enemies.append([enemy_img, enemy_x, enemy_y, enemy_speed])

# Game Over variables
max_enemy_touches = 3
max_enemy_passes = 8
enemy_touches = 0
enemy_passes = 0

# Wave Variables
WAVE_COUNT = 10
WAVE_SCORE_THRESHOLD = 30

# New variables for wave information
wave_names = [
    "                   Wave 1",
    "      :            Wave 2",
    "      :            Wave 3",
    "      :            Wave 4",
    "      :            Wave 5",
    "      :            Wave 6",
    "      :            Wave 7",
    "      :            Wave 8",
    "      :            Wave 9",
    "      :                            FINAL WAVE",
]
current_wave = 0

# Play Button
play_button_img = pygame.image.load("PLAY BUTTON  NEW.png").convert_alpha()
play_button_img = pygame.transform.scale(play_button_img, (450, 150))
play_button_rect = play_button_img.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

def display_play_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    return

        screen.fill(WHITE)
        screen.blit(intro_background_img, (0, 0))
        screen.blit(play_button_img, play_button_rect)

        pygame.display.update()
        clock.tick(60)

# Function to draw score
def show_score(x, y):
    score_render = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_render, (x, y))

# Function to display intro text
def display_intro(intro_text, duration, font_size=32):
    screen.blit(intro_background_img, (0, 0))
    intro_font = pygame.font.Font('freesansbold.ttf', font_size)
    intro_text_render = intro_font.render(intro_text, True, (255, 255, 255))
    intro_text_rect = intro_text_render.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(intro_text_render, intro_text_rect)
    pygame.display.update()
    time.sleep(duration)

# Function to display intro text with multiple lines
def display_intro_multi_line(lines, duration, font_size=32):
    screen.blit(intro_background_img, (0, 0))
    intro_font = pygame.font.Font('freesansbold.ttf', font_size)

    y_position = SCREEN_HEIGHT // 2 - len(lines) * (font_size + 5) // 2

    for line in lines:
        intro_text_render = intro_font.render(line, True, (255, 255, 255))
        intro_text_rect = intro_text_render.get_rect(center=(SCREEN_WIDTH // 2, y_position))
        screen.blit(intro_text_render, intro_text_rect)
        y_position += font_size + 5

    pygame.display.update()
    time.sleep(duration)

# Creator's name
def display_creator():
    creator_font = pygame.font.Font('freesansbold.ttf', 14)
    creator_text = creator_font.render("Reha Demircan", True, (255, 255, 255))
    creator_text_rect = creator_text.get_rect(bottomright=(SCREEN_WIDTH - 10, SCREEN_HEIGHT - 10))
    screen.blit(creator_text, creator_text_rect)
    pygame.display.update()

# Play menu
display_play_menu()

# Intro 1
display_intro("SPACE INVADERS", 8)

# Intro 2 with multiple lines
intro_text_2_lines = [
    "In a long endless universe on the distant edges of the galaxy  there is numberless lives and planets",
    "you live peacefully in your galaxy, at the one of your travels you get caught at a middle  raid of Invaders",
    "You find yourself in the middle of a galactic conflict with them..",
    "Do not let them pass you    Enemies get faster each 3 waves ! "
]
display_intro_multi_line(intro_text_2_lines, 15, font_size=19)

# Intro 3
screen.blit(intro_background_img, (0, 0))
display_creator()
intro_text_3 = "Made with PYGAME."
intro_font_3 = pygame.font.Font('freesansbold.ttf', 20)
intro_text_render_3 = intro_font_3.render(intro_text_3, True, (255, 255, 255))
intro_text_rect_3 = intro_text_render_3.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
screen.blit(intro_text_render_3, intro_text_rect_3)
pygame.display.update()
time.sleep(3)

# Intro 4
display_intro("Use W, A, S, D to move and Space button to shoot.", 4, font_size=18)
display_intro("You have 3 lives; do not let enemies reach the bottom!", 4, font_size=18)

# Game loop starts after intros
running = True
clock = pygame.time.Clock()

# Reset game-over variables
max_enemy_touches = 3
max_enemy_passes = 6
enemy_touches = 0
enemy_passes = 0

# Flag to track if the game is over
game_over = False

while running:
    screen.fill(WHITE)
    screen.blit(intro_background_img, (0, 0))  # Use intro background for gameplay

    # Display wave name on the top-left corner
    wave_name_render = font.render(wave_names[current_wave], True, (255, 255, 255))
    screen.blit(wave_name_render, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + PLAYER_SIZE // 2 - 5
                bullet_y = player_y
                bullets.append([bullet_x, bullet_y])

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
        player_x += player_speed
    if keys[pygame.K_w] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_s] and player_y < SCREEN_HEIGHT - PLAYER_SIZE:
        player_y += player_speed

    # Move bullets
    for bullet in bullets:
        bullet[1] -= bullet_speed

    # Draw player
    screen.blit(player_img, (player_x, player_y))

    # Draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

    # Draw enemies
    for enemy in enemies:
        screen.blit(enemy[0], (enemy[1], enemy[2]))
        enemy[2] += enemy[3]

        # Check if enemy touches the player
        if (
            player_x < enemy[1] < player_x + PLAYER_SIZE
            and player_y < enemy[2] < player_y + PLAYER_SIZE
        ):
            enemy_touches += 1
            enemy[1] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemy[2] = random.randint(-200, -50)

        # Check if enemy passes the line
        if enemy[2] > SCREEN_HEIGHT:
            enemy_passes += 1
            enemy[1] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
            enemy[2] = random.randint(-200, -50)

    # Collision detection between bullet and enemy
    for enemy in enemies:
        for bullet in bullets:
            if 0 <= bullet[0] - enemy[1] <= ENEMY_SIZE and 0 <= bullet[1] - enemy[2] <= ENEMY_SIZE:
                if bullet in bullets:
                    bullets.remove(bullet)
                score += 1
                enemy[1] = random.randint(0, SCREEN_WIDTH - ENEMY_SIZE)
                enemy[2] = random.randint(-200, -50)

    # Check game-over conditions
    if enemy_touches >= max_enemy_touches or enemy_passes >= max_enemy_passes:
        game_over = True

    # Check if the score threshold for the next wave is reached
    if score >= (current_wave + 1) * WAVE_SCORE_THRESHOLD:
        current_wave += 1

        if current_wave == WAVE_COUNT:
            # End game message
            game_over = True

        # Adjust enemy speed based on the current wave
        for enemy in enemies:
            if 1 <= current_wave < 1:
                enemy[3] = 0.5 * ENEMY_INITIAL_SPEED
            elif 3 <= current_wave <8:
                enemy[3] = ENEMY_INITIAL_SPEED
            elif 6 <= current_wave <9:
                enemy[3] = 2 * ENEMY_INITIAL_SPEED
            elif current_wave ==10:
                enemy[3] = 3 * ENEMY_INITIAL_SPEED

    # Update score on the screen
    show_score(text_x, text_y)

    pygame.display.update()
    clock.tick(60)

    # Game over logic
    if game_over:
        screen.blit(game_over_background_img, (0, 0))
        display_creator()
        game_over_font = pygame.font.Font('freesansbold.ttf', 20)
        game_over_text = game_over_font.render(
            "Game Over!", True, (255, 255, 255)
        )
        game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(game_over_text, game_over_text_rect)
        pygame.display.update()
        pygame.time.delay(3000)  # 3000 milliseconds (3 seconds)
        break

pygame.quit()

