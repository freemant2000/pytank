import asyncio
from typing import Callable
import qasync
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView
from qasync import QApplication

class MainWindow(QWidget):
    def __init__(self, on_ready: Callable):
        super().__init__()
        self.gs=QGraphicsScene()
        self.gv=QGraphicsView(self.gs)
        self.gv.setFixedWidth(600)
        self.gv.setFixedHeight(400)
        self.gv.setSceneRect(0, 0, 600-2, 400-2)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.gv)
        self.layout().update()
        on_ready(self)
    
async def main(on_ready: Callable):
    def leave():
        if not future.done():
            future.set_result(0)
    future=asyncio.Future()
    app=QApplication.instance()
    app.aboutToQuit.connect(leave)
    main=MainWindow(on_ready)
    main.show()
    await future

def start_game(on_ready: Callable):
    qasync.run(main(on_ready))
