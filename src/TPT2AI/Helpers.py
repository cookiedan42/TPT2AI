from .BaseClass import *

def ExportToBytes(exportString:str)-> bytes:
    '''
    convert AI export to understandable bytes
    ''' 
    return base64.b64decode(exportString)

def floatToBytes(f:float) -> bytes:
    '''
    Convert a float to byte representation of a Double
    '''
    return struct.pack("d",f)

def intToBytes(i):
    '''
    Convert an integer to 4 Byte representation
    '''
    return int.to_bytes(i,4,'little',signed=True)