class Monster:
    def __init__(self):
        self.hp = 10  # have to use self to set the instance.


class Weapon:

    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):  # attack() is what's called externally. Outside the class definition.
        self.set_durability()  # an internal method. Not able to be called on externally.
        return self.damage

    def set_durability(self):
        self.durability -= 1
        if self.durability < 0:
            self.durability = 0
            self.damage = 0


class Sword(Weapon):

    def __init__(self):
        self.damage = 3
        self.durability = 2


class UnbreakableSword(Sword):
    def set_durability(self):
        pass

orc = Monster()
bad_sword = Weapon()
ok_sword = Sword()
awesome_sword = UnbreakableSword()

print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
orc.hp -= awesome_sword.attack()
print(orc.hp)
