import os
import sys
import pygame
import requests
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton, QApplication, QWidget

x = 135
y = -27
size = 25
sp = ['map', 'sat', 'sat,skl', 'sat,trf,skl']
bfon = pygame.transform.scale(pygame.image.load("New game Button.png"), (600 * 0.19, 450 * 0.2))
bfon1 = pygame.transform.scale(pygame.image.load("New Game  col_Button.png"), (600 * 0.19, 450 * 0.2))
c = 0

class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.lineyka = QLineEdit
        self.searchnow = QPushButton("Поиск")
        self.searchnow.clicked.connect(self.searchprocess)

    def searchprocess(self):
        print("kys now")

def between(x, x1, y):
    if x < y < x1:
        return True
    else:
        return False
def pr():
    # K = Search
    # K.show()
    print("ТЫ РАЗГОВОРИВАЕШЬ????")

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h, text, font, fon, screen, group, func):
        super().__init__(group)
        self.x, self.y, self.w, self.h, self.text, self.font, self.fon, self.screen = x, y, w, h, text, font, fon, screen
        self.rect = pygame.Rect(x, y, w, h)
        self.image0 = fon[0]
        self.image1 = fon[1]
        self.image = self.image0
        self.func = func

    def update(self):
        mx, my = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        if self.x < mx < self.x + self.w and self.y < my < self.y + self.h:
            self.image = self.image1
        else:
            self.image = self.image0

    def check(self):
        if self.image == self.image1:
            self.func()

map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={size},{size}&l=sat"

pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
sprites = pygame.sprite.Group()
Button(0,0,600,450,123,"123", [bfon, bfon1], screen, sprites, pr)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.key.get_pressed()[pygame.K_PAGEUP]:
        size = size * 1.1
    if pygame.key.get_pressed()[pygame.K_PAGEDOWN]:
        size = size * 0.9
    if pygame.key.get_pressed()[pygame.K_w]:
        y += 2 * size / 25
    if pygame.key.get_pressed()[pygame.K_a]:
        x -= 2 * size / 25
    if pygame.key.get_pressed()[pygame.K_s]:
        y -= 2 * size / 25
    if pygame.key.get_pressed()[pygame.K_d]:
        x += 2 * size / 25
    if pygame.key.get_pressed()[pygame.K_1]:
        c = 0
    if pygame.key.get_pressed()[pygame.K_2]:
        c = 1
    if pygame.key.get_pressed()[pygame.K_3]:
        c = 2
    if pygame.key.get_pressed()[pygame.K_4]:
        c = 3
    mkeys = pygame.mouse.get_pressed()
    for i in sprites:
        i.update()
    if mkeys[0]:
        for i in sprites:
            i.check()
    screen.fill((255, 255, 255))
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&spn={size},{size}&l={sp[c]}"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load("map.png"), (0, 0))
    sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(40)

    os.remove(map_file)