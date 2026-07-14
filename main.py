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
move_right = False
move_left = False
speed_x = 3
speed_y = 3
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

class Label(Area):
    '''
    Clase para objetos de texto
    '''
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



ball = Picture('ball.png', 160, 200, 50, 50)
platform = Picture('platform.png', racket_x, racket_y, 100, 30)

start_x = 5
start_y = 5

count = 9
monsters = []
for j in range(3):
    y = start_y + (55 * j)
    x = start_x + (27.5 * j) 
    for i in range (count):
        d = Picture('enemy.png', x, y, 50, 50)
        monsters.append(d)
        x = x + 55
    count = count - 1

while not game_over:
    ball.fill()
    platform.fill()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    if ball.rect.y < 0:
        speed_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:
        speed_x *= -1
    if ball.colliderect(platform.rect):
        speed_y *= -1
    if len(monsters) == 0:
        win_text = Label(150,150,50,50,back)
        win_text.set_text('GANASTE',60, (0,200,0))
        win_text.draw(10, 10)
        game_over = True

    if ball.rect.y > 350:
        lose_text = Label(150,150,50,50,back)
        lose_text.set_text('PERDISTE',60, (255,0,0))
        lose_text.draw(10, 10)
        game_over = True


    for monster in monsters:
        monster.draw()
        if monster.colliderect(ball.rect):
            monsters.remove(monster)
            monster.fill()
            speed_y *= -1

    platform.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(40)
