from asyncio import create_task, sleep, get_event_loop
from qasync import QApplication
from PySide6.QtWidgets import QGraphicsScene, QGraphicsRectItem
from PySide6.QtCore import QEventLoop
from bullet import Bullet

class Tank(QGraphicsRectItem):
    w=50
    h=70
    center_h=35
    def __init__(self, gs: QGraphicsScene, x, y):
        super().__init__(0, 0, Tank.w, Tank.h)
        self.gs=gs
        self.heading=0
        self.setPos(x, y)
        self.gs.addItem(self)
        create_task(self.on_ready())
        create_task(self.update())

    def set_heading(self, h):
        self.heading=h
        self.setTransformOriginPoint(Tank.w/2, Tank.center_h)
        self.setRotation(self.heading)

    async def on_ready(self):
        #await self.move(200)
        #Bullet(self.gs, self.x(), self.y())
        await self.turn(-30)
        pass
        
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

    async def turn(self, angle):
        step_degree=3
        if angle>0:
            sign=1
        else:
            sign=-1
            angle=-angle
        for e in range(angle//step_degree):
            await sleep(0.1)
            self.set_heading(self.heading+sign*step_degree)
    # def move_wait(self, d):
    #     is_moving=True
    #     async def do_move():
    #         nonlocal is_moving
    #         await self.move(d)
    #         is_moving=False
    #     app=QApplication.instance()
    #     get_event_loop().create_task(do_move())
    #     while is_moving:
    #         app.processEvents(QEventLoop.ProcessEventsFlag.AllEvents, 100)
