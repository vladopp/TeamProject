class Weapon:

	def __init__(self, weapon_name, damage):
		if not isinstance(weapon_name, str) or not isinstance(damage, int):
			raise TypeError
		self.weapon_name = weapon_name
		self.damage = damage
