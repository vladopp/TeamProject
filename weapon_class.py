class Weapon:
    def __init__(self, name, damage):
        if not isinstance(name, str):
            raise TypeError("Name must be string")

        if not isinstance(damage, int):
            raise TypeError("Damage must be integer")

        self.name = name
        self.__damage = damage

    def __repr__(self):
        return "{} - {} DMG".format(self.name, self.__damage)

    def get_damage(self):
        return self.__damage
