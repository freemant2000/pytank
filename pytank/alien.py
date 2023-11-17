from asyncio import create_task, sleep
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class Alien(QGraphicsPixmapItem):
    w=40
    h=30
    center_to_top=0.4*h
    center_h=h-center_to_top
    step=4
    def __init__(self, gs: QGraphicsScene, x: int, y: int, dx: int=0, dy: int=0):
        pm=QPixmap("pytank/alien.png")
        pm_body=pm.scaled(Alien.w, Alien.h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        super().__init__(pm_body)
        self.setOffset(-Alien.w//2, -Alien.center_to_top)
        self.setPos(x, y)
        self.gs=gs
        self.gs.addItem(self)
        self.dx=dx
        self.dy=dy
        create_task(self.update())

    async def update(self):
        while True:
            await sleep(0.1)
            self.setPos(self.x()+self.dx, self.y()+self.dy)
