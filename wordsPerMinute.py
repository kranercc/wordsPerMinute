import pytesseract
import time
from PIL import Image, ImageEnhance, ImageFilter,ImageGrab
import threading
import pyautogui

time.sleep(1) #delay so you put your cursor on the webpage
def takeSS():
    #coordonates
    xstart = 220
    ystart = 274
    xend = 1171
    yend = 711
    a=ImageGrab.grab([xstart,ystart,xend,yend])
    a.save("text.png")
words = []
def trasnformAndEnhance():
    global words
    im = Image.open("text.png")
    text = pytesseract.image_to_string(Image.open('text.png'))
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save('temp2.jpg')
    text = pytesseract.image_to_string(Image.open('temp2.jpg'))
    for i in text:
        words.append(i)

takeSS()
trasnformAndEnhance()
tracker = 0
while True:
    time.sleep(1/500)
    for i in words:
        pyautogui.write(i)
        tracker +=1
        if tracker >= len(words):
            print("Tracker a ajuns la len cu wards:",tracker)
            print(len(words))
            takeSS()
            trasnformAndEnhance()

#Important
#install tesseract-ocr