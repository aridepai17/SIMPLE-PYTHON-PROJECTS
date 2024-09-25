import pyautogui 
import time
import matplotlib.pyplot as plt

time.sleep(7)
pyautogui.click()

distance = 250

x, y = [0], [0]

currentx, currenty = 0, 0

while distance > 0:
    currentx += distance
    x.append(currentx)
    y.append(currenty)
    pyautogui.dragRel(distance, 0, duration = 0.1)
    distance -= 5

    currenty += distance
    x.append(currentx)
    y.append(currenty)
    pyautogui.dragRel(0, distance, duration = 0.1)

    currentx -= distance
    x.append(currentx)
    y.append(currenty)
    pyautogui.dragRel(-distance, 0, duration=0.1)
    distance -= 5

    currenty -= distance
    x.append(currentx)
    y.append(currenty)
    pyautogui.dragRel(0, -distance, duration = 0.1)

plt.figure(figsize = (8, 8))
plt.plot(x, y, marker='o')
plt.title('Path of PyAutoGUI Drag')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
