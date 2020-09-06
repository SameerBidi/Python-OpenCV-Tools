import os
import cv2

def convertToGrayscale():
  print("")
  folderPath = input("Enter the folder path where images are stored (Make sure there are only images in that folder): ")
  print("")
  for imageName in os.listdir(folderPath):
    image = cv2.imread(f"{folderPath}/{imageName}", cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f"{folderPath}/{imageName}", image)
    print(f"{imageName} converted to grayscale")
  print("\nDone!")