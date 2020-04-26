import random
import enemis
import sys
import items


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.inventory

    def intro_text(self):
        raise NotImplementedError("Sous classe crée en substitue")

    def modify_player(self, player):
        pass


class StartTile(MapTile):

    def intro_text(self):
        return """
        Vous vous réveillez dans un vaisseau spatial , une alerte rouge sonne ,
        il y a marqué à coté de vous sur un écran : ENNEMI INCONNU A BORD .
        Vous avez besoin d’une nacelle d’évacuation pour voyager en toute sécurité sur la planète voisine.
        Vous avez besoin de d'eau,de nourriture pour le voyage et la survie sur la planète.
        Vous pouvez aller dans quatre directions : vers l’avant, vers l’arrière, babord , tribord
        Vous avez quatre actions : Inventaire, attaquer, soigner, proteger
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        Il n’y a pas de d'eau , de nourriture ou de nacelle d’évasion ici.
        """


class ViewMapTile(MapTile):
    def intro_text(self):
        return """
        Vous voyez un plan sur le mur.
        """

    def print_map(self):
        self.ship_printable = """
                            devant
                |          |Cuisine |            |
        babord  |          |        |Vous êtes IC|  Tribord
                |          | Start  |            |
                |Evacuation|        |            |
                            arrière
        """
        print(self.ship_printable)


class SuppliesTile(MapTile):
    def __init__(self, x, y):
        self.i = 0
        self.name = "Eau,Nourriture;Oxygene"
        self.inventory = [items.Blaster(), items.OxygenTank(),
                          items.SpaceSuit(), items.FirstAid(),
                          items.CrustyBread(), items.Water(), items.Shelter()]

        super().__init__(x, y)

    def intro_text(self):
        self.start_supplies = """
        Vous voyez une grande caisse métallique. Vous l’ouvrez.
        C’est un approvisionnement ! Vous avez trouvé une trousse de premiers soins, un réservoir d’oxygène,
        un costume spatial, de la nourriture, de l’eau, un couteau de poche et un pistolet à rayons.
        """
        self.no_supplies = "Il n'y a rien ici"
        supply_text = [self.start_supplies, self.no_supplies]
        if self.i == 0:
            self.i += 1
            return supply_text[0]
        else:
            return supply_text[1]

    def suppy(self):
        for i, item in enumerate(self.inventory, 1):
            print("Vous avez ajoutez les items suivant à votre inventaire!")
            print("{}. {}.".format(i, item.name))
        self.add_inventory()

    def add_inventory(self, current_inventory):
        for item in self.inventory:
            current_inventory.append(item)
        self.inventory = []


class EscapePod(MapTile):
    def modify_player(self, player):
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        Tu as trouvé la navette d’évacuation ! Vous ouvrez la porte et entrez dans la navette.
        La navette d’évacuation se désengage lentement du navire et se rend à
        la planète voisine. Vous êtes en sécurité, pour l’instant...
        """


class EnemyTile(MapTile):
    def __init__(self, x, y):
        self.j = 0
        self.k = 0
        r = random.random()
        if r < 0.30:
            self.enemy = enemis.Drone()
            alive_start = """
            Vous entendez un bruit bourdonnant. Vous vous retournez et voyez un drone ennemi
            avec ses armes dirigées vers vous
            """
            alive_attack = "Le drone attaque."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            Le bourdonnement s’arrête, le drone explose et tombe au sol
            """
            dead_return = "Un drone désactivé est au sol."
            self.dead_text = [dead_start, dead_return]
        elif r < 0.60 and r >= 0.30:
            self.enemy = enemis.Soldier()
            alive_start = """
            Un soldat ennemi dans une combinaison spatiale surgit du coin du couloir
            et commence à tirer.
            """
            alive_attack = "le soldat attaque."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            Le soldat laisse tomber son arme et s’effondre au sol.
            """
            dead_return = "Un soldat mort est au sol."
            self.dead_text = [dead_start, dead_return]
        elif r < 0.75 and r >= 0.60:
            self.enemy = enemis.Robot()
            alive_start = """
            Votre œil remarque la lueur du métal dans la lumière vacillante. Un
            grand œil rouge se tourne vers vous , scanne votre corps, s’arrête, puis ouvre le feu.
            """
            alive_attack = "Le robot attaque."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            Le grand œil rouge devient faible à mesure que les étincelles volent autour du robot.
            """
            dead_return = "Un robot désactivé est au sol."
            self.dead_text = [dead_start, dead_return]
        elif r < 0.90 and r >= 0.75:
            self.enemy = enemis.Troll()
            alive_start = """
            Une grande omre se trouve devant vous .Un grand troll de l’espace casse le vaisseau . 
            Il s’arrête soudainement et vous remarque en essayant de vous cacher. Il s’approche
            rapidement et se balance à vous avec ses grands poings.
            """
            alive_attack = "Le troll attaque."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            Le troll qui soffre de ses blessures mortelles , tombe avec un bruit sourd fort
            qui secoue tout le navire
            """
            dead_return = "Un troll mort est au sol."
            self.dead_text = [dead_start, dead_return]
        else:
            self.enemy = enemis.SpaceDucks()
            alive_start = """
            Vous voyez des canard spatiaux bleu .
            Ils ont l'air de créer un nid. 
            Ils semblent se diriger vers vous
            et ne semblent pas très amicaux ...
            """
            alive_attack = "Les êtres attaquent."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            Le dernier canard spatial bleu explose dans un nuage de plumes. Vous pataugez à travers
            grandes étendues de plumes bleues et essayer de nettoyer le navire
            l’équipement et le désalog des conduits d’air bloqués.
            """
            dead_return = "Les canards morts et une étendue de plumes bleues se trouvent au sol."
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            if self.j == 0:
                self.j += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        else:
            if self.k == 0:
                self.k += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        if self.enemy.is_alive():
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("Le {} vous a fait {} dégats. Vous avez {} Points de vie restant".
                      format(self.enemy.name,
                             self.enemy.damage,
                             player.hp))
            elif player.hp <= self.enemy.damage:
                print("Le {} vous a causé des blessures mortelles. Vous en mourrez.".
                      format(self.enemy.name))
                sys.exit()

ship_map = []


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return ship_map[y][x]
    except IndexError:
        return None


ship_dsl = """
|ET|CU|ET|
|RT|RT|MP|
|ET|ST|ET|
|EP|RT|RT|
"""


def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|EP|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


tile_type_dict = {"EP": EscapePod,
                  "ST": StartTile,
                  "CU": SuppliesTile,
                  "ET": EnemyTile,
                  "RT": BoringTile,
                  "MP": ViewMapTile,
                  "  ": None}
start_tile_location = None


def parse_ship_dsl():
    if not is_dsl_valid(ship_dsl):
        raise SyntaxError("DSL est invalide!")

    dsl_lines = ship_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cells in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cells]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)
        ship_map.append(row)
