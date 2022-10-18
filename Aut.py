#library
import subprocess, pyautogui
#path teams
subprocess.Popen(r'C:\WINDOWS\system32\notepad.exe')
#position mouse and clic
pyautogui.click(800, 20, 3)
#input name funtionary HSN
pyautogui.typewrite("Recursos Python")


print (pyautogui.position())


