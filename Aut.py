#library
import subprocess, pyautogui,urllib.request
#path teams
subprocess.Popen(r'C:\WINDOWS\system32\notepad.exe')
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

datos = urllib.request.urlopen('https://www.openwebinars.net')






print (pyautogui.position())
print (datos)

