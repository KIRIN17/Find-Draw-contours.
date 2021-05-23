import cv2
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    def nothing(*arg):
        pass

cap = cv2.VideoCapture('test.mp4')  # 0 или путь к файлу так как подключается веб-камера или чтение видео

frameTime = 200

try:
    while True:
        flag, img = cap.read()  # flag - булевское значение,сигнализирующее о прочтении кадра
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow('test', hsv)


        image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)#100 - значение для определенного цвета

        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        image = cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        cv2.imshow('test', image)

        ch = cv2.waitKey(5)
        if ch == 27:
            break


except KeyboardInterrupt:
    print(' Exit pressed Ctrl+C')
    cv2.destroyAllWindows()


