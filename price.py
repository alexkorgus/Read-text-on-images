import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('price.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img, lang='rus'))
