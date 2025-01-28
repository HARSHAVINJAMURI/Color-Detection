import cv2
import numpy as np
import pandas as pd
from tkinter import Tk
from tkinter.filedialog import askopenfilename
def getColorName(R, G, B):
    minimum = 10000
    cname = "Unknown"
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
print("Please select an image to analyze.")
Tk().withdraw()
file_path = askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
if not file_path:
    print("No file selected. Exiting!")
    exit()
img = cv2.imread(file_path)
if img is None:
    print("Error: Unable to read the selected image. Exiting!")
    exit()
clicked = False
r = g = b = xpos = ypos = 0
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)
if csv.empty:
    print("Error: colors.csv file is empty or not loaded correctly!")
    exit()
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        clicked = False
    key = cv2.waitKey(1) & 0xFF
    if key == 27 or cv2.getWindowProperty('image', cv2.WND_PROP_VISIBLE) < 1:
        break
cv2.destroyAllWindows()