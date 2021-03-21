from .BaseClass import *
from .Impulses import *
from .Conditions import *
from .Actions import *


class Script(Interface):
    '''
    Script class for assembly
    '''

    def __init__(self, name: str = "default"):
        self.name = name.lower()
        self.impulses = []
        self.conditions = []
        self.actions = []

    def addImpulse(self, impulse: Impulse):
        self.impulses += [impulse]

    def addCondition(self, condition: Condition):
        self.conditions += [condition]

    def addAction(self, action: Action):
        self.actions += [action]

    def asBytes(self):
        bt = bytes([len(self.name)]) + bytes(self.name, "utf-8")

        bt += int.to_bytes(len(self.impulses), 4, 'little', signed=True)
        for i in self.impulses:
            bt += i.asBytes()

        bt += int.to_bytes(len(self.conditions), 4, 'little', signed=True)
        for i in self.conditions:
            bt += i.asBytes()

        bt += int.to_bytes(len(self.actions), 4, 'little', signed=True)
        for i in self.actions:
            bt += i.asBytes()

        return bt

    def export(self):
        return str(base64.b64encode(self.asBytes()), "utf-8")
