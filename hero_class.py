class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):
        if not isinstance(name, str) or not isinstance(title, str) or not isinstance(health, int) or not isinstance(mana, int) or not isinstance(mana_regeneration_rate, int):
            raise TypeError
        self.__name = name
        self.__title = title
        self.health = health
        self.mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        self.__maxhealth = health
        self.__maxmana = mana
        self.weapon = None
        self.spell = None

    def known_as(self):
        return "{} the {}".format(self.__name, self.__title)

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

    def take_damage(self, damage_points):
        if not isinstance(damage_points, int) and not isinstance(damage_points, float):
            raise(TypeError)
        if damage_points < 0:
            raise(ValueError)
        if damage_points > self.health:
            self.health = 0
        else:
            self.health -= damage_points

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
        mana_points += self.__mana_regeneration_rate
        self.mana += mana_points
        if self.mana > self.__maxmana:
            self.mana = self.__maxmana

    def equip(self, weapon):
        self.weapon = weapon

    def learn(self, spell):
        self.spell = spell

    def attack(self, what):
        if not self.what != "weapon" or not self.what != "magic":
            raise(ValueError)

        if what == "weapon":
            if self.weapon is None:
                return 0
            else:
                return self.weapon.damage()

        if what == "magic":
            if self.magic is None:
                return 0
            else:
                return self.spell.damage()
