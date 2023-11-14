from PySide6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from asyncio import create_task, sleep, get_event_loop
import math

class Bullet(QGraphicsEllipseItem):
    diameter=4
    step=4
    def __init__(self, gs: QGraphicsScene, x, y, heading):
        super().__init__(0, 0, Bullet.diameter, Bullet.diameter)
        heading_r=math.radians(heading)
        self.dx=math.sin(heading_r)*Bullet.step
        self.dy=-math.cos(heading_r)*Bullet.step
        self.gs=gs
        self.gs.addItem(self)
        self.setPos(x, y)
        create_task(self.update())

    async def update(self):
        while True:
            await sleep(0.1)
            self.setPos(self.x()+self.dx, self.y()+self.dy)
            if self.y()<0 or self.y()>400 or self.x()<0 or self.x()>600:
                self.gs.removeItem(self)
                break
        print("removed")
