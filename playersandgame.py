imboard = [['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', ' ', '*', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', ' ', '*', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
           ['*', ' ', '_', '_', '_', '_', '_', '*', '*', '*', '_', '_', '_', '_', '_', ' ', '*'],
           ['*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', '*', ' ', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', '_', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', ' ', '*', '*', ' ', '*', ' ', '_', ' ', '*', '*', ' ', '*', ' ', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', ' ', ' ', ' ', '*', '*', '*', '*', '*', '*', '*'],
           ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']]

order = ['b', 'r', 'g', 'y']
colorresppos = {'b': (7, 14), 'r': (14, 9), 'g': (9, 2), 'y': (2, 7)}
colortext = {'b': 'Синие', 'r': 'Красные', 'g': 'Зеленые', 'y': 'Желтые'}
whoseturn = 3


class Piece:
    def __init__(self, startpos, color):
        self.y, self.x = startpos
        self.revspot = startpos
        self.color = color
        self.active = False
        self.gone_through = 0
        # self.limit = 58

    def activate(self):
        self.active = True
        self.y, self.x = colorresppos[self.color]
        print('done!' + self.color)

    def move(self, tiles):
        if self.active is False and tiles < 6:
            return None
        if self.active is False and tiles == 6:
            return self.activate()
        for i in range(tiles):
            if self.x - 8 >= 0:
                if imboard[self.y + 1][self.x] == ' ':
                    self.y += 1
                else:
                    if self.y - 8 > 0:
                        if imboard[self.y][self.x - 1] == ' ':
                            self.x -= 1
                    if self.y - 8 < 0:
                        if imboard[self.y][self.x + 1] == ' ':
                            self.x += 1
            if self.x - 8 < 0:
                if imboard[self.y - 1][self.x] == ' ':
                    self.y -= 1
                else:
                    if self.y - 8 > 0:
                        if imboard[self.y][self.x - 1] == ' ':
                            self.x -= 1
                    if self.y - 8 < 0:
                        if imboard[self.y][self.x + 1] == ' ':
                            self.x += 1
            self.gone_through += 1

    def getpar(self):
        return self.y, self.x, self.color

    def getcolor(self):
        return self.color

    def getcoords(self):
        return self.y, self.x


players = [Piece((11, 2), 'g'), Piece((11, 5), 'g'), Piece((14, 2), 'g'), Piece((14, 5), 'g'),
           Piece((2, 2), 'y'), Piece((2, 5), 'y'), Piece((5, 2), 'y'), Piece((5, 5), 'y'),
           Piece((2, 11), 'b'), Piece((2, 14), 'b'), Piece((5, 11), 'b'), Piece((5, 14), 'b'),
           Piece((11, 11), 'r'), Piece((11, 14), 'r'), Piece((14, 11), 'r'), Piece((14, 14), 'r')]
