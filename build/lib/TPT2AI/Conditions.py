from .BaseClass import *


class TRUE(Boolean_):
    def __init__(self):
        super().__init__(True)


class FALSE(Boolean_):
    def __init__(self):
        super().__init__(False)


class Condition(Boolean_):
    def __init__(self, name: bytes):
        self.name = checkType(name, bytes)

    def asBytes(self) -> bytes:
        return bytes([len(self.name)]) + self.name


class Compare(Condition):
    def __init__(self, name: bytes, left, comparator: String_, right):
        super().__init__(name)
        self.left = left
        self.comparator = comparator
        self.right = right

    def asBytes(self):
        return(
            super().asBytes()
            + self.left.asBytes()
            + self.comparator.asBytes()
            + self.right.asBytes()
        )


class BoolCompare(Compare):
    def __init__(self,
                 left: Union[bool, Boolean_],
                 comparator: Union[str, String_],
                 right: Union[bool, Boolean_]):
        left = checkType(left, bool, Boolean_)
        right = checkType(right, bool, Boolean_)
        comparator = checkType(comparator, str, String_)
        super().__init__(b'comparison.bool', left, comparator, right)


class IntCompare(Compare):
    def __init__(self,
                 left: Union[int, Integer_],
                 comparator: Union[str, String_],
                 right: Union[int, Integer_]):
        left = checkType(left, int, Integer_)
        right = checkType(right, int, Integer_)
        comparator = checkType(comparator, str, String_)
        super().__init__(b'comparison.int', left, comparator, right)


class DoubleCompare(Compare):
    def __init__(self,
                 left: Union[float, Double_],
                 comparator: Union[str, String_],
                 right: Union[float, Double_]):
        left = checkType(left, float, Double_)
        right = checkType(right, float, Double_)
        comparator = checkType(comparator, str, String_)
        super().__init__(b'comparison.double', left, comparator, right)


class StringCompare(Compare):
    def __init__(self,
                 left: Union[str, String_],
                 comparator: Union[str, String_],
                 right: Union[str, String_]):
        left = checkType(left, str, String_)
        right = checkType(right, str, String_)
        comparator = checkType(comparator, str, String_)
        super().__init__(b'comparison.string', left, comparator, right)


class TowerStunned(Condition):  # boolean
    def __init__(self):
        super().__init__(b'tower.stunned')


class WindowOpen(Condition):
    def __init__(self, value: Union[str, String_]):
        super().__init__(b'town.window.isopen')
        self.value = checkType(value, str, String_)

    def asBytes(self) -> bytes:
        return super().asBytes() + self.value.asBytes()


class Machine(Condition):
    def __init__(self, machineName: Union[str, String_]):
        super().__init__(b'factory.machine.active')
        self.machineName = checkType(machineName, str, String_)

    def asBytes(self) -> bytes:
        return super().asBytes() + self.machineName.asBytes()


class MuseumFill(Condition):
    def __init__(self):
        super().__init__(b'museum.isfill')
