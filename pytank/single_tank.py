from pytank.game import start_game
from pytank.tank import Tank
from PySide6.QtWidgets import QGraphicsScene

the_tank: Tank = None

class TheTank(Tank):
    def __init__(self, gs: QGraphicsScene, x: int, y: int):
        import __main__
        self.mod=vars(__main__)
        super().__init__(gs, x, y)
    async def on_ready(self):
        await self.call_async_handler("on_ready")
    async def call_async_handler(self, fn):
        handler=self.mod.get(fn)
        if handler:
            await handler()

def start():
    def on_ready(game):
        global the_tank
        the_tank=TheTank(game.gs, 200, 300)
    start_game(on_ready)

async def move(d: int):
    await the_tank.move(d)

async def turn(d: int):
    await the_tank.turn(d)

async def turn_gun(d: int):
    await the_tank.turn_gun(d)

def fire():
    the_tank.fire()