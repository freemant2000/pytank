from PySide6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from asyncio import create_task, sleep, get_event_loop

class Bullet(QGraphicsEllipseItem):
    def __init__(self, gs: QGraphicsScene, x, y):
        super().__init__(0, 0, 4, 4)
        self.gs=gs
        self.gs.addItem(self)
        self.setPos(x, y)
        create_task(self.update())

    async def update(self):
        while True:
            await sleep(0.1)
            self.setY(self.y()-4)
            if self.y()<0:
                self.gs.removeItem(self)
                break
