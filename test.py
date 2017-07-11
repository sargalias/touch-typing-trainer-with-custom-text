import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()