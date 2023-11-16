import asyncio
import qasync
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsRectItem
from qasync import QApplication
from tank import Tank

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.gs=QGraphicsScene()
        self.gv=QGraphicsView(self.gs)
        self.gv.setFixedWidth(600)
        self.gv.setFixedHeight(400)
        self.gv.setSceneRect(0, 0, 600-2, 400-2)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.gv)
        self.layout().update()
        Tank(self.gs, 200, 300)
    
async def main():
    def leave():
        if not future.done():
            future.set_result(0)
    future=asyncio.Future()
    app=QApplication.instance()
    app.aboutToQuit.connect(leave)
    main=MainWindow()
    main.show()
    await future

qasync.run(main())
