class Enemy():
    def __init__(self):
        raise NotImplementedError("Ne créez pas d’objets ennemis bruts")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Robot(Enemy):
    def __init__(self):
        self.name = "Robot"
        self.hp = 30
        self.damage = 10


class Soldier(Enemy):
    def __init__(self):
        self.name = "Soldat Ennemi"
        self.hp = 10
        self.damage = 2


class Drone(Enemy):
    def __init__(self):
        self.name = "Drone ennemi"
        self.hp = 5
        self.damage = 1


class Troll(Enemy):
    def __init__(self):
        self.name = "Troll de l'espace"
        self.hp = 80
        self.damage = 15


class SpaceDucks(Enemy):
    def __init__(self):
        self.name = "Nuée de canard spatiaux bleus"
        self.description = "Suivent les miettes de pain rouge rassis spatial."
        self.hp = 100
        self.damage = 3
