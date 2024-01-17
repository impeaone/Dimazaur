from additions import *
import sys
import pygame
import main

on = 0
skin = [j for j in open("txts/skins.txt")][0][4]


def main_menu():
    global on, skin
    pygame.mixer.init()
    all_sprites = pygame.sprite.Group()
    pygame.font.init()
    size = 1600, 900
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('DimaZaur')
    # Музыка в меню
    pygame.mixer.music.load("sounds/Menu.wav")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    # Звуки
    menu_buttons = pygame.mixer.Sound("sounds/Buttons.wav")  # Кнопки в меню
    menu_buttons.set_volume(0.1)
    buy_dimazaur = pygame.mixer.Sound("sounds/Buy.wav")  # Покупка димазавра
    buy_dimazaur.set_volume(0.1)
    select_skin = pygame.mixer.Sound("sounds/Select_Skin.wav")  # Выбрать скин
    select_skin.set_volume(0.1)

    # скины
    a = [j for j in open("txts/skins.txt")]
    skin2_count, skin3_count = a[0][0], a[0][2]

    # фон
    fon = pygame.sprite.Sprite(all_sprites)
    fon.image = load_image('background.png')
    fon.rect = fon.image.get_rect()

    # кнопка игры
    play = pygame.sprite.Sprite(all_sprites)
    play.image = load_image('play.png')
    play.rect = play.image.get_rect()

    # кнопка магазина
    shop = pygame.sprite.Sprite(all_sprites)
    shop.image = load_image('shop.png')
    shop.rect = shop.image.get_rect()

    # название
    name = pygame.sprite.Sprite(all_sprites)
    name.image = load_image('name.png', -1)
    name.rect = name.image.get_rect()

    # выход
    quit_ = pygame.sprite.Sprite(all_sprites)
    quit_.image = load_image('quit.png')
    quit_.rect = quit_.image.get_rect()

    # фон магазина
    shop_ = pygame.sprite.Sprite(all_sprites)
    shop_.image = load_image('backg_shop.png')
    shop_.rect = shop_.image.get_rect()
    shop_.rect.x = -1600
    shop_.rect.y = -900

    # кнопка назад
    shop_b = pygame.sprite.Sprite(all_sprites)
    shop_b.image = load_image('back_s.png')
    shop_b.rect = shop_b.image.get_rect()
    shop_b.rect.x = -1600
    shop_b.rect.y = -900

    # куплено или нет
    buy_skin = pygame.sprite.Sprite(all_sprites)
    buy_skin.image = load_image('buyed.png')
    buy_skin.rect = buy_skin.image.get_rect()
    buy_skin.rect.x, buy_skin.rect.y = -1600, -1600

    nbuy_skin2 = pygame.sprite.Sprite(all_sprites)
    nbuy_skin2.image = load_image('NotBuyed.png')
    nbuy_skin2.rect = nbuy_skin2.image.get_rect()
    nbuy_skin2.rect.x, nbuy_skin2.rect.y = -1600, -1600

    nbuy_skin3 = pygame.sprite.Sprite(all_sprites)
    nbuy_skin3.image = load_image('NotBuyed.png')
    nbuy_skin3.rect = nbuy_skin3.image.get_rect()
    nbuy_skin3.rect.x, nbuy_skin3.rect.y = -1600, -1600

    # Скины в магазине
    skin1 = pygame.sprite.Sprite(all_sprites)
    skin1.image = load_image('stand1.png', -1)
    skin1.rect = skin1.image.get_rect()
    skin1.rect.x = -1600
    skin1.rect.y = -900

    skin2 = pygame.sprite.Sprite(all_sprites)
    skin2.image = load_image('stand2.png', -1)
    skin2.rect = skin2.image.get_rect()
    skin2.rect.x = -1600
    skin2.rect.y = -900

    skin3 = pygame.sprite.Sprite(all_sprites)
    skin3.image = load_image('stand3.png', -1)
    skin3.rect = skin3.image.get_rect()
    skin3.rect.x = -1600
    skin3.rect.y = -900

    # текст
    txt = pygame.font.Font(None, 100)
    txt2 = pygame.font.Font(None, 100)

    running = True
    while running:
        score = [i for i in open("txts/money.txt")][0].strip()  # Заработанные монеты
        score2 = [i1 for i1 in open("txts/max_score.txt")][0].strip()  # заработанные очки
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                # Вызов игры
                if event.pos[0] in range(560, 560 + 480) and event.pos[1] in range(340, 340 + 142) and on == 0:
                    menu_buttons.play()
                    pygame.time.wait(100)
                    try:
                        pygame.quit()
                    except ExitError:
                        print('Game quit')
                    main.main_game()

                # Выход из игры
                if event.pos[0] in range(560, 560 + 480) and event.pos[1] in range(730, 730 + 142):
                    try:
                        if on == 0:
                            menu_buttons.play()
                            pygame.time.wait(100)
                            pygame.quit()
                            sys.exit()
                    except ExitError:
                        print('Game quit')

                # Выбор скина и его покупка
                if event.pos[1] in range(440, 440 + 337) and on == 1:
                    # Выбрать зелёного динозаврика
                    select_skin.play()
                    if event.pos[0] in range(222, 222 + 333):
                        skin = "1"
                        with open('txts/skins.txt', mode='w') as r:
                            r.write(f"{skin2_count} {skin3_count} 1")

                    # Выбрать розового динозаврика
                    elif event.pos[0] in range(607, 607 + 333):
                        # Выбрать
                        if skin2_count != "0":
                            select_skin.play()
                            skin = "2"
                            with open('txts/skins.txt', mode='w') as r:
                                r.write(f"{skin2_count} {skin3_count} 2")
                        # Купить
                        else:
                            if int(score) >= 100:
                                buy_dimazaur.play()
                                with open('txts/money.txt', mode='w') as f:
                                    f.write(str(int(score) - 100))
                                skin2_count = "1"
                                with open('txts/skins.txt', mode='w') as r:
                                    r.write(f"1 {skin3_count} {skin}")

                    # Выбрать оранжевого динозаврика
                    elif event.pos[0] in range(992, 992 + 333):
                        # Выбрать
                        if skin3_count != "0":
                            select_skin.play()
                            skin = "3"
                            with open('txts/skins.txt', mode='w') as r:
                                r.write(f"{skin2_count} {skin3_count} 3")
                        # Купить
                        else:
                            if int(score) >= 100:
                                buy_dimazaur.play()
                                with open('txts/money.txt', mode='w') as f:
                                    f.write(str(int(score) - 100))
                                skin3_count = "1"
                                with open('txts/skins.txt', mode='w') as r:
                                    r.write(f"{skin2_count} 1 {skin}")
                # Из меню в магазин
                if event.pos[0] in range(560, 560 + 480) and event.pos[1] in range(530, 530 + 142):
                    if on == 0:
                        on = 1
                        menu_buttons.play()

                # Из магазина в меню
                if event.pos[0] in range(10, 10 + 50) and event.pos[1] in range(10, 10 + 47):
                    if on == 1:
                        on = 0
                        menu_buttons.play()

        if on == 0:
            # Меню
            fon.rect.x = 0
            fon.rect.y = 0

            play.rect.x = 560
            play.rect.y = 330

            shop.rect.x = 560
            shop.rect.y = 530

            name.rect.x = 0
            name.rect.y = 0

            quit_.rect.x = 560
            quit_.rect.y = 730

            # Спрайты магазина
            shop_.rect.x = -1600
            shop_.rect.y = -1600
            shop_b.rect.x = -1600
            shop_b.rect.y = -1600
            skin1.rect.x = -1600
            skin1.rect.y = -1600
            skin2.rect.x = -1600
            skin2.rect.y = -1600
            skin3.rect.x = -1600
            skin3.rect.y = -1600
            buy_skin.rect.x, buy_skin.rect.y = -1600, -1600
            nbuy_skin2.rect.x, nbuy_skin2.rect.y = -1600, -1600
            nbuy_skin3.rect.x, nbuy_skin3.rect.y = -1600, -1600

            # вывод колличества очков
            text_score2 = txt2.render(f"Max score: {score2} ", True, (0, 0, 0))
            screen.blit(text_score2, (550, 260))

            pygame.display.flip()
        elif on == 1:
            # Магазин
            shop_.rect.x = 0
            shop_.rect.y = 0

            shop_b.rect.x = 10
            shop_b.rect.y = 10
            # скины
            skin1.rect.x = 222
            skin1.rect.y = 440

            skin2.rect.x = 607
            skin2.rect.y = 440

            skin3.rect.x = 992
            skin3.rect.y = 440

            # Выбор динозаврика
            if skin == "1":
                buy_skin.rect.x, buy_skin.rect.y = 222, 440
            elif skin == "2":
                buy_skin.rect.x, buy_skin.rect.y = 607, 440
            elif skin == "3":
                buy_skin.rect.x, buy_skin.rect.y = 992, 440

            # Розовый динозаврик
            pink_s = txt2.render(f"100", True, (255, 255, 255))
            if skin2_count == "0":
                nbuy_skin2.rect.x, nbuy_skin2.rect.y = 607, 440
                # Розовый скин заблокирован
                screen.blit(pink_s, (660, 435))
            else:
                # Розовый скин разблокирован
                nbuy_skin2.rect.x, nbuy_skin2.rect.y = -1600, -1600
                screen.blit(pink_s, (-1600, -900))

            # Оранжевый динозаврик
            orage_s = txt2.render(f"100", True, (255, 255, 255))
            if skin3_count == "0":
                nbuy_skin3.rect.x, nbuy_skin3.rect.y = 992, 440
                screen.blit(orage_s, (1045, 435))
            else:
                nbuy_skin3.rect.x, nbuy_skin3.rect.y = -1600, -1600
                screen.blit(orage_s, (-1600, -900))

            # вывод колличества монет
            text_score = txt.render(f"Money: {score} ", True, (255, 255, 255))
            screen.blit(text_score, (570, 280))

            pygame.display.flip()

        all_sprites.draw(screen)


main_menu()
