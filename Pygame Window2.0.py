import pygame
pygame.init()
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_CAPTION = "MY FIRST GAME SCREEN"
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
IMAGE_SIZE = (IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_FILENAME = 'Adasaurus.jpg'
GREY = (58, 58, 58)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_CAPTION)
original_image = pygame.image.load(IMAGE_FILENAME)
game_image = pygame.transform.scale(original_image, IMAGE_SIZE)
game_image = pygame.Surface(IMAGE_SIZE)
game_image.fill(RED)
font = pygame.font.Font(None, 36)
text_surface = font.render("Image Not Found", True, WHITE)
text_rect = text_surface.get_rect(center=(IMAGE_WIDTH // 2, IMAGE_HEIGHT // 2))
game_image.blit(text_surface, text_rect)
image_rect = game_image.get_rect()
image_rect.centerx = WINDOW_WIDTH // 2
image_rect.centery = WINDOW_HEIGHT // 2
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill(GREY)
    screen.blit(game_image, image_rect)
    pygame.display.flip()
pygame.quit()