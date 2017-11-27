def right_justify(inTxt):
    count = 70 - len(inTxt)
    outTxt = ' ' * count + inTxt
    print(outTxt)

right_justify('Gogo')
