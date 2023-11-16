from pytank.single_tank import *

async def on_ready():
    await turn(30)
    await move(100)
    fire()

start()