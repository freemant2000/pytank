from PySide6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem, QGraphicsRectItem
from asyncio import create_task, sleep
from scene_utils import get_xy_proj

class Bullet(QGraphicsEllipseItem):
    diameter=4
    step=4
    def __init__(self, gs: QGraphicsScene, x: int, y: int, heading: int):
        super().__init__(-Bullet.diameter//2, -Bullet.diameter//2, Bullet.diameter, Bullet.diameter)
        self.dx, self.dy=get_xy_proj(Bullet.step, heading)
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
