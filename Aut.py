#library
import subprocess, pyautogui,urllib.request, pyperclip, pytesseract, cv2
#path teams
#subprocess.Popen(r'C:\WINDOWS\system32\notepad.exe')
#position mouse and clic
pyautogui.click(800, 20)
#input name funtionary HSN
#pyautogui.typewrite("Recursos Python")
#select funcionary
pyautogui.click(500, 150)
#Input message 
#pyautogui.typewrite("Hola")
#pyautogui.typewrite("buen día")
#press button "enter"
#pyautogui.press("enter")

#--------------- Step 2 -----------------------
#Verify the mail send for HSN

#datos = urllib.request.urlopen('https://www.openwebinars.net')
import cv2
import pytesseract
 


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\vmartinez\AppData\Local\Tesseract-OCR\tesseract.exe'
 
# Read image from which text needs to be extracted
img = cv2.imread("sample4.jpg")
 
# Preprocessing the image starts
 
# Convert the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# Performing OTSU threshold
ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
 
# Specify structure shape and kernel size.
# Kernel size increases or decreases the area
# of the rectangle to be detected.
# A smaller value like (10, 10) will detect
# each word instead of a sentence.
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
 
# Applying dilation on the threshold image
dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
 
# Finding contours
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                 cv2.CHAIN_APPROX_NONE)
 
# Creating a copy of image
im2 = img.copy()
 
# A text file is created and flushed
file = open("recognized.txt", "w+")
file.write("")
file.close()
 
# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
     
    # Drawing a rectangle on copied image
    rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
     
    # Cropping the text block for giving input to OCR
    cropped = im2[y:y + h, x:x + w]
     
    # Open the file in append mode
    file = open("recognized.txt", "a")
     
    # Apply OCR on the cropped image
    text = pytesseract.image_to_string(cropped)
     
    # Appending the text into file
    file.write(text)
    file.write("\n")
     
    
    # Close the file
    file.close


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
ser = Service(r"C:\Users\vmartinez\Downloads\chromedriver_win32 (3)\chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)

#driver = webdriver.Chrome (executable_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# maximize with maximize_window()
s.maximize_window()
s.get("https://www.tutorialspoint.com/index.htm")
# identify element
l=s.find_element_by_css_selector("h4")
# get text and print
print("Text is : " + l.text)



text = pyperclip.paste()

pyperclip.copy(text)
















