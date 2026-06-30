import pygame
pygame.init()

back = (200, 255, 255)  # Color de fondo
mw = pygame.display.set_mode((500, 500)) 
mw.fill(back)
clock = pygame.time.Clock()

'''
Variables de las coordenadas de la plataforma
'''
racket_x = 200
racket_y = 330

'''
Bandera del final del juego
'''
game_over = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)       

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Picture(Area):
    '''
    Clase para objetos de imagen
    '''
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
        
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


while not game_over:

    pygame.display.update()
    clock.tick(40)
