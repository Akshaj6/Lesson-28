import pygame
pygame.init()
SCREENWIDTH, SCREENHEIGHT = 500, 500
display_surface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Adding image and background image')
background_image = pygame.transform.scale(
    pygame.image.load('dinos.jfif').convert(),
    (SCREENWIDTH, SCREENHEIGHT))
dino_image = pygame.transform.scale(
    pygame.image.load('Adasaurus.jpg').convert_alpha(), (200, 200))
dino_rect = dino_image.get_rect(center=(SCREENWIDTH // 2,
                                        SCREENHEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render("Hello World!", True,
                                         pygame.Color('black'))
text_rect = text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 110))
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(dino_image, dino_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
    game_loop()