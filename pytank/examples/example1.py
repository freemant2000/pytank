from pytank.single_tank import *

async def on_ready():
    fire()
    await turn(30)
    await move(100)
    fire(3)

start()