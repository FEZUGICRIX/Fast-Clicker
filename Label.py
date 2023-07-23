import pygame
pygame.init()



class Label:
    def __init__(self, screen, x, y, text, counter, time=0):
        # Инициализация класса
        self.font = pygame.font.SysFont('verdana', 30)
        self.lower_image = x + 100
        self.image = self.font.render(text, True, (0, 0, 0))
        self.counter = counter
        self.screen = screen
        self.time = time
        self.x = x
        self.y = y


    def draw(self):
        # Метод отображения элемента Label
        self.lower_image = self.font.render(str(self.counter), True, (19, 33, 191))
        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.lower_image, (self.x + 110, self.y))





