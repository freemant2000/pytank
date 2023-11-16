import math
import typing
from PySide6.QtWidgets import QGraphicsScene
from PySide6.QtGui import QPolygon
from PySide6.QtCore import Qt, QPoint

def get_xy_proj(dist, heading):
    heading_r=math.radians(heading)
    dx=math.sin(heading_r)*dist
    dy=-math.cos(heading_r)*dist
    return (dx, dy)

def select_items(qs: QGraphicsScene, pts: typing.Sequence[typing.Tuple]):
    p=QPolygon([QPoint(x, y) for (x, y) in pts])
    items=qs.items(p, Qt.ItemSelectionMode.IntersectsItemBoundingRect)
    print(items)
    return items