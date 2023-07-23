import pygame
pygame.init()

class Card:
    def __init__(self, screen, x=60, y=200, text=None, text_color=(0, 0, 0), color=(216, 222, 44), width=120, height=180):
        # Инициализация класса
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color
        self.width = width
        self.height = height
        self.frame = pygame.Rect(self.x, self.y, self.width + 5, self.height + 4)
        self.draw_frame = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.font = pygame.font.SysFont('verdana', 30)

        self.text_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text_color = text_color
        self.image = self.font.render(text, True, text_color)

        self.click = self.font.render('Click!', True, (0, 0, 0))
        self.draw_click = False

    def draw(self):
        # Отрисовка объектов класса Card
        pygame.draw.rect(self.screen, self.color, self.rect)
        if self.draw_frame:
            pygame.draw.rect(self.screen, (26, 78, 189), self.frame, 5)
        if self.draw_click:
            self.screen.blit(self.click, (self.x + 22, self.y + 65))

        self.screen.blit(self.image, (self.x, self.y))



