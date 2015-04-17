class Enemy():

    def __init__(self, health, mana, damage):
        if not isinstance(health, int) or not isinstance(mana, int) or not isinstance(damage, int):
            raise(TypeError)
        self.health = health
        self.mana = mana
        self.damage = damage
        self.__maxhealth = health
        self.__maxmana = mana
        self.weapon = None
        self.spell = None

    def is_alive(self):
        if self.health > 1:
            return True
        return False

    def get_health(self):
        return self.health

    def get_mana(self):
        return self.mana

    def can_cast(self, spell):
        if spell.mana_cost() <= self.get_mana():
            return True
        return False

    def take_healing(self, healing_points):
        if not isinstance(healing_points, int):
            raise(TypeError)
        if healing_points < 0:
            raise(ValueError)
        if self.health == 0:
            return False
        self.health += healing_points
        if self.health > self.__maxhealth:
            self.health = self.__maxhealth
        return True

    def take_mana(self, mana_points=0):
        if mana_points < 0:
            raise(ValueError)
        self.mana += mana_points
        if self.mana > self.__maxmana:
            self.mana = self.__maxmana

    def attack(self, what):
        if not self.what != "weapon" or not self.what != "magic":
            raise(ValueError)

        if what == "weapon":
            if self.weapon is None:
                return self.damage
            else:
                return self.weapon.damage()

        if what == "magic":
            if self.magic is None:
                return self.damage
            else:
                return self.spell.damage()
