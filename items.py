class Weapon():
    def __init__(self):
        raise NotImplementedError("Ne créez pas d’objets d’armes bruts")

    def __str__(self):
        return "{} (+ {} Dégats)".format(self.name, self.damage)


class Blaster(Weapon):
    def __init__(self):
        self.name = "Pistolet laser"
        self.description = """
                            Un pistolet à rayons pour éliminer les obstacles et attaquer
                            Ennemis
                            """
        self.damage = 5


class Knife(Weapon):
    def __init__(self):
        self.name = "Couteau de poche"
        self.description = """
                            Un couteau avec une lame qui peut rentrer
                            dans la poche lorsque la lame est
                            rentrée .
                           """
        self.damage = 2


class Consumable():
    def __init__(self):
        raise NotImplementedError("Ne créez pas d’objets consommables bruts.")

    def __str__(self):
        return "{} (+ {} points de vie)".format(self.name, self.healing_value)


class Water(Consumable):
    def __init__(self):
        self.name = "Eau"
        self.healing_value = 10


class OxygenTank(Consumable):
    def __init__(self):
        self.name = "Barril d'Oxygene"
        self.healing_value = 20


class FirstAid(Consumable):
    def __init__(self):
        self.name = "Kit de soins"
        self.healing_value = 50


class Protection():
    def __init__(self):
        raise NotImplementedError("Ne créez pas d’objets de protection bruts.")

    def __str__(self):
        return "{} (- {} Dégats)".format(self.name, self.protect_value)


class SpaceSuit(Protection):
    def __init__(self):
        self.name = "Combinaison d'astronaute"
        self.protect_value = 50


class Shelter(Protection):
    def __init__(self):
        self.name = "Bunker de poche"
        self.protect_value = 100


class CrustyBread(Consumable, Protection):
    def __init__(self):
        self.name = "Pain rassis"
        self.healing_value = 5
        self.protect_value = 0
