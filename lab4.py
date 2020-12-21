class entity:
    name = 'entity'    
    level = 1
    mana_equiv = 10 * level
    regen_mana = mana_equiv / 4
    life_equiv = 10 * level
    mana = mana_equiv
    life = life_equiv
    regen_life = life_equiv / 5
    position = 0
    damage = 2 * level
    status = 'Alive'


    def get_pos(self):
        return self.position


    def get_mana(self):
        return self.mana


    def get_life(self):
        return self.life


    def get_name(self):
        return self.name


    def move(self, direct):
        self.position += direct
        if self.mana + self.regen_mana <= self.mana_equiv:
            self.mana += self.regen_mana
        else:
            self.mana = self.mana_equiv
        if self.life + self.regen_life <= self.life_equiv:
            self.life += self.regen_life
        else:
            self.life = self.life_equiv

    def  heal(self, mana):
        if self.mana - mana >= 0:
            self.mana -= mana
        else:
            mana = self.mana
            self.mana = 0
        if self.life + mana <= self.life_equiv:
            self.life += mana
        else:
            self.life = self.life_equiv


    def attack(self, mob, mana = 0):
        if mob.status == 'Alive':
            mob.life -= self.damage + mana
            mob.check()


    def check(self):
        if self.life<=0:
            self.status='Dead'


class Player(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_equiv = 15 * level
        self.regen_mana = self.mana_equiv / 4
        self.life_equiv = 15 * level
        self.mana = self.mana_equiv
        self.life = self.life_equiv
        self.regen_life = self.life_equiv / 4
        self.damage = 3 * level


class Mage(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_equiv = 30 * level
        self.regen_mana = self.mana_equiv / 2
        self.life_equiv = 10 * level
        self.mana = self.mana_equiv
        self.life = self.life_equiv
        self.regen_life = self.life_equiv / 5
        self.damage = 2 * level


class Warrior(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_equiv = 10 * level
        self.regen_mana = self.mana_equiv / 5
        self.life_equiv = 30 * level
        self.mana = self.mana_equiv
        self.life = self.life_equiv
        self.regen_life = self.life_equiv / 2
        self.damage = 4 * level

        

class Mob(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_equiv = 0
        self.damage = 6 * level
        self.life_equiv = 10 * level
        self.life = self.life_equiv
        self.regen_life = self.life_equiv/5
