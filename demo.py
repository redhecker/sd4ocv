from cvsd import SD
import cv2

modelPath = 'tindsd'
sd = SD(modelPath)
img = sd.infer("sailing ship")

cvimg = cv2.cvtColor(img[0], cv2.COLOR_BGR2RGB)
cv2.imwrite("output.jpg", cvimg)
print("output.jpg saved")