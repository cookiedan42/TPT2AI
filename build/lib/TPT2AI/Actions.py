from .BaseClass import *


class Action(Interface):
    '''
    Base Class for Actions
    '''

    def __init__(self, name: bytes):
        self.name = checkType(name, bytes)

    def asBytes(self) -> bytes:
        return bytes([len(self.name)]) + self.name


class GOTO(Action):
    '''
    GOTO target line
    '''

    def __init__(self,
                 target: Union[int, Integer_]):
        super().__init__(b'generic.goto')
        self.target = checkType(target, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.target.asBytes())


class GOTO_IF(Action):
    '''
    GOTO target line if condition is true
    '''

    def __init__(self,
                 target: Union[int, Integer_],
                 condition: Union[bool, Boolean_]):
        super().__init__(b'generic.goto')
        self.target = checkType(target, int, Integer_)
        self.condition = checkType(condition, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.target.asBytes()
                + self.condition.asBytes())


class Click(Action):
    '''
    Click on screen at (x,y)
    '''

    def __init__(self,
                 x: Union[float, Double_],
                 y: Union[float, Double_]):
        super().__init__(b'generic.click')
        self.x = checkType(x, float, Double_)
        self.y = checkType(y, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.x.asBytes()
                + self.y.asBytes())


class Slider(Action):
    '''
    Move a slider at slider vector to target fraction of its full value
    '''

    def __init__(self,
                 slider: Vector_,
                 target: Union[float, Double_]):
        super().__init__(b'generic.slider')
        self.slider = checkType(slider, target=Vector_)
        # target needs to be between 0 and 1
        self.target = checkType(target, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.slider.asBytes()
                + self.target.asBytes())


class ScrollRect(Action):
    '''
    Scroll scrollable at scrollable vector to (x,y)
    '''

    def __init__(self,
                 scrollable: Vector_,
                 x: Union[float, Double_],
                 y: Union[float, Double_]):
        super().__init__('')
        self.scrollable = checkType(scrollable, target=Vector_)
        self.x = checkType(x, float, Double_)
        self.y = checkType(y, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.scrollable.asBytes()
                + self.x.asBytes()
                + self.y.asBytes())


class Wait(Action):
    '''
    Wait for time seconds
    '''

    def __init__(self,
                 time: Union[float, Double_]):
        super().__init__(b'generic.wait')
        self.time = checkType(time, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.time.asBytes())


class WaitWhile(Action):
    '''
    Wait while condition true
    '''

    def __init__(self,
                 condition: Union[bool, Boolean_]):
        super().__init__('generic.waitwhile')
        self.condition = checkType(condition, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.condition.asBytes())


class WaitUntil(Action):
    '''
    Wait until condition true
    '''

    def __init__(self,
                 condition: Union[bool, Boolean_]):
        super().__init__('generic.waituntil')
        self.condition = checkType(condition, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.condition.asBytes())


class Execute(Action):
    '''
    Execute scriptName
    '''

    def __init__(self,
                 scriptName: Union[str, String_]):
        super().__init__(b'generic.execute')
        self.scriptName = checkType(scriptName, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.scriptName.asBytes())


class ExecuteSync(Action):
    '''
    Execute scriptName and wait for it to finish
    '''

    def __init__(self,
                 scriptName: Union[str, String_]):
        super().__init__(b'generic.executesync')
        self.scriptName = checkType(scriptName, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.scriptName.asBytes())


class Stop(Action):
    '''
    Stop all scripts named scriptName
    '''

    def __init__(self,
                 scriptName: Union[str, String_]):
        super().__init__(b'generic.stop')
        self.scriptName = checkType(scriptName, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.scriptName.asBytes())


class OpenWindow(Action):
    '''
    Open window named window if condition evaluates to true
    '''

    def __init__(self,
                 window: Union[str, String_],
                 condition: Union[bool, Boolean_]):
        super().__init__(b'town.window.show')
        self.window = checkType(window, str, String_)
        self.condition = checkType(condition, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.window.asBytes()
                + self.condition.asBytes())


class Dig(Action):
    '''
    Dig at (x,y) in the mine
    '''

    def __init__(self,
                 x: Union[int, Integer_],
                 y: Union[int, Integer_]):
        super().__init__(b'mine.dig')
        self.x = checkType(x, int, Integer_)
        self.y = checkType(y, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.x.asBytes()
                + self.y.asBytes())


class NewLayer(Action):
    '''
    Generate new layer in mine
    '''

    def __init__(self):
        super().__init__(b'mine.newlayer')


