from player import Player
import vaisseau
from collections import OrderedDict


def play():
    print("Echappez vous du vaisseau!")
    vaisseau.parse_ship_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        position = vaisseau.tile_at(player.x, player.y)
        print(position.intro_text())
        position.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(position, player)


def get_available_actions(position, player):
    actions = OrderedDict()
    print("Chosissez une action : ")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Afficher l'inventaire")
    if isinstance(position, vaisseau.ViewMapTile):
        action_adder(actions, "p", position.print_map, "Plan du vaisseau")
    if isinstance(position, vaisseau.SuppliesTile) and position.inventory:
        action_adder(actions, "s", player.add_supplies, "Ajouter des choses")
    elif isinstance(position, vaisseau.EnemyTile) and position.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attaquer")
        action_adder(actions, "e", player.protect, "Protection")
    else:
        if vaisseau.tile_at(position.x, position.y - 1):
            action_adder(actions, "z", player.move_forward, "Devant")
        if vaisseau.tile_at(position.x, position.y + 1):
            action_adder(actions, "s", player.move_aftward, "Derriere")
        if vaisseau.tile_at(position.x - 1, position.y):
            action_adder(actions, "q", player.move_port, "Babord")
        if vaisseau.tile_at(position.x + 1, position.y):
            action_adder(actions, "d", player.move_starboard,"Tribord")
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "soigner")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))


def choose_action(position, player):
    action = None
    while not action:
        available_actions = get_available_actions(position, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("action invalide!")


def move_player(actions, player, position):
    if vaisseau.tile_at(position.x, position.y - 1):
        return action_adder(actions, "z", player.move_forward, "devant")
    if vaisseau.tile_at(position.x, position.y + 1):
        return action_adder(actions, "s", player.move_aftward, "derriere")
    if vaisseau.tile_at(position.x - 1, position.y):
        return action_adder(actions, "q", player.move_port, "babord")
    if vaisseau.tile_at(position.x + 1, position.y):
        return action_adder(actions, "d", player.move_starboard,"tribord")


play()
