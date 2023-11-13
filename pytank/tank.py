from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem
from asyncio import create_task, sleep, get_event_loop
from bullet import Bullet

class Tank(QGraphicsRectItem):
    def __init__(self, gs: QGraphicsScene, x, y):
        super().__init__(0, 0, 50, 70)
        self.gs=gs
        self.moving=False
        self.setPos(x, y)
        self.gs.addItem(self)
        create_task(self.on_ready())
        create_task(self.update())

    async def on_ready(self):
        await self.move(200)
        Bullet(self.gs, self.x(), self.y())
        
    async def update(self):
        while True:
            await sleep(0.1)
            await self.on_update()
    async def on_update(self):
        pass
    async def move(self, d):
        for e in range(d//4):
            await sleep(0.1)
            self.setX(self.x()+4)
