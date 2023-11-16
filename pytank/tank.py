from asyncio import create_task, sleep
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from bullet import Bullet
from scene_utils import get_xy_proj

class Tank(QGraphicsPixmapItem):
    w=40
    h=40
    center_h=0.4*h
    center_to_top=h-center_h
    def __init__(self, gs: QGraphicsScene, x: int, y: int):
        pm=QPixmap("pytank/tank.png")
        pm2=pm.scaled(Tank.w, Tank.h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        super().__init__(pm2)
        self.setOffset(-Tank.w//2, -Tank.center_to_top)
        self.gs=gs
        self.heading=0
        self.setPos(x, y)
        self.gs.addItem(self)
        create_task(self.on_ready())
        create_task(self.update())

    def set_heading(self, h: int):
        self.heading=h
        self.setRotation(self.heading)

    async def on_ready(self):
        #await self.move(200)
        #Bullet(self.gs, self.x(), self.y())
        await self.turn(30)
        dx, dy=get_xy_proj(Tank.center_to_top, self.heading)
        Bullet(self.gs, self.x()+dx, self.y()+dy, self.heading)
        pass
        
    async def update(self):
        while True:
            await sleep(0.1)
            await self.on_update()
    async def on_update(self):
        pass
    async def move(self, d: int):
        for e in range(d//4):
            await sleep(0.1)
            self.setX(self.x()+4)

    async def turn(self, angle: int):
        step_degree=3
        if angle>0:
            sign=1
        else:
            sign=-1
            angle=-angle
        for e in range(angle//step_degree):
            await sleep(0.1)
            self.set_heading(self.heading+sign*step_degree)
