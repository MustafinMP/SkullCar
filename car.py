class Car:
    def __init__(self):
        self.__right = False
        self.__left = False
        self.__up = False
        self.__down = False
        self.__last = [self.__up, self.__down, self.__left, self.__right]

    def set_right(self, value: bool):
        self.__right = value

    def set_left(self, value: bool):
        self.__left = value

    def set_up(self, value: bool):
        self.__up = value

    def set_down(self, value: bool):
        self.__down = value

    def drive_key(self):
        if self.__up and self.__down:
            return 'S'
        elif self.__up:
            return 'F'
        elif self.__down:
            return 'B'
        return 'D'

    def steal_key(self):
        if self.__right == self.__left:
            return 'f'
        if self.__right:
            return 'r'
        return 'l'

    def changed(self):
        if self.__last == [self.__up, self.__down, self.__left, self.__right]:
            return False
        self.__last = [self.__up, self.__down, self.__left, self.__right]
        return True
