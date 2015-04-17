from hero_class import Hero
import os


class Dungeon:
    def __init__(self, filename):
        self.map = []
        self.hero = None
        with open(filename, "r") as f:
            for line in f:
                temp = []
                for char in line:
                    if char != '\n' and char != ' ' and char != '':
                        temp.append(char)
                self.map.append(temp)
        self.heroposX = None
        self.heroposY = None

    def print_map(self):
        for line in self.map:
            print(''.join(line))

    def spawn(self, hero):
        if isinstance(hero, Hero):
            self.hero = hero
        else:
            raise(TypeError)

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self[x][y] == "S":
                    self[x][y] = "H"
                    self.heropoX = x
                    self.heroposY = y
                    return True
        print("Game Over :(")
        os.__exit()

    def move_hero(self, direction):
        if direction == "left":
            if self.heroposX == 0:
                return False
            if self.map[self.heroposX-1][self.heroposY] == '.':
                pass
