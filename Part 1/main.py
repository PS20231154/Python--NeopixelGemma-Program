import globalvariables

import time
import board
import neopixel
 
pixpin = board.A3
numpix = 128


strip = neopixel.NeoPixel(pixpin, numpix, brightness=0.1, auto_write=False)


def lookupColor(color,i):
    if color == 0:
        strip[i] = (255,0,0)
    # orange
    elif color == 1:
        strip[i] = (255,179,0)
    # yellow
    elif color == 2:
        strip[i] = (0,0,255)
    # green
    elif color == 3:
        strip[i] = (255,255,255)
    # blue
    elif color == 4:
        strip[i] = (0,0,255)
    # violet
    elif color == 5:
        strip[i] = (62,0,105)
    # pink
    elif color == 7:
        strip[i] = (247,50,255)
    # black
    elif color == 9:
        strip[i] = (0,0,0)

def showMessage(nextMessage,duration,myMessage):
    # start - fixed message 4 
    # remember to change globalvariables.message#
    i = 0
    for r in range(0,8):
        for c in range(0,8):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    for r in range(0,8):
        for c in range(8,16):
            color = myMessage[r][c]
            lookupColor(color,i)
            i += 1
    strip.write()
    time.sleep(duration)

    # switch to next message
    globalvariables.messageID = nextMessage


def showMessageL(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength += 1
    globalvariables.durationCounter += 1
    if globalvariables.countToMaxLength > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage



def showMessageR(nextMessage,duration,myMessage,startingPoint):
    # start - show Message
    if globalvariables.myStart == 0:
        globalvariables.myStart = 1
        globalvariables.countToMaxLength = startingPoint

        

    i = 0
    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength,globalvariables.countToMaxLength+8):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    for r in range(0,8):
        for c in range(globalvariables.countToMaxLength+8,globalvariables.countToMaxLength+16):
            temp = c % len(myMessage[0])
            color = myMessage[r][temp]
            lookupColor(color,i)
            i += 1

    strip.write()

    globalvariables.countToMaxLength -= 1
    globalvariables.durationCounter += 1
    if globalvariables.durationCounter > duration:
        globalvariables.countToMaxLength = 0
        globalvariables.myStart = 0
        globalvariables.durationCounter = 0
        globalvariables.messageID = nextMessage



while True:
    if globalvariables.messageID == 1:
        strip.write()
        showMessage(2,5,globalvariables.message1)
    elif globalvariables.messageID == 2:
        strip.write()
        showMessageL(3,16,globalvariables.message2,0)
    elif globalvariables.messageID == 3:
        strip.write()
        showMessageL(4,16,globalvariables.message3,0)
    elif globalvariables.messageID == 4:
        strip.write()
        showMessageL(4,16,globalvariables.message4,0)
