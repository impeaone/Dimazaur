import os
import pygame


class ExitError(Exception):
    pass


class RepackError(Exception):
    pass


# Загружать картинки
def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        print('Ошибка(')
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def shipi():
    traps = pygame.sprite.Sprite()
    traps.image = load_image('trap.png', -1)


# Бомбочки просто так
class Bomb(pygame.sprite.Sprite):

    def __init__(self, *group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно!!!
        super().__init__(*group)
        a = load_image('trap.png', -1)
        self.image = a
        self.rect = self.image.get_rect()
        self.rect.x = 585
        self.rect.y = 1500
        print("Бомба поставлена успешно")


# Экран проигрыща
def lose(screen):
    pygame.draw.rect(screen, (0, 0, 0), (395, 195, 810, 610))
    pygame.draw.rect(screen, (128, 128, 128), (400, 200, 800, 600))
    print('Ошибок вывода нет')


# Для удаления всех спрайтов, выбирая какую-либо группу
def delete_sprites(group):
    for i in group:
        group.remove(i)
    else:
        print('Все спрайты удалены успешно')
