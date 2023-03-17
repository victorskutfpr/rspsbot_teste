import cv2
import numpy as np
import pyautogui
from time import sleep

pixel = cv2.imread('letra.png')

largura = 500
altura = 340

while True:
    #     # get random value step 50
    x = np.random.randint(0, 500, 1)
    # if (x+75 > 500):
    #     x = x-75
    # else:
    #     x = x+75
    y = np.random.randint(0, 340, 1)
    # if (y+75 > 340):
    #     y = y-75
    # else:
    #     y = y+75

    pyautogui.moveTo(x, y)
    image = pyautogui.screenshot(region=(0, 30, largura, altura))

    tela = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

#     # # writing it to the disk using opencv
    cv2.imwrite("tela.png", tela)

    tela = cv2.imread('tela.png')
#     # # cv2.imshow('image', tela)
#     # # cv2.waitKey()
#     # # cv2.destroyAllWindows()

#     # # cv2.imshow('pixel', pixel)
#     # # cv2.waitKey()
#     # # cv2.destroyAllWindows()

#     # # cv2.imshow('tela', tela)
#     # # cv2.waitKey()
#     # # cv2.destroyAllWindows()
    result = cv2.matchTemplate(tela, pixel, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val > 0.68:
        print(max_val, max_loc)
        pyautogui.click(x, y)
        sleep(2)

# # print(max_val, max_loc)

# # cv2.imshow('result', result)
# # cv2.waitKey()
# # cv2.destroyAllWindows()

# # create rectangle
# # top_left = max_loc
# # bottom_right = (top_left[0] + 50, top_left[1] + 50)
# # cv2.rectangle(tela, top_left, bottom_right, 255, 2)

# # cv2.imshow('tela', tela)
# # cv2.waitKey()
# # cv2.destroyAllWindows()

# # get mouse position
# # sleep(2)
# # print(pyautogui.position())
