from .BaseClass import *


class IntClass(Integer_):
    '''
    Middleware for statements that evaluate to Integer_
    '''

    def __init__(self, name: bytes):
        self.name = checkType(name, bytes)

    def asBytes(self) -> bytes:
        return bytes([len(self.name)]) + self.name


class IntArithmetic(IntClass):
    '''
    Math operation : Left Operator Right
    '''

    def __init__(self,
                 left: Union[int, Integer_],
                 operator: Union[str, String_],
                 right: Union[int, Integer_]):
        super().__init__(b'arithmetic.int')
        self.left = checkType(left, int, Integer_)
        self.operator = checkType(operator, str, String_)
        self.right = checkType(right, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.left.asBytes()
                + self.operator.asBytes()
                + self.right.asBytes())


class d2i(IntClass):
    '''
    Double to Int
    '''

    def __init__(self,
                 doubleInput: Union[float, Double_]):
        super().__init__(b'd2i')
        self.doubleInput = checkType(doubleInput, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes() + self.doubleInput.asBytes())


class RandomInt(IntClass):
    '''
    Random Integer between low and high
    '''

    def __init__(self,
                 low: Union[int, Integer_],
                 high: Union[int, Integer_]):
        super().__init__(b'int.rnd')
        self.low = checkType(low, int, Integer_)
        self.high = checkType(high, int, Integer_)


class IntScreenWidth(IntClass):  # IN PIXELS
    '''
    Screen Width in Pixels
    '''

    def __init__(self):
        super().__init__(b'screen.width')


class IntScreenHeight(IntClass):  # IN PIXELS
    '''
    Screen Height in Pixels
    '''

    def __init__(self):
        super().__init__(b'screen.height')


class IntMin(IntClass):
    '''
    Minimum of two Integers
    '''

    def __init__(self,
                 first: Union[int, Integer_],
                 second: Union[int, Integer_]):
        super().__init__(b'int.min')
        self.first = checkType(first, int, Integer_)
        self.second = checkType(second, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.first.asBytes()
                + self.second.asBytes())


class IntMax(IntClass):
    '''
    Maximum of two Integers
    '''

    def __init__(self,
                 first: Union[int, Integer_],
                 second: Union[int, Integer_]):
        super().__init__(b'int.max')
        self.first = checkType(first, int, Integer_)
        self.second = checkType(second, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.first.asBytes()
                + self.second.asBytes())


class StringLength(IntClass):
    '''
    Length of string <value>
    '''

    def __init__(self,
                 value: Union[str, String_]):
        super().__init__(b'string.length')
        self.value = checkType(value, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.value.asBytes())


class TowerBuffsNegative(IntClass):
    '''
    Number of negative Buffs active on the tower
    '''

    def __init__(self):
        super().__init__(b'tower.buffs.negative')


class TradeOfferCount(IntClass):
    '''
    Number of Trade offers at trading post
    '''

    def __init__(self):
        super().__init__(b'tradingpost.offerCount')


class MuseumFreeSlots(IntClass):
    '''
    Number of free slots in <target> location of museum
    '''

    def __init__(self,
                 target: Union[str, String_]):
        super().__init__(b'museum.freeSlots')
        self.target = checkType(target, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes() + self.target.asBytes())


class MuseumStoneTier(IntClass):
    '''
    Tier of Stone at target[index]
    '''

    def __init__(self,
                 target: Union[str, String_],
                 index: Union[int, Integer_]):
        super().__init__(b'museum.stone.tier')
        self.target = checkType(target, str, String_)
        self.index = checkType(index, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.target.asBytes()
                + self.index.asBytes())
