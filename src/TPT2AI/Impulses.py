from .BaseClass import *


class Impulse(Interface):
    '''
    Impulse Base class
    '''

    def __init__(self, name: bytes):
        self.name = name

    def asBytes(self):
        return bytes([len(self.name)]) + self.name


class NewRound(Impulse):
    '''
    Run Script when starting a new towerTesting round
    '''

    def __init__(self):
        super().__init__(b'game.newround')


class WakeUp(Impulse):
    '''
    Run script on wakeup
    '''

    def __init__(self):
        super().__init__(b'wakeup')


class OpenPlace(Impulse):
    '''
    Run script when <place> is opened
    '''

    def __init__(self,
                 place: Union[str, String_]):
        if type(place) == String_:
            place = place.text
        place = place.lower()
        super().__init__(b'open.' + bytes(place, "utf-8"))


class KeyPress(Impulse):
    '''
    Run script when <key> is pressed
    '''

    def __init__(self, key):  # key can be int or string, i just sanitise both
        key = str(key)
        if len(key) != 1:
            raise ValueError("key must be length 1")
        if not key.isalnum():
            raise ValueError("key must be alphanumeric")
        super().__init__(bytes(f"key.{key}".lower(), "utf-8"))
