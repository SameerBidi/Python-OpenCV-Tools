import win32gui
import win32api
import cv2
import mss
import mss.tools
import threading
import time
import pyHook
import pythoncom
import winsound
import numpy as np

stopDrawing = False
tkey = "P"
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
savePath = "captured/"

def drawRect(x1, y1, x2, y2, xDiff, yDiff):
  dc = win32gui.GetDC(0)
  color = win32api.RGB(255, 0, 0)

  while(True):
    global stopDrawing
    for i in range(xDiff):
      win32gui.SetPixel(dc, x1 + i, y1, color)
      win32gui.SetPixel(dc, x2 - i, y2, color)
    for i in range(yDiff):
      win32gui.SetPixel(dc, x1, y1 + i, color)
      win32gui.SetPixel(dc, x2, y2 - i, color)
    if(stopDrawing): break

def OnKeyboardEvent(event):
  global stopDrawing, monitor, savePath
  if(event.Key == 'Escape'):
    stopDrawing = True

  if(event.Key.upper() == tkey.upper()):
    with mss.mss() as sct:
      output = f"{savePath}/{int(time.time()*1000.0)}.jpg"
      sct_img = np.array(sct.grab(monitor))
      cv2.imwrite(output, sct_img)
      winsound.Beep(1000, 100)
      print(output)

  return True

def init():
  global stopDrawing, tkey, monitor, savePath
  stopDrawing = False

  print("\n1: Fullscreen\n2: Defined Coordinates")
  ch = input("Enter your choice: ")
  print("")
  if (ch == "1"):
    w = int(input("Screen Width: "))
    h = int(input("Screen Height: "))
    monitor = {"top": 0, "left": 0, "width": w, "height": h}
  elif (ch == "2"):
    print("Enter top left x y")
    x1 = int(input("x: "))
    y1 = int(input("y: "))
    print("Enter bottom right x y")
    x2 = int(input("x: "))
    y2 = int(input("y: "))

    xDiff = x2 - x1
    yDiff = y2 - y1

    monitor = {"top": y1, "left": x1, "width": xDiff, "height": yDiff}
    th = threading.Thread(target=drawRect, args=(x1 - 1, y1 - 1, x2, y2, xDiff + 1, yDiff + 1))
    th.start()
  else: return

  savePath = input("Enter folder path to save images: ")
  tkey = input("Enter screenshot trigger key: ")
  print(f"\nPress {tkey} to take screenshot, you will hear a beep once a screenshot is captured")
  print(f"Screenshots will be saved to {savePath}")
  print("Press Escape key to end the screenshot process")

  hm = pyHook.HookManager()
  hm.KeyDown = OnKeyboardEvent
  hm.HookKeyboard()
  try:
    while not stopDrawing:
      pythoncom.PumpWaitingMessages()
  except KeyboardInterrupt:
    stopDrawing = True
    pass