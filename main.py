import pygame, logic

IMAGES = {}
SQUARE_SIZE = 100

BOARD_COLORS = [pygame.Color('#363636'), pygame.Color('#545454')]

pygame.init()
screen = pygame.display.set_mode((800, 850))
clock = pygame.time.Clock()

running = True

board = logic.initial_state()

def load_images():
    for piece in logic.Pieces:
        res = str(piece)
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("./assets/{piece}.svg".format(piece=res[7:])), (SQUARE_SIZE, SQUARE_SIZE))


def render_board():
    for horizontal in range(8):
        for vertical in range(8):
            color = BOARD_COLORS[((horizontal + vertical) % 2)]
            pygame.draw.rect(screen, color, (horizontal *  SQUARE_SIZE, vertical * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def render_pieces(_board):
    for row in range(8):
        for column in range(8):
            piece = _board[row][column]
            if piece == None:
                break                        
            screen.blit(IMAGES[piece], pygame.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def render_menu_bar():
    pygame.draw.rect(color='black', rect=(0,800,800,50), surface=screen)

def init():
    load_images()

def loop():
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # menu bar

    render_board()

    render_pieces(board)   

    render_menu_bar() 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60


# run    
init()
while running:
    if loop():
        break


pygame.quit()



