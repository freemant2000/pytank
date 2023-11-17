from asyncio import create_task, sleep
from typing import Awaitable
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsTextItem
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from pytank.bullet import Bullet
from pytank.scene_utils import get_xy_proj, select_items

class Tank(QGraphicsPixmapItem):
    w=40
    h=40
    center_h=0.4*h
    center_to_top=h-center_h
    step=4
    step_degree=3
    def __init__(self, gs: QGraphicsScene, name: str, x: int, y: int, on_ready: Awaitable):
        self.name=name
        self.energy=20
        self.pending_dist=0
        self.pending_angle=0
        self.pending_gun_angle=0
        self.heading=0
        self.gun_heading=0
        pm=QPixmap("pytank/tank_body.png")
        pm_body=pm.scaled(Tank.w, Tank.h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        super().__init__(pm_body)
        self.setOffset(-Tank.w//2, -Tank.center_to_top)
        self.setPos(x, y)
        self.gs=gs
        self.gs.addItem(self)
        pm=QPixmap("pytank/tank_gun.png")
        pm_gun=pm.scaled(Tank.w, Tank.h, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.gun=QGraphicsPixmapItem(pm_gun)
        self.gun.setOffset(-Tank.w//2, -Tank.center_to_top)
        self.gun.setPos(x, y)
        self.gs.addItem(self.gun)
        self.info=QGraphicsTextItem()
        font=self.info.font()
        font.setPointSize(8)
        self.info.setFont(font)
        self.info.setPos(x-Tank.w//2, y+Tank.center_h)
        self.info.setTextWidth(Tank.w)
        self.update_info()
        self.gs.addItem(self.info)
        create_task(on_ready(self))
        create_task(self.update())
    
    def update_info(self):
        self.info.setHtml(f"<center>{self.name}<br>{self.energy}</center>")
    def set_heading(self, h: int):
        self.heading=h
        self.setRotation(self.heading)

    def set_gun_heading(self, h: int):
        self.gun_heading=h
        self.gun.setRotation(self.gun_heading)

    async def update(self):
        while True:
            await sleep(0.1)
            if self.pending_dist!=0:
                sign=1 if self.pending_dist>0 else -1
                s=min(abs(self.pending_dist), Tank.step)
                dx, dy=get_xy_proj(s, self.heading)
                self.setPos(self.x()+dx, self.y()+dy)
                self.gun.setPos(self.gun.x()+dx, self.gun.y()+dy)
                self.info.setPos(self.info.x()+dx, self.info.y()+dy)
                self.pending_dist-=sign*s
            if self.pending_angle!=0:
                sign=1 if self.pending_angle>0 else -1
                s=min(abs(self.pending_angle), Tank.step_degree)
                self.set_heading(self.heading+sign*s)
                self.pending_angle-=sign*s
            if self.pending_gun_angle!=0:
                sign=1 if self.pending_gun_angle>0 else -1
                s=min(abs(self.pending_gun_angle), Tank.step_degree)
                self.set_gun_heading(self.gun_heading+sign*s)
                self.pending_gun_angle-=sign*s

    async def move(self, d: int):
        self.pending_dist=d
        while self.pending_dist!=0:
            await sleep(0)

    async def turn(self, angle: int):
        self.pending_angle=angle
        while self.pending_angle!=0:
            await sleep(0)

    async def turn_gun(self, angle: int):
        self.pending_gun_angle=angle
        while self.pending_gun_angle!=0:
            await sleep(0)
    
    def fire(self, energy: int=1):
        if energy<1 or energy>3:
            print(f"invalid energy {energy}")
            return
        if energy>self.energy:
            print("out of energy")
            return
        self.energy-=energy
        self.update_info()
        dx, dy=get_xy_proj(Tank.center_to_top, self.gun_heading)
        Bullet(self.gs, self.x()+dx, self.y()+dy, self.gun_heading, energy)
