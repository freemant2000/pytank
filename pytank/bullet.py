from PySide6.QtWidgets import QGraphicsScene, QGraphicsEllipseItem
from PySide6.QtGui import QBrush, QColor
from asyncio import create_task, sleep
from pytank.scene_utils import get_xy_proj

class Bullet(QGraphicsEllipseItem):
    diameter=4
    step=4
    def __init__(self, gs: QGraphicsScene, x: int, y: int, heading: int, energy: int=1):
        d=Bullet.diameter*energy
        super().__init__(-d//2, -d//2, d, d)
        self.dx, self.dy=get_xy_proj(Bullet.step, heading)
        self.energy=energy
        self.gs=gs
        self.setBrush(QBrush(QColor("black")))
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
