from .BaseClass import *


class Getter(Interface):
    '''
    Get a stored value <varName>
    '''
    def __init__(self,
                 name: bytes,
                 varName: Union[str, String_]):
        self.name = checkType(name, bytes)
        self.varName = checkType(varName, str, String_)

    def asBytes(self) -> bytes:
        return (bytes([len(self.name)])
                + bytes(self.name)
                + self.varName.asBytes())


class GET_Local_Int(Getter, Integer_):
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'local.int.get', varName)


class GET_Global_Int(Getter, Integer_):  # TODO
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'global.int.get', varName)


class GET_Local_Double(Getter, Double_):  # TODO
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'local.double.get', varName)


class GET_Global_Double(Getter, Double_):  # TODO
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'global.double.get', varName)


class GET_Local_String(Getter, String_):  # TODO
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'local.string.get', varName)


class GET_Global_String(Getter, String_):  # TODO
    def __init__(self, varName: Union[str, String_]):
        super().__init__(b'global.string.get', varName)


class Setter(Interface):
    def __init__(self,
                 name: bytes,
                 varName: Union[str, String_], value: Interface):
        self.name = checkType(name, bytes)
        self.varName = checkType(varName, str, String_)
        self.value = value  # different type depending on whomst

    def asBytes(self) -> bytes:
        return (bytes([len(self.name)]) + bytes(self.name)
                + self.varName.asBytes()
                + self.value.asBytes())


class Set_Global_Int(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[int, Integer_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, int, Integer_)
        super().__init__(b'global.int.set', varName, value)


class Set_Local_Int(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[int, Integer_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, int, Integer_)
        super().__init__(b'local.int.set', varName, value)


class Set_Global_Double(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[float, Double_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, float, Double_)
        super().__init__(b'global.double.set', varName, value)


class Set_Local_Double(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[float, Double_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, float, Double_)
        super().__init__(b'local.double.set', varName, value)


class Set_Global_String(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[str, String_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, str, String_)
        super().__init__(b'global.string.set', varName, value)


class Set_Local_String(Setter):
    def __init__(self,
                 varName: Union[str, String_],
                 value: Union[str, String_]):
        varName = checkType(varName, str, String_)
        value = checkType(value, str, String_)
        super().__init__(b'local.string.set', varName, value)
