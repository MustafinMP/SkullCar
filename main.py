import pygame


import load_image
from menu import Menu
from car import Car
from connector import Connector

WIDTH, HEIGHT = 1440, 960
FPS = 120
size = width, height = WIDTH, HEIGHT

pygame.init()
pygame.display.set_caption('Mustang GT drive')
Icon = pygame.image.load('data/Ford-Mustang-icon.png')
pygame.display.set_icon(Icon)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
car = Car()
conn = Connector()

menu = Menu()

if __name__ == '__main__':
    running = True
    # start = True
    while running:
        screen.fill((0, 0, 0))

        # контроль текущего размера экрана для правильного отображения объектов
        size = width, height = pygame.display.get_window_size()
        d1, d2 = False, False
        s1, s2 = False, False
        for event in pygame.event.get():
            ev = event.type
            if ev == pygame.QUIT:
                running = False
                conn.send('g')
                conn.close()
                break
            if ev == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        car.set_up(True)
                    case pygame.K_DOWN:
                        car.set_down(True)
                    case pygame.K_RIGHT:
                        car.set_right(True)
                    case pygame.K_LEFT:
                        car.set_left(True)
            if ev == pygame.KEYUP:
                match event.key:
                    case pygame.K_UP:
                        car.set_up(False)
                    case pygame.K_DOWN:
                        car.set_down(False)
                    case pygame.K_RIGHT:
                        car.set_right(False)
                    case pygame.K_LEFT:
                        car.set_left(False)
        if car.changed():
            message = car.drive_key() + car.steal_key()
            menu.update_command(message)
            try:
                conn.send(message)
            except Exception:
                print('Disconnected')
        # if not conn.connected():
        #     menu.update_connect_status(False)
        #     try:
        #         conn.connect()
        #         menu.update_connect_status(True)
        #     except Exception:
        #         print('Disconnected')

        menu.draw(screen, width, height)
        pygame.display.flip()
        clock.tick(FPS)

