from TPT2AI import *



def make_DiggerCall():
    '''
    Demo add name, impulse, condition, action
    '''

    diggercall = Script("diggercall")
    diggercall.addImpulse(OpenPlace(SCREENS.MINE))
    diggercall.addCondition(WindowOpen(SCREENS.MINE))
    diggercall.addAction(ExecuteSync("digger"))
    return diggercall.export()

def make_Digger():
    '''
    Demo procedural generation of hardcoded values
    '''
    digger = Script("digger")
    for i in range(4):
        for j in range(4):
            digger.addAction(Dig(i,j))
    digger.addAction(NewLayer())

    return digger.export()

print()
print(make_DiggerCall())

print()
print(make_Digger())