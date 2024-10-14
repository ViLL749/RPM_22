import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Лабиринт')

# Определяем цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Загружаем фон (используйте ваше изображение)
background_image = pygame.image.load('background.jpg')  # Убедитесь, что файл существует
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение фона
    screen.blit(background_image, (0, 0))

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
