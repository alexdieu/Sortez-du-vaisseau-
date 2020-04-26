import items
import vaisseau


class Player:
    def __init__(self):
        self.inventory = [items.Knife()]
        self.x = vaisseau.start_tile_location[0]
        self.y = vaisseau.start_tile_location[1]
        self.hp = 100
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        print("Inventaire:")
        for item in self.inventory:
            print("* " + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Votre meilleure arme est {}".format(best_weapon))

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_forward(self):
        self.move(dx=0, dy=-1)

    def move_aftward(self):
        self.move(dx=0, dy=1)

    def move_starboard(self):
        self.move(dx=1, dy=0)

    def move_port(self):
        self.move(dx=-1, dy=0)

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        position = vaisseau.tile_at(self.x, self.y)
        enemy = position.enemy
        print("Vous utilisez {} contre {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("Vous avez tué {}".format(enemy.name))
        else:
            print("{} Points de vie est à {}.".format(enemy.name, enemy.hp))

    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]

        if not consumables:
            print("Vous n'avez pas les items requis pour vous soigner!")
            return

        print("Choisissez un item pour vous soigner: ")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_use = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_use.healing_value)
                self.inventory.remove(to_use)
                print("Points de vie actuellement: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Choix Invalide .Réessayer")

    def protect(self):
        """Check and use items for protection"""
        protection = [item for item in self.inventory
                      if isinstance(item, items.Protection)]
        if not protection:
            print("Vous n'avez pas d'items pour vous protéger!")
            return
        position = vaisseau.tile_at(self.x, self.y)
        enemy = position.enemy
        if enemy.name == "Troupeau de canards bleus spatiaux":
            print("La valeur de protection du pain rassis contre les canards est de -100 Dégats")
        print("Choisissez un item pour vous protéger : ")
        for i, item in enumerate(protection, 1):
            print("{}. {}".format(i, item))
        valid = False
        while not valid:
            choice = input("")
            try:
                to_use = protection[int(choice) - 1]
                self.inventory.remove(to_use)
                if enemy.name == "Troupeaux de canard bleus":
                    if to_use.name == "Pain rassis":
                        to_use.protect_value = 100
                else:
                    if to_use.name == "pain rassis":
                        to_use.protect_value = 0

                enemy.damage = enemy.damage - to_use.protect_value
                if enemy.damage > 0:
                    return enemy.damage
                else:
                    enemy.damage = 0
                    return enemy.damage
                print("Dégats potentiels : {}".format(enemy.damage))
                valid = True
            except (ValueError, IndexError):
                print("Choix Invalid .Réessayer.")

    def add_supplies(self):
        position = vaisseau.tile_at(self.x, self.y)
        current_inventory = self.inventory
        position.add_inventory(current_inventory)
