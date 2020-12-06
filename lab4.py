class Entity:
    name = 'entity'    
    level = 1
    mana_Equiv = 10 * level
    regen_Mana = mana_Equiv / 4
    life_Equiv = 10 * level
    mana = mana_Equiv
    life = life_Equiv
    regen_Life = life_Equiv / 5
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
        if self.mana + self.regen_Mana <= self.mana_Equiv:
            self.mana += self.regen_Mana
        else:
            self.mana = self.mana_Equiv
        if self.life + self.regen_Life <= self.life_Equiv:
            self.life += self.regen_Life
        else:
            self.life = self.life_Equiv

    def  heal(self, mana):
        if self.mana - mana >= 0:
            self.mana -= mana
        else:
            mana = self.mana
            self.mana = 0
        if self.life+mana <= self.life_Equiv:
            self.life += mana
        else:
            self.life = self.life_Equiv


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
        self.mana_Equiv = 15 * level
        self.regen_Mana = self.mana_Equiv / 4
        self.life_Equiv = 15 * level
        self.mana = self.mana_Equiv
        self.life = self.life_Equiv
        self.regen_Life = self.life_Equiv / 4
        self.damage = 3 * level


class Mage(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_Equiv = 30 * level
        self.regen_Mana = self.mana_Equiv / 2
        self.life_Equiv = 10 * level
        self.mana = self.mana_Equiv
        self.life = self.life_Equiv
        self.regen_Life = self.life_Equiv / 5
        self.damage = 2 * level


class Warrior(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_Equiv = 10 * level
        self.regen_Mana = self.mana_Equiv / 5
        self.life_Equiv = 30 * level
        self.mana = mana_Equiv
        self.life = life_Equiv
        self.regen_Life = life_Equiv / 2
        self.damage = 4 * level

        

class Mob(Entity):
    def __init__(self, name, level):
        super().__init__()
        self.name = name
        self.level = level
        self.mana_Equiv = 0
        self.damage = 6 * level
        self.life_Equiv = 10*level
        self.life = self.life_Equiv
        self.regen_Life = self.life_Equiv/5
