import cv2

def init():
  print("")
  cascadePath = input("Path to cascade xml: ")
  imagePath = input("Path of the image to test: ")
  scaleFactor = float(input("Scale factor: "))
  minNeighbours = int(input("Minimum Neighbours: "))
  print("Minimum Size")
  minw = int(input("Width: "))
  minh = int(input("Height: "))
  print("Maximum Size")
  maxw = int(input("Width: "))
  maxh = int(input("Height: "))
  cascade = cv2.CascadeClassifier(cascadePath)
  image = cv2.imread(imagePath)
  detections = cascade.detectMultiScale(image, scaleFactor=scaleFactor, minNeighbors=minNeighbours, minSize=(minw, minh), maxSize=(maxw, maxh))
  for(x, y, w, h) in detections:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

  cv2.imshow("image", image); cv2.waitKey(0); cv2.destroyAllWindows(); cv2.waitKey(1)