from .BaseClass import *

class VecFromCoords(Vector_):
    '''
    Get a Vector from Double <X> and Double <Y>
    '''
    def __init__(self, x, y):
        self.name = b'vec.fromCoords'
        self.x = checkType(x, float, Double_)
        self.y = checkType(y, float, Double_)

    def asBytes(self) -> bytes:
        return (bytes([len(self.name)])
                + self.name
                + self.x.asBytes()
                + self.y.asBytes())


class getMousePos(Vector_):
    '''
    Get current mouse position as a Vector
    '''
    def __init__(self):
        self.name = b'mouse.position'
    def asBytes(self) -> bytes:
        return bytes([len(self.name)]) + self.name