class Craft(Action):
    '''
    Craft <count> <item>s of <tier> 
    '''

    def __init__(self,
                 item: Union[str, String_],
                 tier: Union[int, Integer_],
                 count: Union[float, Double_]):
        super().__init__(b'factory.craft')
        self.item = checkType(item, str, String_)
        self.tier = checkType(tier, int, Integer_)
        self.count = checkType(count, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.item.asBytes()
                + self.tier.asBytes()
                + self.count.asBytes())


class Produce(Action):
    '''
    Put  <count> <item>s of <tier> into <destination>
    '''

    def __init__(self,
                 item: Union[str, String_],
                 tier: Union[int, Integer_],
                 count: Union[float, Double_],
                 destination: Union[str, String_]):
        super().__init__(b'factory.produce')
        self.item = checkType(item, str, String_)
        self.tier = checkType(tier, int, Integer_)
        self.count = checkType(count, float, Double_)
        self.destination = checkType(destination, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.item.asBytes()
                + self.tier.asBytes()
                + self.count.asBytes()
                + self.destination.asBytes())


class PowerplantSell(Action):
    '''
    Sell the object at (x,y) in the powerplant
    '''

    def __init__(self,
                 x: Union[int, Integer_],
                 y: Union[int, Integer_]):
        super().__init__(b'powerplant.sell')
        self.x = checkType(x, int, Integer_)
        self.y = checkType(y, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.x.asBytes()
                + self.y.asBytes())


class RefreshTrade(Action):
    '''
    Regenerate the trades in trading post
    '''

    def __init__(self):
        super().__init__(b'tradingpost.refresh')


class TradePost(Action):
    '''
    Trade the offer at positon tradeNo using tradeFrac of the available resources
    '''

    def __init__(self,
                 tradeNo: Union[int, Integer_],
                 tradeFrac: Union[float, Double_]):
        super().__init__(b'tradingpost.trade')
        self.tradeNo = checkType(tradeNo, int, Integer_)
        self.tradeFrac = checkType(tradeFrac, float, Double_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.tradeNo.asBytes()
                + self.tradeFrac.asBytes())


class MuseumFill(Action):
    '''
    Set Museum Fill buy to newState
    '''

    def __init__(self,
                 newState: Union[bool, Boolean_]):
        super().__init__(b'museum.fill')
        self.newState = checkType(newState, bool, Boolean_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.newState.asBytes())


class MuseumCombine(Action):
    '''
    Combine Powerstones up to tier maxTier, 0 for unrestricted
    '''

    def __init__(self,
                 maxTier: Union[int, Integer_] = 0):
        super().__init__(b'museum.combine')
        self.maxTier = checkType(maxTier, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.maxTier.asBytes())


class MuseumTransmute(Action):
    '''
    Transmute PowerStones
    '''

    def __init__(self):
        super().__init__(b'museum.transmute')


class MuseumBuy(Action):
    '''
    Buy powerstones of <element>
    '''

    def __init__(self,
                 element: Union[str, String_]):
        super().__init__(b'museum.buy')
        self.element = checkType(element, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.element.asBytes())


class MuseumBuyMarket(Action):
    '''
    Buy powerstones from market of <element> up to <tier> 
    '''

    def __init__(self,
                 element: Union[str, String_],
                 tier: Union[int, Integer_]):
        super().__init__(b'museum.buyMarket')
        self.element = checkType(element, str, String_)
        self.tier = checkType(tier, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.element.asBytes()
                + self.tier.asBytes())


class MuseumMove(Action):
    '''
    Move powerstone from <source[index]> to destination
    '''

    def __init__(self,
                 source: Union[str, String_],
                 index: Union[int, Integer_],
                 destination: Union[str, String_]):
        super().__init__(b'museum.move')
        self.source = checkType(source, str, String_)
        self.index = checkType(index, int, Integer_)
        self.destination = checkType(destination, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.source.asBytes()
                + self.index.asBytes()
                + self.destination.asBytes())


class MuseumDelete(Action):
    '''
    Delete Powerstone at <target[index]>
    '''

    def __init__(self,
                 target: Union[str, String_],
                 index: Union[int, Integer_]):
        super().__init__(b'museum.delete')
        self.target = checkType(target, str, String_)
        self.index = checkType(index, int, Integer_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.target.asBytes()
                + self.index.asBytes())


class MuseumClear(Action):
    '''
    Delete all powerstones from 
    '''

    def __init__(self,
                 target: Union[str, String_]):
        super().__init__(b'museum.clear')
        self.target = checkType(target, str, String_)

    def asBytes(self) -> bytes:
        return (super().asBytes()
                + self.target.asBytes())
