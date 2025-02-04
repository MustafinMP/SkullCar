import pygame
from pygame.sprite import Group, Sprite
import load_image

WIDTH, HEIGHT = 1200, 720
FPS = 60
pygame.font.init()

font_label = pygame.font.SysFont('consolas', 32)
label = font_label.render('Mustang GT', True,
                          (240, 242, 245))


class CarMainImage(Sprite):

    def __init__(self, *group) -> None:
        super().__init__(*group)
        self.image = load_image.load_image('car_main.png')

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = [WIDTH // 2 - self.rect.width // 2,
                                    HEIGHT // 2 - self.rect.height // 2]

    def update_position(self, w, h):
        self.rect.x, self.rect.y = [w // 2 - self.rect.width // 2,
                                    h // 2 - self.rect.height // 2]

    def get_top(self):
        return self.rect.top

    def get_bottom(self):
        return self.rect.bottom

    def get_left(self):
        return self.rect.left

    def get_right(self):
        return self.rect.right


class Triangles:
    def __init__(self):
        self.on = False
        self.switch_off()

    def switch_on(self):
        self.on = True

    def switch_off(self):
        self.on = False


class TrianglesUp(Triangles):
    def draw(self, screen, w, car_top, k):
        c1, c2, c3 = (100, 100, 100), (180, 180, 180), (255, 255, 255)
        if self.on:
            if 0 <= k < FPS // 2:
                self.__draw_triangle(screen, (w // 2, car_top - 130), c1)
                self.__draw_triangle(screen, (w // 2, car_top - 90), c1)
                self.__draw_triangle(screen, (w // 2, car_top - 50), c3)
            elif k < FPS:
                self.__draw_triangle(screen, (w // 2, car_top - 130), c1)
                self.__draw_triangle(screen, (w // 2, car_top - 90), c3)
                self.__draw_triangle(screen, (w // 2, car_top - 50), c2)
            elif k < FPS * 1.5:
                self.__draw_triangle(screen, (w // 2, car_top - 130), c3)
                self.__draw_triangle(screen, (w // 2, car_top - 90), c2)
                self.__draw_triangle(screen, (w // 2, car_top - 50), c1)
            else:
                self.__draw_triangle(screen, (w // 2, car_top - 130), c2)
                self.__draw_triangle(screen, (w // 2, car_top - 90), c1)
                self.__draw_triangle(screen, (w // 2, car_top - 50), c1)
        else:
            self.__draw_triangle(screen, (w // 2, car_top - 50), (36, 36, 36))

    @staticmethod
    def __draw_triangle(screen, coord: [int, int], color):
        tx, ty = coord
        pygame.draw.polygon(screen, color, [coord, (tx - 50, ty + 20), (tx - 50, ty + 40),
                                            (tx, ty + 20), (tx + 50, ty + 40), (tx + 50, ty + 20)])


class TrianglesDown(Triangles):
    def draw(self, screen, w, car_bottom, k):
        c1, c2, c3 = (100, 100, 100), (180, 180, 180), (255, 255, 255)
        if self.on:
            if 0 <= k < FPS // 2:
                self.__draw_triangle(screen, (w // 2, car_bottom + 90), c1)
                self.__draw_triangle(screen, (w // 2, car_bottom + 50), c1)
                self.__draw_triangle(screen, (w // 2, car_bottom + 10), c3)
            elif k < FPS:
                self.__draw_triangle(screen, (w // 2, car_bottom + 90), c1)
                self.__draw_triangle(screen, (w // 2, car_bottom + 50), c3)
                self.__draw_triangle(screen, (w // 2, car_bottom + 10), c2)
            elif k < FPS * 1.5:
                self.__draw_triangle(screen, (w // 2, car_bottom + 90), c3)
                self.__draw_triangle(screen, (w // 2, car_bottom + 50), c2)
                self.__draw_triangle(screen, (w // 2, car_bottom + 10), c1)
            else:
                self.__draw_triangle(screen, (w // 2, car_bottom + 90), c2)
                self.__draw_triangle(screen, (w // 2, car_bottom + 50), c1)
                self.__draw_triangle(screen, (w // 2, car_bottom + 10), c1)
        else:
            self.__draw_triangle(screen, (w // 2, car_bottom + 10), (36, 36, 36))

    @staticmethod
    def __draw_triangle(screen, coord: [int, int], color):
        tx, ty = coord
        pygame.draw.polygon(screen, color, [(tx - 50, ty), (tx - 50, ty + 20), (tx, ty + 40),
                                            (tx + 50, ty + 20), (tx + 50, ty), (tx, ty + 20)])


class TrianglesRight(Triangles):
    def draw(self, screen, car_right, h, k):
        c1, c2, c3 = (100, 100, 100), (180, 180, 180), (255, 255, 255)
        if self.on:
            if 0 <= k < FPS // 2:
                self.__draw_triangle(screen, (car_right + 60, h // 2), c1)
                self.__draw_triangle(screen, (car_right + 35, h // 2), c1)
                self.__draw_triangle(screen, (car_right + 10, h // 2), c3)
            elif k < FPS:
                self.__draw_triangle(screen, (car_right + 60, h // 2), c1)
                self.__draw_triangle(screen, (car_right + 35, h // 2), c3)
                self.__draw_triangle(screen, (car_right + 10, h // 2), c2)
            elif k < FPS * 1.5:
                self.__draw_triangle(screen, (car_right + 60, h // 2), c3)
                self.__draw_triangle(screen, (car_right + 35, h // 2), c2)
                self.__draw_triangle(screen, (car_right + 10, h // 2), c1)
            else:
                self.__draw_triangle(screen, (car_right + 60, h // 2), c2)
                self.__draw_triangle(screen, (car_right + 35, h // 2), c1)
                self.__draw_triangle(screen, (car_right + 10, h // 2), c1)
        else:
            self.__draw_triangle(screen, (car_right + 10, h // 2), (36, 36, 36))

    @staticmethod
    def __draw_triangle(screen, coord: [int, int], color):
        tx, ty = coord
        pygame.draw.polygon(screen, color, [(tx, ty - 50), (tx + 15, ty - 50), (tx + 30, ty),
                                            (tx + 15, ty + 50), (tx, ty + 50), (tx + 15, ty)])


class TrianglesLeft(Triangles):
    def draw(self, screen, car_left, h, k):
        c1, c2, c3 = (100, 100, 100), (180, 180, 180), (255, 255, 255)
        if self.on:
            if 0 <= k < FPS // 2:
                self.__draw_triangle(screen, (car_left - 60, h // 2), c1)
                self.__draw_triangle(screen, (car_left - 35, h // 2), c1)
                self.__draw_triangle(screen, (car_left - 10, h // 2), c3)
            elif k < FPS:
                self.__draw_triangle(screen, (car_left - 60, h // 2), c1)
                self.__draw_triangle(screen, (car_left - 35, h // 2), c3)
                self.__draw_triangle(screen, (car_left - 10, h // 2), c2)
            elif k < FPS * 1.5:
                self.__draw_triangle(screen, (car_left - 60, h // 2), c3)
                self.__draw_triangle(screen, (car_left - 35, h // 2), c2)
                self.__draw_triangle(screen, (car_left - 10, h // 2), c1)
            else:
                self.__draw_triangle(screen, (car_left - 60, h // 2), c2)
                self.__draw_triangle(screen, (car_left - 35, h // 2), c1)
                self.__draw_triangle(screen, (car_left - 10, h // 2), c1)
        else:
            self.__draw_triangle(screen, (car_left - 10, h // 2), (36, 36, 36))

    @staticmethod
    def __draw_triangle(screen, coord: [int, int], color):
        tx, ty = coord
        pygame.draw.polygon(screen, color, [(tx, ty - 50), (tx - 15, ty - 50), (tx - 30, ty),
                                            (tx - 15, ty + 50), (tx, ty + 50), (tx - 15, ty)])


class Menu:
    def __init__(self):
        self.car_main_image = CarMainImage()
        self.car_im = Group()
        self.car_im.add(self.car_main_image)
        self.up = TrianglesUp()
        self.down = TrianglesDown()
        self.right = TrianglesRight()
        self.left = TrianglesLeft()
        self.k = 0
        self.command = ''
        self.conn = True

    def update_command(self, command):
        self.command = command

    def update_connect_status(self, status: bool):
        self.conn = status

    def draw(self, screen, w, h):
        d_on = True
        if 'F' in self.command:
            self.up.switch_on()
            self.down.switch_off()
        elif 'B' in self.command:
            self.up.switch_off()
            self.down.switch_on()
        else:
            self.up.switch_off()
            self.down.switch_off()
            d_on = False

        s_on = True
        if 'r' in self.command:
            self.right.switch_on()
            self.left.switch_off()
        elif 'l' in self.command:
            self.right.switch_off()
            self.left.switch_on()
        else:
            self.right.switch_off()
            self.left.switch_off()

        screen.blit(label, (24, 24))
        self.car_main_image.update_position(w, h)
        self.car_im.draw(screen)
        self.up.draw(screen, w, self.car_main_image.get_top(), self.k)
        self.down.draw(screen, w, self.car_main_image.get_bottom(), self.k)
        self.right.draw(screen, self.car_main_image.get_right(), h, self.k)
        self.left.draw(screen, self.car_main_image.get_left(), h, self.k)
        self.k += 1
        if self.k == FPS * 2 or (not d_on and not s_on):
            self.k = 0
