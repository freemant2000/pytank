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
    step=4
    step_degree=3
    def __init__(self, gs: QGraphicsScene, x: int, y: int):
        pm=QPixmap("pytank/tank.png")
        pm2=pm.scaled(Tank.w, Tank.h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        super().__init__(pm2)
        self.setOffset(-Tank.w//2, -Tank.center_to_top)
        self.gs=gs
        self.pending_dist=0
        self.pending_angle=0
        self.heading=0
        self.setPos(x, y)
        self.gs.addItem(self)
        create_task(self.on_ready())
        create_task(self.update())

    def set_heading(self, h: int):
        self.heading=h
        self.setRotation(self.heading)

    async def on_ready(self):
        await self.turn(30)
        await self.move(200)
        #Bullet(self.gs, self.x(), self.y())
        #await self.turn(30)
        # dx, dy=get_xy_proj(Tank.center_to_top, self.heading)
        # Bullet(self.gs, self.x()+dx, self.y()+dy, self.heading)
        pass
        
    async def update(self):
        while True:
            await sleep(0.1)
            if self.pending_dist!=0:
                sign=1 if self.pending_dist>0 else -1
                s=min(abs(self.pending_dist), Tank.step)
                dx, dy=get_xy_proj(s, self.heading)
                self.setPos(self.x()+dx, self.y()+dy)
                self.pending_dist-=sign*s
            if self.pending_angle!=0:
                sign=1 if self.pending_angle>0 else -1
                s=min(abs(self.pending_angle), Tank.step_degree)
                self.set_heading(self.heading+sign*s)
                self.pending_angle-=sign*s

    async def move(self, d: int):
        self.pending_dist=d
        while self.pending_dist!=0:
            await sleep(0.01)

    async def turn(self, angle: int):
        self.pending_angle=angle
        while self.pending_angle!=0:
            await sleep(0.01)
