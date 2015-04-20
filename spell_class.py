class Spell:

	def __init__(self, spell_name, damage, mana_cost, cast_range):
		if not isinstance(spell_name, str) or not isinstance(damage, int) or not isinstance(mana_cost, int) or not isinstance(cast_range, int):
			raise TypeError

		self.spell_name
		self.damage = damage
		self.mana_cost = mana_cost
		self.cast_range = cast_range

	def spell_damage(self, damage_points):
		damage_points = damage
		self.health = self.health - damage
		return self.health
		