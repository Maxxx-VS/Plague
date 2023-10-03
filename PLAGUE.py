import pygame
import random
import time

clock = pygame.time.Clock() # добавляем часы в игру
pygame.init() # инициализайия игры
screen = pygame.display.set_mode((1366, 710)) # размер экрана (600, 300, flags=pygame.NOFRAME)-окно без рамок
pygame.display.set_caption('PLAGUE') # определяет название проекта
icon = pygame.image.load('GAME/Plague.png').convert_alpha() # определяет иконку проекта
pygame.display.set_icon(icon) # устанавливает иконку проекта
bg = pygame.image.load('GAME/BG-P.jpg') # создаем задний фон окна
bg_sound = pygame.mixer.Sound('GAME/Plague.mp3') # переменная для звуков
bg_sound.play()
font = pygame.font.SysFont(None, 40)
label = pygame.font.SysFont(None, 40) # переменная хранящая в себе информацию о характеристике надписи
lose_label = label.render(f'КОМАНДА ПРОИГРАЛА!', False, (193, 196, 199)) # текст на экран проигрыша
restsrt_label = label.render('ЗАПУСТИТЬ ЗАНОВО?', False, (115, 132, 148)) # текст на экрана перезапуска
restsrt_label_rect = restsrt_label.get_rect(topleft=(180, 200)) # создание рамки у текст на экрана перезапуска
FPS = 5
r = 100
max_score = 99999
max_speed = 1.025
min_speed = 1.015
total_1 = 0

def draw_text_A1(screen, text): # функция для размещения цифр в цкетре
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect() # создал невидимый квадрат вокруг цифр
    text_rect.center = (100, 100) # опрделил ценр для размещения цифр
    screen.blit(text_surface, text_rect) # разместил цифры

