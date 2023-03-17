import cv2
import numpy as np
import pyautogui
from time import sleep

pixel = cv2.imread('pixel_satan.png')

largura = 500
altura = 340
campos = [[426, 221], [423, 157]]
cont = 0

instance = [[665, 255], [659, 294]]

while True:
    cont += 1
    for campo in campos:
        pyautogui.moveTo(campo[0], campo[1])
        image = pyautogui.screenshot(region=(0, 30, largura, altura))

        tela = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        cv2.imwrite("tela.png", tela)

        tela = cv2.imread('tela.png')
        result = cv2.matchTemplate(tela, pixel, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_loc[0] == 59 and max_loc[1] == 7:
            # print(max_val, max_loc)
            pyautogui.click(campo[0], campo[1])
            cont = 0
            sleep(8)

    if cont >= 5:
        pyautogui.moveTo(instance[0][0], instance[0][1])
        sleep(1)
        pyautogui.rightClick(instance[0][0], instance[0][1])
        sleep(1)
        pyautogui.moveTo(instance[1][0], instance[1][1])
        sleep(1)
        pyautogui.click(instance[1][0], instance[1][1])
        sleep(3)

    sleep(1)

# sleep(2)
# print(pyautogui.position())
# sleep(2)
# print(pyautogui.position())
