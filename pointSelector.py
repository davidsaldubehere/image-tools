from pynput import mouse
import argparse
from time import sleep
clickPositions = []
def getClickPos(x, y, button, pressed):
    clickPositions.append(f'{x} width, {y} height')
    return False

def startListener():
    with mouse.Listener(on_click=getClickPos) as listener:
        listener.join()

parser = argparse.ArgumentParser(description='Return the positions of mouse clicks')
parser.add_argument('Clicks',
                       metavar='clicks',
                       type=int,
                       help='Number of recorded clicks')
args = parser.parse_args()

for i in range(args.Clicks):
    startListener()
    #pausing for 10 milliseconds prevents accidental double recording
    sleep(.1)
for item in clickPositions:
    print(item)