def draw_text_A2(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (100, 350)
    screen.blit(text_surface, text_rect)

def draw_text_A3(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (100, 600)
    screen.blit(text_surface, text_rect)

def draw_text_B1(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (1200, 100)
    screen.blit(text_surface, text_rect)

def draw_text_B2(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (1200, 350)
    screen.blit(text_surface, text_rect)

def draw_text_B3(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (1200, 600)
    screen.blit(text_surface, text_rect)

def draw_text_C1(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (500, 150)
    screen.blit(text_surface, text_rect)

def draw_text_C2(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (500, 550)
    screen.blit(text_surface, text_rect)

def draw_text_C3(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (750, 300)
    screen.blit(text_surface, text_rect)

def draw_text_C4(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (750, 600)
    screen.blit(text_surface, text_rect)

def draw_total(screen, text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (100, 20)
    screen.blit(text_surface, text_rect)

score_A1 = random.randint(3, 5) + random.random() # генерируем первоначальное значение в круге
score_A2 = random.randint(3, 5) + random.random()
score_A3 = random.randint(3, 5) + random.random()
score_B1 = random.randint(3, 5) + random.random()
score_B2 = random.randint(3, 5) + random.random()
score_B3 = random.randint(3, 5) + random.random()
score_C1 = random.randint(3, 5) + random.random()
score_C2 = random.randint(3, 5) + random.random()
score_C3 = random.randint(3, 5) + random.random()
score_C4 = random.randint(3, 5) + random.random()

gameplay = True
running = True

while running:
    clock.tick(FPS) # устанавливаем задержку
    screen.blit(bg, (0, 0))  # размещаем задний фон окна
    mouse = pygame.mouse.get_pos()  # создаем переменную для определения координаты мышки

    if gameplay:  # условие, игра запущена пока один игрок не проиграл

        if score_A1  < max_score:
            score_A1 = round(score_A1 * max_speed, 1) # увеличивем на каждой итерации значение на 5%
        else:
            score_A1 = max_score
        if score_A2 < max_score:
            score_A2 = round(score_A2 * max_speed, 1)
        else:
            score_A2 = max_score
        if score_A3 < max_score:
            score_A3 = round(score_A3 * max_speed, 1)
        else:
            score_A3 = max_score
        if score_B1  < max_score:
            score_B1 = round(score_B1 * max_speed, 1)
        else:
            score_B1 = max_score
        if score_B2 < max_score:
            score_B2 = round(score_B2 * max_speed, 1)
        else:
            score_B2 = max_score
        if score_B3 < max_score:
            score_B3 = round(score_B3 * max_speed, 1)
        else:
            score_B3 = max_score
        if score_C1  < max_score:
            score_C1 = round(score_C1 * min_speed, 1) # увеличивем на каждой итерации значение на 3%
        else:
            score_C1 = max_score
        if score_C2  < max_score:
            score_C2 = round(score_C2 * min_speed, 1)
        else:
            score_C2 = max_score
        if score_C3  < max_score:
            score_C3 = round(score_C3 * min_speed, 1)
        else:
            score_C3 = max_score
        if score_C4  < max_score:
            score_C4 = round(score_C4 * min_speed, 1)
        else:
            score_C4 = max_score

        obg_A1 = pygame.draw.circle(screen, (255, 0, 75), (100, 100), (score_A1/r))  # создаем круг, размещаем в окне, цвет, координаты, радиус
        obg_A2 = pygame.draw.circle(screen, (255, 0, 75), (100, 350), (score_A2/r))
        obg_A3 = pygame.draw.circle(screen, (255, 0, 75), (100, 600), (score_A3/r))
        obg_B1 = pygame.draw.circle(screen, (0, 255, 255), (1200, 100), (score_B1/r))
        obg_B2 = pygame.draw.circle(screen, (0, 255, 255), (1200, 350), (score_B2/r))
        obg_B3 = pygame.draw.circle(screen, (0, 255, 255), (1200, 600), (score_B3/r))
        obg_C1 = pygame.draw.circle(screen, (128, 128, 128), (500, 150), (score_C1/r))
        obg_C2 = pygame.draw.circle(screen, (128, 128, 128), (500, 550), (score_C2/r))
        obg_C3 = pygame.draw.circle(screen, (128, 128, 128), (750, 300), (score_C3/r))
        obg_C4 = pygame.draw.circle(screen, (128, 128, 128), (750, 600), (score_C4/r))

        draw_text_A1(screen, f"{int(score_A1)}") # вызов функции для размещения цифр в цкетре
        draw_text_A2(screen, f"{int(score_A2)}")
        draw_text_A3(screen, f"{int(score_A3)}")
        draw_text_B1(screen, f"{int(score_B1)}")
        draw_text_B2(screen, f"{int(score_B2)}")
        draw_text_B3(screen, f"{int(score_B3)}")
        draw_text_C1(screen, f"{int(score_C1)}")
        draw_text_C2(screen, f"{int(score_C2)}")
        draw_text_C3(screen, f"{int(score_C3)}")
        draw_text_C4(screen, f"{int(score_C4)}")
        draw_total(screen, f'TOTAL = {int(total_1)}')


        label_A1 = label.render(f'{score_A1}', False, (0, 0, 0)) # создаем текстовый лейбл для цифр
        label_A1_rect = label_A1.get_rect(centerx = 100, centery = 100) # создаем рамку вокруг цифр (принимет только string)
        label_A2 = label.render(f'{score_A2}', False, (0, 0, 0))
        label_A2_rect = label_A2.get_rect(centerx = 100, centery = 350)
        label_A3 = label.render(f'{score_A3}', False, (0, 0, 0))
        label_A3_rect = label_A3.get_rect(centerx = 100, centery = 600)
        label_B1 = label.render(f'{score_B1}', False, (0, 0, 0))
        label_B1_rect = label_B1.get_rect(centerx = 1200, centery = 100)
        label_B2 = label.render(f'{score_B2}', False, (0, 0, 0))
        label_B2_rect = label_B2.get_rect(centerx = 1200, centery = 350)
        label_B3 = label.render(f'{score_B3}', False, (0, 0, 0))
        label_B3_rect = label_B3.get_rect(centerx = 1200, centery = 600)
        label_C1 = label.render(f'{score_C1}', False, (0, 0, 0))
        label_C1_rect = label_C1.get_rect(centerx = 500, centery = 150)
        label_C2 = label.render(f'{score_C2}', False, (0, 0, 0))
        label_C2_rect = label_C2.get_rect(centerx = 500, centery = 550)
        label_C3 = label.render(f'{score_C3}', False, (0, 0, 0))
        label_C3_rect = label_C3.get_rect(centerx = 750, centery = 300)
        label_C4 = label.render(f'{score_C4}', False, (0, 0, 0))
        label_C4_rect = label_C4.get_rect(centerx = 750, centery = 600)

    if label_A1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]: # нажатием ЛКМ помещаем значение в промежуточную переменную, само значение обнуляем
        total_1 += score_A1
        score_A1 = 2
    if label_A2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        total_1 += score_A2
        score_A2 = 2
    if label_A3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
        total_1 += score_A3
        score_A3 = 2

    if label_A1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]: # нажатием ПКМ выгружаем значение из промежуточной переменной, само значение обнуляем
        score_A1 += total_1
        total_1 = 0
    if label_A2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_A2 += total_1
        total_1 = 0
    if label_A3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_A3 += total_1
        total_1 = 0

    if label_B1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        if total_1 > score_B1:
            score_B1 = total_1 - score_B1
            total_1 = 0
        else:
            score_B1 = score_B1 - total_1
            total_1 = 0
    if label_B2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        if total_1 > score_B2:
            score_B2 = total_1 - score_B2
            total_1 = 0
        else:
            score_B2 = score_B2 - total_1
            total_1 = 0
    if label_B3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        if total_1 > score_B3:
            score_B3 = total_1 - score_B3
            total_1 = 0
        else:
            score_B3 = score_B3 - total_1
            total_1 = 0

    if label_C1_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_C1 = total_1 - score_C1
        total_1 = 0
    if label_C2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_C2 = total_1 - score_C2
        total_1 = 0
    if label_C3_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_C3 = total_1 - score_C3
        total_1 = 0
    if label_C4_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[2]:
        score_C4 = total_1 - score_C4
        total_1 = 0


    # else:
    #     screen.fill((87, 88, 89)) # создаем экран проигрыша и перезапуска
    #     screen.blit(lose_label, (180, 100))
    #     screen.blit(restsrt_label, restsrt_label_rect)

    pygame.display.update()  # постоянное обновление экрана

    for event in pygame.event.get(): # перебрали все события в pygame
        if event.type == pygame.QUIT: # создали условия для закрытия окна программы
            running = False
            pygame.quit()