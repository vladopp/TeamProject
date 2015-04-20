class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        if not isinstance(name, str) or not isinstance(damage, int) or not isinstance(mana_cost, int) or not isinstance(cast_range, int):
            raise TypeError

        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.cast_range = cast_range
