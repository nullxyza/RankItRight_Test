
def checkvalidityfn(inp,symb):
    newlst= []
    js = [inp[i] for i in range(0, len(inp))]
    if js[0] == '+':
        js.pop(1)
    for i in range(0, len(js)):
        if js[i] not in symb:
            newlst.append(js[i])
        else:
            continue
    if len(newlst)==10:
        return True
    else:
        return False


Inp = input()
symbols = ['-','.',' ','(',')','+']

if (checkvalidityfn(Inp,symbols)):
    print("Valid Number")
else:
    print("Not a Valid Number")




