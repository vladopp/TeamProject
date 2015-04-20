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

    def treasure(self):
        pass

    def move_hero(self, direction):
        if direction == "left":
            if self.map[self.heroposX-1][self.heroposY] == '#':
                return False
            else:
                if self.map[self.heroposX-1][self.heroposY] == '.':
                    self.map[self.heroposX-1][self.heroposY] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposX -= 1
                    self.hero.take_mana()
                    return True

                elif self.map[self.heroposX][self.heroposY-1] == 'T':
                    self.map[self.heroposX][self.heroposY-1] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposY -= 1
                    self.treasure()
                    self.hero.take_mana()
                    return True

        elif direction == "right":
            if self.map[self.heroposX+1][self.heroposY] == '#':
                return False
            else:
                if self.map[self.heroposX+1][self.heroposY] == '.':
                    self.map[self.heroposX+1][self.heroposY] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposX += 1
                    self.hero.take_mana()
                    return True

                elif self.map[self.heroposX+1][self.heroposY] == 'T':
                    self.map[self.heroposX+1][self.heroposY] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposX += 1
                    self.treasure()
                    self.hero.take_mana()
                    return True

        elif direction == "up":
            if self.map[self.heroposX][self.heroposY-1] == '#':
                return False
            else:
                if self.map[self.heroposX][self.heroposY-1] == '.':
                    self.map[self.heroposX][self.heroposY-1] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposY -= 1
                    self.hero.take_mana()
                    return True

                elif self.map[self.heroposX][self.heroposY-1] == 'T':
                    self.map[self.heroposX][self.heroposY-1] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposY -= 1
                    self.treasure()
                    self.hero.take_mana()
                    return True

        elif direction == "down":
            if self.map[self.heroposX][self.heroposY+1] == '#':
                return False
            else:
                if self.map[self.heroposX][self.heroposY+1] == '.':
                    self.map[self.heroposX][self.heroposY+1] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposY += 1
                    self.hero.take_mana()
                    return True

                elif self.map[self.heroposX][self.heroposY+1] == 'T':
                    self.map[self.heroposX][self.heroposY+1] = 'H'
                    self.map[self.heroposX][self.heroposY] = '.'
                    self.heroposY += 1
                    self.treasure()
                    self.hero.take_mana()
                    return True

    def hero_attack(self, by):
        pass
