from .BaseClass import *


class DoubleClass(Double_):
    def __init__(self, name: bytes):
        self.name = checkType(name, bytes)

    def asBytes(self) -> bytes:
        return bytes([len(self.name)]) + self.name


class DoubleArithmetic(DoubleClass):
    def __init__(self,
                 left: Union[float, Double_],
                 operator: Union[str, String_],
                 right: Union[float, Double_]):
        super().__init__(b'arithmetic.double')
        self.left = checkType(left, float, Double_)
        self.operator = checkType(operator, str, String_)
        self.right = checkType(right, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.left.asBytes()
                + self.operator.asBytes()
                + self.right.asBytes())


class PI(DoubleClass):
    def __init__(self):
        super().__init__(b'const.pi')


class VEC2X(DoubleClass):
    def __init__(self,
                 vector: Vector_):
        super().__init__(b'vec2.x')
        self.vector = checkType(vector, target=Vector_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.vector.asBytes())


class VEC2Y(DoubleClass):
    def __init__(self,
                 vector: Vector_):
        super().__init__(b'vec2.y')
        self.vector = checkType(vector, target=Vector_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.vector.asBytes())


class DoubleScreenWidth(DoubleClass):  # IN PIXELS
    def __init__(self):
        super().__init__(b'screen.width.d')


class DoubleScreenHeight(DoubleClass):  # IN PIXELS
    def __init__(self):
        super().__init__(b'screen.height.d')


class I2D(DoubleClass):
    def __init__(self,
                 value: Union[int, Integer_]):
        super().__init__(b'i2d')
        self.value = checkType(value, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.value.asBytes())


class RandDouble(DoubleClass):
    def __init__(self,
                 lower: Union[float, Double_],
                 upper: Union[float, Double_]):
        super().__init__(b'double.rnd')
        self.lower = checkType(lower, float, Double_)
        self.upper = checkType(upper, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.lower.asBytes()
                + self.upper.asBytes())


class DoubleMin(DoubleClass):
    def __init__(self,
                 first: Union[float, Double_],
                 second: Union[float, Double_]):
        super().__init__(b'double.min')
        self.first = checkType(first, float, Double_)
        self.second = checkType(second, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.first.asBytes()
                + self.second.asBytes())


class DoubleMax(DoubleClass):
    def __init__(self,
                 first: Union[float, Double_],
                 second: Union[float, Double_]):
        super().__init__(b'double.max')
        self.first = checkType(first, float, Double_)
        self.second = checkType(second, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.first.asBytes()
                + self.second.asBytes())


class Floor(DoubleClass):
    def __init__(self,
                 value: Union[float, Double_]):
        super().__init__(b'double.floor')
        self.value = checkType(value, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.value.asBytes())


class Ceiling(DoubleClass):
    def __init__(self,
                 value: Union[float, Double_]):
        super().__init__(b'double.ceil')
        self.value = checkType(value, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.value.asBytes())


class Round(DoubleClass):
    def __init__(self,
                 value: Union[float, Double_]):
        super().__init__(b'double.round')
        self.value = checkType(value, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.value.asBytes())


class TowerHealth(DoubleClass):
    def __init__(self,
                 percentage: Union[bool, Boolean_]):
        super().__init__(b'tower.health')
        self.percentage = checkType(percentage, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.percentage.asBytes())


class TowerHealthMax(DoubleClass):
    def __init__(self):
        super().__init__(b'tower.health.max')


class TowerHealthRegen(DoubleClass):
    def __init__(self):
        super().__init__(b'tower.health.regeneration')


class TowerEnergy(DoubleClass):
    def __init__(self,
                 percentage: Union[bool, Boolean_]):
        super().__init__(b'tower.energy')
        self.percentage = checkType(percentage, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.percentage.asBytes())


class TowerEnergyMax(DoubleClass):
    def __init__(self):
        super().__init__(b'tower.energy.max')


class TowerHealthRegen(DoubleClass):
    def __init__(self):
        super().__init__(b'tower.energy.regeneration')


class TowerShield(DoubleClass):
    def __init__(self,
                 percentage: Union[bool, Boolean_]):
        super().__init__(b'tower.shield')
        self.percentage = checkType(percentage, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.percentage.asBytes())


class TowerShieldMax(DoubleClass):
    def __init__(self):
        super().__init__(b'tower.shield.max')


class TowerModuleCooldown(DoubleClass):
    def __init__(self,
                 index: Union[int, Integer_]):
        super().__init__(b'tower.module.cooldown')
        self.index = checkType(index, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.index.asBytes())


class FactoryItemCount(DoubleClass):
    def __init__(self,
                 item: Union[str, String_],
                 tier: Union[int, Integer_]):
        super().__init__(b'factory.items.count')
        self.item = checkType(item, str, String_)
        self.tier = checkType(tier, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.item.asBytes()
                + self.tier.asBytes())
