import pygame, logic

pygame.init()
screen = pygame.display.set_mode((800, 850))
clock = pygame.time.Clock()

running = True

board = logic.initial_state()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(color='black', rect=(0,0,800,50), surface=screen)
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()