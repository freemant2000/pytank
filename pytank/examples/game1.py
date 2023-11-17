from pytank.game import start_game
from pytank.tank import Tank
from pytank.alien import Alien

async def on_tank_ready(tank: Tank):
    tank.fire()

def on_game_ready(game):
    Tank(game.gs, 250, 380, on_tank_ready)
    Alien(game.gs, 20, 40, 3, 0)
    Alien(game.gs, 400, 80, 0, 4)

start_game(on_game_ready)