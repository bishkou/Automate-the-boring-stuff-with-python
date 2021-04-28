import cv2 
import pytesseract
from PIL import Image
import xml.etree.ElementTree as ET
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# img  = cv2.imread('page_1.jpg')

# print(pytesseract.image_to_string(img))

# print(pytesseract.image_to_boxes(Image.open('page_1.jpg')))

# print(pytesseract.image_to_data(Image.open('page_1.jpg')))

# print(pytesseract.image_to_osd(Image.open('page_1.jpg')))

x = pytesseract.image_to_alto_xml('page_1.jpg')
tree = ET.parse(x)
root = tree.getroot()
# ET.fromstring(country_data_as_string)
print(root.tag)
