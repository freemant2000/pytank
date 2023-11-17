from pytank.game import start_game
from pytank.tank import Tank

the_tank: Tank = None

async def on_tank_ready(tank: Tank):
    import __main__
    mod=vars(__main__)
    async def call_async_handler(fn):
        handler=mod.get(fn)
        if handler:
            await handler()
    await call_async_handler("on_ready")

def start():
    def on_game_ready(game):
        global the_tank
        the_tank=Tank(game.gs, "T1", 250, 330, on_tank_ready)
    start_game(on_game_ready)

async def move(d: int):
    await the_tank.move(d)

async def turn(d: int):
    await the_tank.turn(d)

async def turn_gun(d: int):
    await the_tank.turn_gun(d)

def fire():
    the_tank.fire()