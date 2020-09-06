import cv2
import os
import subprocess

def createPosList(path):
  posPath = f"{path}/pos"
  for imageName in os.listdir(posPath):
    image = cv2.imread(f"{posPath}/{imageName}")
    h, w, _ = image.shape
    line = f"pos\\{imageName} 1 0 0 {w} {h}\n"
    with open(f"{path}/pos.lst", "a") as file:
      file.write(line)

def createNegList(path):
  negPath = f"{path}/neg"
  for imageName in os.listdir(negPath):
    line = f"{negPath}\\{imageName}\n"
    with open(f"{path}/neg.lst", "a") as file:
      file.write(line)

def deleteFile(filePath):
  try:
    os.remove(filePath)
  except OSError:
    pass

def createSamples(path, width, height):
  infoPath = f"{path}/pos.lst".replace("/", os.sep)
  vecPath = f"{path}/positives.vec".replace("/", os.sep)
  num = len(os.listdir(f'{path}/pos'))

  print(f"\nCommand:\nopencv_createsamples -info {infoPath} -num {num} -vec {vecPath} -w {width} -h {height}\n")
  subprocess.call(f"opencv_createsamples -info {infoPath} -num {num} -vec {vecPath} -w {width} -h {height}", shell=True)
  print("\nDone: Create Samples")

def trainCascade(path, numPos, numNeg, width, height, numStages):
  vecPath = f"{path}/positives.vec".replace("/", os.sep)
  bgPath = f"{path}/neg.lst".replace("/", os.sep)
  trainFolder = f"{path}/trained_data".replace("/", os.sep)

  if not os.path.exists(trainFolder):
    os.makedirs(trainFolder)

  print(f"\nCommand:\nopencv_traincascade -data {trainFolder} -vec {vecPath} -bg {bgPath} -numPos {numPos} -numNeg {numNeg} -numStages {numStages} -w {width} -h {height}\n")
  subprocess.call(f"opencv_traincascade -data {trainFolder} -vec {vecPath} -bg {bgPath} -numPos {numPos} -numNeg {numNeg} -numStages {numStages} -w {width} -h {height}", shell=True)
  print("\nDone: Train Cascade")

def init():
  print("\nPlace your positive and negative images in their own folder named pos and neg")
  print("Place these two folders in a separate folder call it anything")
  print("")
  folderPath = input("Parent folder path of pos and neg: ")
  numPos = int(input("Number of positive samples to use: "))
  numNeg = int(input("Number of negative samples to use: "))
  width = int(input("Training Width: "))
  height = int(input("Training Height: "))
  numStages = int(input("Number of Stages: "))
  deleteFile(f"{folderPath}/pos.lst")
  deleteFile(f"{folderPath}/neg.lst")
  deleteFile(f"{folderPath}/positives.vec")
  print("\nCreating Positives list")
  createPosList(folderPath)
  print("\nCreating Negatives list")
  createNegList(folderPath)
  print("\nCreating samples...")
  createSamples(folderPath, width, height)
  print("\nTraining Cascade...")
  trainCascade(folderPath, numPos, numNeg, width, height, numStages)