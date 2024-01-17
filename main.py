from additions import *
import menu
import pygame
from functools import lru_cache
from random import randint
import sys

animated = 1


@lru_cache(None)
def main_game():
    pygame.mixer.init()
    global animated
    skins = [j for j in open("txts/skins.txt")][0][4]
    # Переменная для анмации динозвара
    animation = 0
    speed_animation_fone = 20
    animation_fone_b = 0
    animation_fone_a = 0
    anim_fone = 1
    # Сам экран игры
    size = 1600, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Dinosavr')
    #
    pygame.font.init()
    # Переменные для игрока
    jumps = 0
    hero_fall = 3
    hero_jump = 5

    # Переменные для врагов
    enemy_col = 1000
    shipi_speed = 4
    # Все группы спрайтов
    enemyes_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    additional = pygame.sprite.Group()
    for_oblako = pygame.sprite.Group()
    # Коэффициент для ускорения врагов со временем
    coeff = 500

    # Фон
    sky = pygame.sprite.Sprite(all_sprites)
    sky.image = load_image(f'fon/sky{anim_fone}.png')
    sky.rect = sky.image.get_rect()
    # Земля
    dirt = pygame.sprite.Sprite(all_sprites)
    dirt.image = load_image('fon/dirt.png')
    dirt.rect = sky.image.get_rect()
    dirt.rect.y = 732

    # TEST
    trap = pygame.sprite.Sprite(all_sprites)
    trap.image = load_image('trap.png', -1)
    trap.rect = sky.image.get_rect()
    trap.rect.y = 900
    trap.rect.x = 1500
    # TEST
    dragon = pygame.sprite.Sprite(all_sprites)
    dragon.image = load_image('Dragon.png', -1)
    dragon.rect = sky.image.get_rect()
    dragon.rect.y = 900
    dragon.rect.x = 1500

    # Облако Test
    oblako_coll = 500
    oblako_speed = 1
    oblako = pygame.sprite.Sprite(for_oblako)
    oblako.image = load_image('oblako.png', -1)
    oblako.rect = oblako.image.get_rect()
    oblako.rect.y = 1500
    oblako.rect.x = 1600

    # Пальма
    plm_cf = 1
    palma_coeff = plm_cf
    palma_speed = 2
    palma = pygame.sprite.Sprite(all_sprites)
    palma.image = load_image('fon/palma.png', -1)
    palma.rect = palma.image.get_rect()
    palma.rect.y = 287
    palma.rect.x = 700

    # Диназуврик
    hero = pygame.sprite.Sprite(all_sprites)
    hero.image = load_image('dinosavr1_1.png', -1)
    hero.rect = hero.image.get_rect()
    hero.rect.x = 90
    hero.rect.y = 400

    # Переменная для игрового процесса
    running = True
    # TEST

    # Увеличение скорости с овременем
    time_speed = 250
    # Текст
    txt = pygame.font.Font(None, 100)
    # Деньги и счет
    try:
        with open('txts/money.txt', mode='r') as f:
            money1 = int(f.read())
        print('Файл "money.txt" успешно считан')
    except RepackError:
        print('Не удалось считать файл')
        print('Сейчас устраним проблему!')
        with open('txts/money.txt', mode='w') as f:
            f.write('0')
        with open('txts/money.txt', mode='r') as f:
            money1 = int(f.read())

    try:
        with open('txts/max_score.txt', mode='r') as sc:
            max_score = int(sc.read())
        print('Файл "max_score.txt" успешно считан')
    except RepackError:
        print('Не удалось считать файл')
        print('Сейчас устраним проблему!')
        with open('txts/max_score.txt', mode='w') as sc:
            sc.write('0')
        with open('txts/max_score.txt', mode='r') as sc:
            max_score = int(sc.read())

    score = 0
    add_score = 0.01

    # Переменная с помощью которой динозвар менят картинки
    change_image = 0
    # Переменная чтобы во время проигрыша нельзя было менять картинки динозавра
    helps = 1
    # Игровой процесс
    continiu = 1
    colichestvo_pereprignutih_prepatstviy = 0
    # Звуки###############################################
    # Прыжок
    dinosavr_jump = pygame.mixer.Sound('sounds/Jump.wav')
    dinosavr_jump.set_volume(0.09)
    # Score
    display_score = pygame.mixer.Sound('sounds/Score.wav')
    display_score.set_volume(0.09)
    # Death
    death_dinosavr = pygame.mixer.Sound('sounds/Death.wav')
    death_dinosavr.set_volume(0.09)
    # Press button
    button_go = pygame.mixer.Sound('sounds/Buttons.wav')
    button_go.set_volume(0.09)
    # Going dinosavr
    going_dinosavr = pygame.mixer.Sound('sounds/Going.wav')
    going_dinosavr.set_volume(0.04)
    godinsv = 0
    # Геймплей ############################################
    while running:
        # Звук ходьбы динозвара
        godinsv += 1
        if godinsv >= 55 and dirt.rect.y - hero.rect.y <= 300:
            godinsv = 0
            going_dinosavr.play()
        # Анимации
        if change_image == 1:
            if animation <= 50:
                animated = 1
                hero.image = load_image(f'dinosavr_down{animated}_{skins}.png', -1)
                hero_jump = 0
            if animation >= 50:
                animated = 2
                hero.image = load_image(f'dinosavr_down{animated}_{skins}.png', -1)
                hero_jump = 0
        # Анимации
        if change_image == 0:
            if animation <= 50:
                animated = 1
                hero.image = load_image(f'dinosavr{animated}_{skins}.png', -1)
                hero_jump = 5
            if animation >= 50:
                animated = 2
                hero_jump = 5
                hero.image = load_image(f'dinosavr{animated}_{skins}.png', -1)
        # Текст счета
        text_score = txt.render(f"Score: {round(score)}", True, (0, 0, 0))
        screen.fill(pygame.Color("black"))

        # Ивенты
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        key = pygame.key.get_pressed()
        # Чтобы бесконечного джампа небыло
        if key[pygame.K_SPACE] and dirt.rect.y - hero.rect.y <= 300 and change_image != 1:
            going_dinosavr.stop()
            dinosavr_jump.play()
            jumps = 70
        # Для переключения положения динозавра
        if key[pygame.K_DOWN] and helps == 1:
            change_image = 1
        else:
            change_image = 0
        # Функции платформера
        if jumps == 0 and hero.rect.y < dirt.rect.y - 300:
            hero.rect.y += hero_fall
        if jumps > 0:
            hero.rect.y -= hero_jump
            jumps -= 1

        if oblako_coll <= 0:
            oblako = pygame.sprite.Sprite(for_oblako)
            oblako.image = load_image('oblako.png', -1)
            oblako.rect = oblako.image.get_rect()
            oblako.rect.y = randint(0, randint(2, 200))
            oblako.rect.x = 1600
            oblako_coll = 650
        if oblako_coll > 0:
            oblako_coll -= 1
        # Spawn шипов и птичек
        if enemy_col == 0:
            randm = randint(0, 1)
            if randm == 0:
                trap = pygame.sprite.Sprite(enemyes_group)
                trap.image = load_image('trap.png', -1)
                trap.rect = trap.image.get_rect()
                trap.rect.x = 1600
                trap.rect.y = 665
                enemy_col = coeff
                colichestvo_pereprignutih_prepatstviy += 1
            if randm == 1:
                dragon = pygame.sprite.Sprite(enemyes_group)
                dragon.image = load_image('Dragon.png', -1)
                dragon.rect = dragon.image.get_rect()
                dragon.rect.x = 1600
                randm = randint(0, 1)
                if randm == 0:
                    dragon.rect.y = 550
                else:
                    dragon.rect.y = hero.rect.y - 80
                enemy_col = coeff
                colichestvo_pereprignutih_prepatstviy += 1

        # Для передвижения врагов
        if enemy_col > 0:
            enemy_col -= 1

        # Перемоещние облаков
        for sk in for_oblako:
            if sk.rect.x < -300:
                for_oblako.remove(sk)
            sk.rect.x -= oblako_speed

        # Передвижение пальмы
        if palma_coeff > 0:
            palma_coeff -= 1
        if palma_coeff <= 0:
            palma_coeff = plm_cf
            palma.rect.x -= palma_speed
        if palma.rect.x < -300:
            palma.rect.x = 1600

        # Перебор всех спрайтов
        for i in enemyes_group:

            # Оптимизация
            if i.rect.x < -300:
                enemyes_group.remove(i)

            # Передвижение шипов
            i.rect.x -= shipi_speed

            # Колизия: End game
            if pygame.sprite.collide_mask(hero, i):
                # Звук смерти
                death_dinosavr.play()
                # Удаление всех врагов
                delete_sprites(enemyes_group)

                # Максимальный счет
                if score > max_score:
                    max_score = round(score)
                money = int(score * 0.1)
                text_money = txt.render(f"Got money: {money}", True, (0, 0, 0))
                pygame.time.wait(1000)

                # Функция которая выводит результаты после проигрыша
                all_sprites.draw(screen)
                for_oblako.draw(screen)
                lose(screen)

                # Вывод результатов
                screen.blit(text_score, (450, 250))
                screen.blit(text_money, (450, 350))

                # Функция из главного файла для чего-то там
                # Кнопка продолжить
                cont = pygame.sprite.Sprite(additional)
                cont.image = load_image('continue.png')
                cont.rect = trap.image.get_rect()
                cont.rect.x = 550
                cont.rect.y = 600
                additional.draw(screen)
                pygame.display.flip()
                # Цикл пока игрок не нажмет на кнопку продолжить
                pygame.mixer.music.stop()

                # Звук вывода счета
                display_score.play()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.pos[0] in range(550, 550 + 480) and event.pos[1] in range(600, 600 + 142):
                                button_go.play()
                                pygame.time.wait(200)
                                try:
                                    pygame.quit()
                                except ExitError:
                                    print('Game quit')
                                # Сохранение денег
                                with open('txts/money.txt', mode='w') as f:
                                    f.write(str(int(money) + int(money1)))

                                # Сохранение счета
                                with open('txts/max_score.txt', mode='w') as scr:
                                    scr.write(str(max_score))
                                # Переход в меню
                                menu.main_menu()
                                sys.exit()
        # Для анимаций
        animation += 1
        if animation >= 100:
            animation = 0

        # Передвижение фона
        if animation_fone_a - animation_fone_b == speed_animation_fone:
            anim_fone += 1
            sky.image = load_image(f'fon/sky{anim_fone}.png')
            animation_fone_b = animation_fone_a

        # Анимации фона
        if anim_fone >= 13:
            anim_fone = 1

        # Для анимации фона
        if animation_fone_a >= 2000:
            animation_fone_b = 0
            animation_fone_a = 0

        animation_fone_a += 1
        # Условие для паузы(наверное)
        if continiu == 1:
            # Увеличение скорости врагов со временем
            if time_speed > 0:
                time_speed -= 0.01
            if time_speed <= 0:
                time_speed = 250
                shipi_speed += 1
                speed_animation_fone -= 2
                add_score += 0.02
            # Увеличение счета
            score += add_score
            # Вывод на экран спрайтов
            all_sprites.draw(screen)
            enemyes_group.draw(screen)
            for_oblako.draw(screen)
            # Вывод текста счета
            screen.blit(text_score, (1000, 10))
            pygame.display.flip()

    # Выход
    try:
        sys.exit()
    except ExitError:
        print('Exit Error')
