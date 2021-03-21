
import base64
import struct
from typing import TypeVar, Union

# TODO: how to validate inputs


def checkType(value, primitive=None, target=None):
    if target != None and isinstance(value, target):
        return value
    if primitive != None and isinstance(value, primitive):
        if target == None:
            return value
        return target(value)
    raise TypeError(f"Target must be "
                    + (f"{type(primitive)} " if primitive != None else "")
                    + ("or " if primitive != None and target != None else "")
                    + (f" {type(target)} " if target != None else "")
                    + f"type, received {type(value)}")


'''
everyClass needs a asBytes method
'''


class Interface():
    '''
    return the byte representation of this object
    '''

    def asBytes(self):
        raise NotImplementedError


class Boolean_(Interface):  # < True False?
    def __init__(self, value):
        self.value = value

    def asBytes(self):
        return (b'\x08constant\x01'
                + (b'\x01' if self.value else b'\x00'))


class Integer_(Interface):
    def __init__(self, value: int):
        if abs(value) > 999999999:
            raise ValueError("game only supports 9 digit int")
        self.value = value

    def asBytes(self):
        return (b'\x08constant\x02'
                + int.to_bytes(self.value, 4, 'little', signed=True))


class Double_(Interface):
    def __init__(self, value):
        self.value = value

    def asBytes(self):
        return (b'\x08constant\x03' +
                struct.pack("d", self.value))


class String_(Interface):
    def __init__(self, text):
        if len(text) > 60:
            raise ValueError("game only supports text up to 60 char")
        self.text = text

    def asBytes(self):
        return (b'\x08constant\x04'
                + bytes([len(self.text)])
                + bytes(self.text, "utf-8"))


class Vector_(Interface):
    def __init__(self, x: float, y: float):
        self.x = checkType(x, float)
        self.y = checkType(y, float)

    def asBytes(self) -> bytes:
        return (b'\x08constant\x05'
                + struct.pack("f", self.x)
                + struct.pack("f", self.y))

# CONSTANTS


class CRAFT():
    MOTOR = String_("motor")
    CHIP = String_("chip")
    CABLE = String_("cable.insulated")
    BLOCK = String_("block")
    PUMP = String_("pump")
    STACK = String_("plate.stack")
    LUMP = String_("lump")

    P_TOWN = String_('producer.town')
    P_MINE = String_('producer.mine')
    P_POWERPLANT = String_('producer.powerplant')
    P_FACTORY = String_('producer.factory')
    P_WORKSHOP = String_('producer.workshop')
    P_CONSTRUCTIONFIRM = String_('producer.constructionFirm')
    P_HEADQUARTERS = String_('producer.headquarters')
    P_LABORATORY = String_('producer.laboratory')
    P_TRADINGPOST = String_('producer.tradingpost')
    P_ARCADE = String_('producer.arcade')
    P_MUSEUM = String_('producer.museum')
    P_SHIPYARD = String_('producer.shipyard')
    P_STATUEOFCUBOS = String_('producer.statueofcubos')
    P_GEMS = String_('producer.gems')
    P_EXOTICGEMS = String_('producer.exoticgems')


class MACHINES():
    OVEN = String_("oven")
    ASSEMBLY = String_("assembly")
    REFINER = String_("refiner")
    CRUSHER = String_("crusher")
    CUTTER = String_("cutter")
    PRESSER = String_("presser")
    MIXER = String_("mixer")
    SHAPER = String_("shaper")
    BOILER = String_("boiler")


class SCREENS():  # TODO: verify these strings
    TOWER = String_("towertesting")
    TRADING = String_("tradingpost")
    POWER = String_("powerplant")
    FACTORY = String_("factory")
    LAB = String_("laboratory")
    SHIPYARD = String_("shipyard")
    WORKSHOP = String_("workshop")
    ARCADE = String_("arcade")
    MUSEUM = String_("museum")
    HEADQUARTERS = String_("headquarters")
    CONSTRUCTION = String_("constructionfirm")
    STATUE = String_("statueofcubos")
    MINE = String_("mine")


class MUSEUM():
    INVENTORY = String_("inventory")
    EQUIPPED = String_("equipped")
    CUBOSCUBE = String_("cuboscube")
    COMBINATOR = String_("combinator")


class OPERATORS():
    PLUS = String_("+")
    MINUS = String_("-")
    TIMES = String_("*")
    DIVIDE = String_("/")
    MOD = String_("MOD")
    POW = String_("POW")
    LOG = String_("LOG")



class COMPARATORS():
    EQUAL = String_("==")
    NOT_EQUAL = String_("!=")
    LESS = String_("<")
    LESS_EQUAL = String_("<=")
    GREATER = String_(">")
    GREATER_EQUAL = String_(">=")
    AND = String_("&&")
    OR = String_("||")