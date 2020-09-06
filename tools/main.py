import screenshotter
import converter
import findhsv
import traincascade
import testcascade
import sys

def getUserInputAndDoStuff():
  print("\n1: Take screenshots\n2: Convert images to grayscale\n3: Find HSV Color Range\n4: Train Haar Cascade\n5: Test Haar Cascade\n6: Exit")
  ch = input("Enter your choice: ")

  if (ch == "1"):
    screenshotter.init()
  elif (ch == "2"):
    converter.convertToGrayscale()
  elif (ch == "3"):
    findhsv.init()
  elif (ch == "4"):
    traincascade.init()
  elif (ch == "5"):
    testcascade.init()
  elif (ch == "6"):
    sys.exit()

if __name__ == "__main__":
  print("\nCredits:")
  print("Sentdex: https://www.youtube.com/user/sentdex")
  print("HSV Thresholder: https://github.com/saurabheights/IPExperimentTools/blob/master/AnalyzeHSV/hsvThresholder.py")
  print("And the amazing people on Stackoverflow and OpenCV Forums")
  getUserInputAndDoStuff()