from random import randint
from string import whitespace

import pygame
import sys
import random

from pygame.examples.cursors import image
from pygame.time import delay


if __name__ == '__main__':
    # Initialize Pygame
    pygame.init()
    pygame.font.init()
    # Set up the display
    WIDTH, HEIGHT = 916, 916
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    ME = ("me.png", 'me_up.png', 'me_left.png', 'me_down.png')
    ME_SURF = []
    YA = ("ya_right.png", 'ya_up.png', 'ya_left.png', 'ya_down.png')
    YA_SURF = []
    pygame.display.set_caption('Moving Circles with Classes')
    WALLS = ('wall.png', 'wall1.png', 'wall2.png', 'wall3.png')
    WATER = ('water1.png', 'water2.png', 'water3.png', 'water4.png', 'water5.png')
    WALLS_SURF = []
    WATER_SURF = []
    LEMONS = []
    SPIKES = ('spikes1.png', 'spikes2.png', 'spikes3.png')
    SPIKES_SURF =[]
    DICES = ('dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice6.png')
    DICES_SURF = []
    CAGES = ('cage1.png', 'cage2.png', 'cage3.png')
    CAGES_SURF = []
    LEMONS.append(pygame.image.load('lemons.png').convert_alpha())
    ya_stat = []
    de_stat = []
    floor_group = pygame.sprite.Group
    for i in range(len(WALLS)):
        WALLS_SURF.append(pygame.image.load(WALLS[i]).convert_alpha())
    for i in range(len(WATER)):
        WATER_SURF.append(pygame.image.load(WATER[i]).convert_alpha())
    for i in range(len(SPIKES)):
        SPIKES_SURF.append(pygame.image.load(SPIKES[i]).convert_alpha())
    for i in range(len(DICES)):
        DICES_SURF.append(pygame.image.load(DICES[i]).convert_alpha())
    for i in range(len(CAGES)):
        CAGES_SURF.append(pygame.image.load(CAGES[i]).convert_alpha())
    for i in range(len(ME)):
        ME_SURF.append(pygame.image.load(ME[i]).convert_alpha())
    for i in range(len(YA)):
        YA_SURF.append(pygame.image.load(YA[i]).convert_alpha())
    floor_level = []
    # Define colors
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    sp = []
    walllevel = []
    wall_group = pygame.sprite.Group()
    floor1_group = pygame.sprite.Group()
    floor2_group = pygame.sprite.Group()
    floor3_group = pygame.sprite.Group()
    floor4_group = pygame.sprite.Group()
    floor5_group = pygame.sprite.Group()
    # Cell size
    CELL_SIZE = 16
    sp_wall_x = []
    sp_wall_y = []
    sp_wall_height = []
    timerfl = 0
    class wall(pygame.sprite.Sprite):
        def __init__(self, x, y, img, height):
            super().__init__()
            self.image = img
            self.x = x
            self.y = y
            self.height = height
            self.rect = self.image.get_rect(center=(x + 8, y + 8))
            self.mask = pygame.mask.from_surface(self.image)
            sp_wall_x.append(x)
            sp_wall_y.append(y)
            sp_wall_height.append(height)

        def update(self):
            return self.rect()



    class ya_stats():
        def __init__(self, spisoch):
            self.spisoch = spisoch
            self.img1 = pygame.image.load('zero_hearts.png')
            self.img2 = pygame.image.load('half_heart.png')
            self.img3 = pygame.image.load('full_heart.png')
            self.health = self.spisoch[0]
            self.a = self.spisoch[1]
            self.stamina = self.spisoch[1]
            self.smell = self.spisoch[2]
            self.width = 600
            self.height = 50

        def draw(self):
            pygame.draw.rect(screen, WHITE, (self.width, self.height, 100, 200), 1)
            if self.health == 0:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 0.5:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img2, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 1:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 1.5:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img2, rect1)
                rect2 = self.img2.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 2:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 2.5:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img3, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img2, rect3)
            if self.health == 3:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img3, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img3, rect3)
            pygame.draw.rect(screen, GREEN, (self.width + 10, self.height + 30, 20, self.stamina))
            f1 = pygame.font.SysFont('ariel', 20)
            text1 = f1.render(str('ya_stats'), True, WHITE)
            screen.blit(text1, (self.width + 10, self.height + 170))
            if self.smell == 'lemon':
                img = pygame.image.load('lemons.png')
                rect3 = img.get_rect(center=(self.width + 10, self.height + 150))
                screen.blit(img, rect3)


    class de_stats():
        def __init__(self, spisoch):
            self.spisoch = spisoch
            self.img1 = pygame.image.load('zero_hearts.png')
            self.img2 = pygame.image.load('half_heart.png')
            self.img3 = pygame.image.load('full_heart.png')
            self.health = self.spisoch[0]
            self.a = self.spisoch[1]
            self.stamina = self.spisoch[1]
            self.smell = self.spisoch[2]
            self.width = 100
            self.height = 50

        def draw(self):
            pygame.draw.rect(screen, WHITE, (self.width, self.height, 100, 200), 1)
            if self.health == 0:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 0.5:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img2, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 1:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 1.5:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img2, rect1)
                rect2 = self.img2.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img1, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 2:
                rect1 = self.img3.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img1, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img1, rect3)
            if self.health == 2.5:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img3, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img2, rect3)
            if self.health == 3:
                rect1 = self.img1.get_rect(center=(self.width + 10, self.height + 10))
                screen.blit(self.img3, rect1)
                rect2 = self.img1.get_rect(center=(self.width + 20, self.height + 10))
                screen.blit(self.img3, rect2)
                rect3 = self.img1.get_rect(center=(self.width + 30, self.height + 10))
                screen.blit(self.img3, rect3)
            pygame.draw.rect(screen, GREEN, (self.width + 10, self.height + 30, 20, self.stamina))
            f1 = pygame.font.SysFont('ariel', 20)
            text1 = f1.render(str('de_stats'), True, WHITE)
            screen.blit(text1, (self.width + 10, self.height + 170))
            if self.smell == 'lemon':
                img = pygame.image.load('lemons.png')
                rect3 = img.get_rect(center=(self.width + 10, self.height + 150))
                screen.blit(img, rect3)






    class ya_form():
        def __init__(self):
            self.width = 200
            self.height = 600


    class de_form():
        def __init__(self):
            self.width = 200
            self.height = 600

    class floor(pygame.sprite.Sprite):
        def __init__(self, type, x, y):
            super().__init__()
            self.color = 0
            self.x = x
            self.y = y
            self.type = type
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.mask = pygame.mask.from_surface(self.image)


        def update(self):
            if self.type == 1:
                self.image = WATER_SURF[timerfl // 1000]
                floor1_group.add(self)
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.mask = pygame.mask.from_surface(self.image)
            if self.type == 2:
                self.image = LEMONS[0]
                floor2_group.add(self)
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.mask = pygame.mask.from_surface(self.image)
            if self.type == 3:
                self.image = CAGES_SURF[timerfl // 2000]
                floor3_group.add(self)
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.mask = pygame.mask.from_surface(self.image)
            if self.type == 4:
                self.image = DICES_SURF[timerfl // 500]
                floor4_group.add(self)
                self.rect = self.image.get_rect(center=(self.x, self.y))
                self.mask = pygame.mask.from_surface(self.image)
            if self.type == 5:
                self.image = SPIKES_SURF[timerfl // 1500]
                floor5_group.add(self)
                self.rect = self.image.get_rect(center=(self.x, self.y))


        def returner(self):
            return self.type


    class text():
        def __init__(self, textik, fontik, size):
            self.width = 300
            self.textik = textik
            self.height = 100
            self.f1 = pygame.font.SysFont(fontik, size)

        def drawer(self):
            pygame.draw.rect(screen, WHITE, (WIDTH // 2 - self.width//2 , HEIGHT - 100 - self.height, self.width, self.height), 3)
            text1 = self.f1.render(str(self.textik), True, WHITE)
            screen.blit(text1, (WIDTH // 2 - self.width // 2 + 5 , HEIGHT - 100 - self.height + 10))

        def update(self):
            pygame.draw.rect(screen, BLACK,
                             (WIDTH // 2 - self.width // 2, HEIGHT + 100 + self.height, self.width, self.height))

    class grid():
        def __init__(self, x1, x2, y1, y2):
            self.x1 = x1
            self.x2 = x2
            self.y1 = y1
            self.y2 = y2
            self.CELL_SIZE = CELL_SIZE

        def draw_grid(self):
            global sp
            sp.clear()  # Clear previous coordinates
            for x in range(self.x1, self.x2, CELL_SIZE):
                for y in range(self.y1, self.y2, CELL_SIZE):
                    # Draw the grid
                    pygame.draw.rect(screen, WHITE, (x + 6, y + 6, CELL_SIZE, CELL_SIZE), 1)
                    # Store the top-left corner coordinates of each cell
                    sp.append((x, y))

        def collision(self):
            a = 0

    class level():
        def __init__(self, grid):
            self.grid = grid

        def level_returner(self):
            return [WIDTH // 2 - self.grid * CELL_SIZE // 2, WIDTH // 2 + self.grid * CELL_SIZE // 2, HEIGHT // 2 - (self.grid) * CELL_SIZE // 2, HEIGHT // 2 + (self.grid) * CELL_SIZE // 2]

        def posde_returner(self):
            return [WIDTH // 2 - (self.grid - 2) * CELL_SIZE //2, HEIGHT // 2 - (self.grid - 2) * CELL_SIZE//2]

        def de_grid_retuner(self):
            return [HEIGHT // 2 - (self.grid - 2) * CELL_SIZE//2, HEIGHT// 2 + (self.grid - 0.5) * CELL_SIZE //2]

        def ya_grid_retuner(self):
            return [WIDTH // 2 - (self.grid - 2) * CELL_SIZE //2, WIDTH // 2 + (self.grid - 0.5) * CELL_SIZE //2]

        def posya_returner(self):
            return [WIDTH // 2 + (self.grid - 1.5) * CELL_SIZE //2,HEIGHT// 2 + (self.grid - 1.5) * CELL_SIZE //2]

        def memory(self):
            for i in range(0, WIDTH, CELL_SIZE):
                for j in range(0, HEIGHT, CELL_SIZE):
                    if not WIDTH // 2 - self.grid * CELL_SIZE //2 < i < WIDTH // 2 + self.grid * CELL_SIZE //2 or not HEIGHT // 2 - self.grid * CELL_SIZE//2 < j < HEIGHT// 2 + self.grid * CELL_SIZE //2:
                        if WIDTH // 2 - (self.grid + 2) * CELL_SIZE // 2 < i < WIDTH // 2 + (self.grid + 2) * CELL_SIZE // 2 and HEIGHT // 2 - (self.grid + 2) * CELL_SIZE // 2 < j < HEIGHT // 2 + (self.grid + 2) * CELL_SIZE // 2:
                            walllevel.append([i, j])
                    if i > WIDTH and j > HEIGHT:
                        break

        def level_constructor(self):
            for i in range(0, WIDTH, CELL_SIZE):
                for j in range(0, HEIGHT, CELL_SIZE):
                    rand = random.randint(1, 6)
                    if rand != 6:
                        if WIDTH // 2 - self.grid * CELL_SIZE // 2 < i < WIDTH // 2 + self.grid * CELL_SIZE // 2 or  HEIGHT // 2 - self.grid * CELL_SIZE // 2 < j < HEIGHT // 2 + self.grid * CELL_SIZE // 2:
                            floor_level.append([i, j, rand])
                    else:
                        walllevel.append([i, j])


    class Ya(pygame.sprite.Sprite):
        def __init__(self, color, position, radius, grid):
            super().__init__()
            self.smell = None
            self.health = 3
            self.stamina = 100
            self.color = color
            self.position = position
            self.radius = radius
            self.grid = grid
            self.speed = 5
            self.cigs = 3
            self.image = YA_SURF[0]
            global ya_stat
            ya_stat = [self.health, self.stamina, self.smell]
            self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
            self.controls = {
                'up': pygame.K_w,
                'down': pygame.K_s,
                'left': pygame.K_a,
                'right': pygame.K_d
            }
        def check_wall_collision(self, dx, dy):
            self.mask = pygame.mask.from_surface(self.image)
            for wall in wall_group:
                if pygame.sprite.collide_mask(self, wall):
                   self.position[0] -= dx
                   self.position[1] -= dy

        def check_grid_collision(self):
            # Determine the column of the grid cell the circle is currently in
            column = int(self.position[1] // CELL_SIZE)
            # Check if the circle is touching the grid
            for x in range(int(self.grid[0] - 8.5), int(self.grid[1] + 7), CELL_SIZE):
                if x <= self.position[0] <= x + CELL_SIZE:
                    # Highlight the column green if touching the grid
                    pygame.draw.rect(screen, GREEN, ( x, column * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                else:
                    if not x in sp_wall_x and not self.position[1] in sp_wall_y:
                        # Draw the cell back to black if not touching
                        pygame.draw.rect(screen, BLACK, (x, column * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        def check_wall_collision(self, dx, dy):
            for wall in wall_group:
                if pygame.sprite.collide_mask(self, wall):
                   self.position[0] -= dx
                   self.position[1] -= dy
            for fl in floor1_group:
                if pygame.sprite.collide_mask(self, fl):
                    if self.smell == 'lemon':
                        self.position[0] -= dx
                        self.position[1] -= dy
            for fl in floor2_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.smell = 'lemon'
            for fl in floor3_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.health -= 0.5
            for fl in floor4_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.stamina = self.stamina * 1 / 4
            for fl in floor5_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.health += random.randrange(-1, 2, 1) //2
                    self.stamina += random.randrange(-25, 25, 25)
                    #self.position[0] =
                    #self.position[1] =
        def move(self, dx, dy):
            self.position[0] += dx
            self.position[1] += dy



        def update(self):
            global ya_stat
            ya_stat = [self.health, self.stamina, self.smell]
            keys = pygame.key.get_pressed()
            if keys[self.controls['up']]:
                self.move(0, -self.speed)
                self.image = YA_SURF[1]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0] , self.position[1]))
                self.check_wall_collision(0, -self.speed)
            if keys[self.controls['down']]:
                self.move(0, self.speed)
                self.image = YA_SURF[3]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(0, self.speed)
            if keys[self.controls['left']]:
                self.move(-self.speed, 0)
                self.image = YA_SURF[2]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(-self.speed, 0)
            if keys[self.controls['right']]:
                self.move(self.speed, 0)
                self.image = YA_SURF[0]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(self.speed, 0)



    # Circle class for the second sprite
    class De(pygame.sprite.Sprite):
        def __init__(self, color, position, radius, grid):
            super().__init__()
            self.smell = None
            self.health = 3
            self.stamina = 100
            self.color = color
            self.position = list(position)
            self.grid = grid
            self.radius = radius
            self.speed = 5
            self.image = ME_SURF[0]
            global de_stat
            de_stat = [self.health, self.stamina, self.smell]
            self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
            self.mask = pygame.mask.from_surface(self.image)
            self.controls = {
                'up': pygame.K_UP,
                'down': pygame.K_DOWN,
                'left': pygame.K_LEFT,
                'right': pygame.K_RIGHT
            }

        def check_wall_collision(self, dx, dy):
            for wall in wall_group:
                if pygame.sprite.collide_mask(self, wall):
                   self.position[0] -= dx
                   self.position[1] -= dy
            for fl in floor1_group:
                if pygame.sprite.collide_mask(self, fl):
                    if self.smell == 'lemon':
                        self.position[0] -= dx
                        self.position[1] -= dy
            for fl in floor2_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.smell = 'lemon'
            for fl in floor3_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.health -= 0.5
            for fl in floor4_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.stamina = self.stamina * 1 / 4
            for fl in floor5_group:
                if pygame.sprite.collide_mask(self, fl):
                    self.health += random.randrange(-1, 2, 1) //2
                    self.stamina += random.randrange(-25, 25, 25)
                    #self.position[0] =
                    #self.position[1] =


        def move(self, dx, dy):
            self.position[0] += dx
            self.position[1] += dy



        def update(self):
            global de_stat
            de_stat = [self.health, self.stamina, self.smell]
            keys = pygame.key.get_pressed()
            if keys[self.controls['up']]:
                self.move(0, -self.speed)
                self.image = ME_SURF[1]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0] , self.position[1]))
                self.check_wall_collision(0, -self.speed)
            if keys[self.controls['down']]:
                self.move(0, self.speed)
                self.image = ME_SURF[3]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(0, self.speed)
            if keys[self.controls['left']]:
                self.move(-self.speed, 0)
                self.image = ME_SURF[2]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(-self.speed, 0)
            if keys[self.controls['right']]:
                self.move(self.speed, 0)
                self.image = ME_SURF[0]
                self.mask = pygame.mask.from_surface(self.image)
                self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
                self.check_wall_collision(self.speed, 0)


        def check_grid_collision(self):
            # Determine the column of the grid cell the circle is currently in
            column = int(self.position[0] // CELL_SIZE)
            # Check if the circle is touching the grid
            for y in range(int(self.grid[0] - 8.5), int(self.grid[1] + 7), CELL_SIZE):
                if y <= self.position[1] <= y + CELL_SIZE:
                    # Highlight the column green if touching the grid
                    pygame.draw.rect(screen, GREEN, (column * CELL_SIZE, y, CELL_SIZE, CELL_SIZE))
                else:
                    if not self.position[0] in sp_wall_x and not y in sp_wall_y:
                        pygame.draw.rect(screen, BLACK, (column * CELL_SIZE, y, CELL_SIZE, CELL_SIZE))

        def statret(self):
            return [self.stamina, self.health, self.smell]


    level1 = level(20)


    yacoords = [level1.posya_returner()[0], level1.posya_returner()[1]]

    # Create circle instances
    circle_ya = Ya(RED, [yacoords[0], yacoords[1]], 8, level1.ya_grid_retuner())  # Circle controlled by WASD in the top-left corner
    circle_de = De(BLUE, [level1.posde_returner()[0], level1.posde_returner()[1]],
                   8, level1.de_grid_retuner())  # Circle controlled by arrow keys in the bottom-right corner

    # Create sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(circle_ya)
    all_sprites.add(circle_de)
    level1.memory()
    timer = 5000

    schetforwall = 0
    for i in range(len(walllevel)):
        wall_new = wall(walllevel[i][0], walllevel[i][1], WALLS_SURF[random.randint(0,3)], 3)
        wall_group.add(wall_new)
    for i in range(len(floor_level)):
        floor_new = floor(floor_level[i][2], floor_level[i][0], floor_level[i][1])
        floor_group.add(floor_new)
    checker = 0

    font_button = pygame.font.SysFont('ariel', 48)
    button_surface = pygame.Surface((150, 50))
    text_button = font_button.render("START", True, (0, 0, 0))
    text_rect = text_button.get_rect(
        center=(button_surface.get_width() / 2,
                button_surface.get_height() / 2))
    button_rect = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 - 62, 150, 50)
    while True:

        screen.fill(BLACK)
        if checker == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        checker = 1


            if button_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
            else:
                pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
                pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
                pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
                pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

            button_surface.blit(text_button, text_rect)
            screen.blit(button_surface, (button_rect.x, button_rect.y))


        if checker == 1:
            # Update all sprites
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            all_sprites.update()
            a = pygame.time.get_ticks()
            floor1_group.draw(screen)
            floor2_group.draw(screen)
            floor3_group.draw(screen)
            floor4_group.draw(screen)
            floor5_group.draw(screen)
            wall_group.draw(screen)

            timerfl = pygame.time.get_ticks() % 5000
            text1 = text('dont forget to add stats, visualiser, start, changer', "serif", 18)
            if  - pygame.time.get_ticks() + timer > 0:
                text1.drawer()
            elif pygame.time.get_ticks() - timer == 1:
                text1.update()

            # Draw the grid if 'Z' is pressed
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                gr = grid(level1.level_returner()[0], level1.level_returner()[1], level1.level_returner()[2], level1.level_returner()[3])
                gr.draw_grid()

                # Check De's grid collision and draw
                circle_de.check_grid_collision()
                circle_ya.check_grid_collision()


            all_sprites.draw(screen)
            staty = ya_stats(ya_stat)
            statd = de_stats(de_stat)
            staty.draw()
            statd.draw()

            # Update the display
        pygame.display.flip()

            # Maintain the frame rate
        pygame.time.Clock().tick(60)
