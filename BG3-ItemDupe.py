import win32api, win32gui, win32con # pyright: ignore[reportMissingModuleSource]
from time import sleep

preview = (875, 1092)
right = 1045
left = 710
top = 350
bottom = 980
null = (0,0)
menu = (251, 464)
mid = (1280, 630)

def rgbTuple(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)

def getColor(coords):
    return rgbTuple(win32gui.GetPixel(
        win32gui.GetDC(win32gui.GetActiveWindow()), coords[0], coords[1]))

def checkIfInMenu():
    if(getColor(menu) != (0, 0, 0)):
        return True
    else:
        return False

def pressMouse(coords = null):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, coords[0], coords[1],0,0)

def releaseMouse(coords = null):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, coords[0], coords[1],0,0)

def dupe(coords):
    win32api.SetCursorPos(preview)
    pressMouse()
    releaseMouse()
    sleep(0.1)
    win32api.SetCursorPos(coords)
    pressMouse()
    sleep(0.05)
    win32api.SetCursorPos(mid)

def ifNotMenu():
    win32api.SetCursorPos(preview)
    pressMouse()
    releaseMouse()
    sleep(0.25)

def main():
    print(f"Helmet: 1, Cloak: 2, Armor: 3, Gloves: 4, Boots: 5")
    print(f"Amulvet: 11, Ring 1: 12, Ring 2: 13")
    print(f"Weapon: 21, Shield: 22, Bow 1: 23, Bow 2: 24, Torch 25, Instrument: 26")
    print(f"Camp clothes: 31, Shoes: 32, Undies: 33")

    while True:
        choice = (input("Select: "))
        area = None

        if(len(choice) > 2 and len(choice) < 1):
            print(f"kys")
            main()
            return
        elif(len(choice) > 1):
            area = int(choice[0])
        else:
            area = 0

        if(not checkIfInMenu()):
            ifNotMenu()

        if (area == None):
            continue
        
        match area:
            case 0:
                dupe((left,top+57*(int(choice)-1)))
            case 1:
                dupe((right,int(top+57*3.5)+57*(int(choice[1])-1)))
            case 2:
                if(int(choice[1]) < 3):
                    dupe((left+57*(int(choice[1])-1),bottom))
                elif(int(choice[1]) < 5):
                    dupe((right-57*(int(choice[1])-1),bottom))
                else:
                    dupe((left+(right-left)*(int(choice[1])-5),bottom-(int(57*1.5))))
            case 3:
                dupe((right, top+57*(int(choice[1])-1)))



if __name__ == "__main__":
    main()