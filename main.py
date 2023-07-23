from card import Card
import pygame
from Label import Label
from random import randint

pygame.init()

# Настройки экрана и игры
clock = pygame.time.Clock()
clock.tick()
screen = pygame.display.set_mode((700, 500))
state = 'run'
pygame.display.set_caption('Fast Clicker')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Объекты класса Label для вывода текстовой информации на экран
timer = Label(screen, 8, 10, 'Время:', 1)
points = Label(screen, 550, 10, '  Счёт:', 0, 500)

FPS = 3
time = 0
dt = 1 / FPS

# Создание 4 объектов класса Card - карточек, на которые игрок должен кликать
x = 60
cards = []
for i in range(4):
    cards.append(Card(screen, x, 200))
    x += 150
    Card.draw_frame = True
def setting_state():
    quit_game = Card(screen)
    play_again = Card(screen, x=200, y=350)
    pygame.display.update()

# Основной цикл игры
running = True
while running:
    # Заливка игры цветом
    screen_color = screen.fill((132, 236, 245))
    # Логика статуса игры

    # обработка событий, происходящих в игре
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in cards:
                card.color = (216, 222, 44)
                if event.button == 1 and card.rect.collidepoint(pygame.mouse.get_pos()):
                    if card.draw_click == True:
                        points.counter += 1
                        card.color = (134, 247, 149)
                    else:
                        card.color = (207, 31, 95)

    index = randint(0, 3)
    time += dt
    for i in range(1):
        if timer.counter < time:
            timer.counter += 1
    timer.draw()
    points.draw()

    for i, card in enumerate(cards):
        if i == index:
            card.draw_click = True
        else:
            card.draw_click = False
    for card in cards:
        card.draw()

    if timer.counter == 1 and points.counter == 0:
        state = 'win'

    if timer.counter == 0 and points.counter < 5:
        state = 'lose'

    if state == 'win':
        setting_state()
        pygame.display.update()

    elif state == 'lose':
        # setting_state((255, 0, 0))
        pygame.display.update()

    # Определение Кадров в секунду и обновление дисплея
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()