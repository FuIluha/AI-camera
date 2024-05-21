from ..bridge.bridge import Bridge
import cv2

class Camera:
    def __init__(self, port: str):
        self.board = Bridge(port)
        self.cascade = cv2.CascadeClassifier('data/haarcascade_mcs_upperbody.xml')
 
    def starting_stream(self):
        """Запуск видеопотока с веб-камеры"""
        cap = cv2.VideoCapture(0)
        center_x, center_y = 1000, 500

        while True:
            ret, frame = cap.read()
            if not ret:
                break
 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
            # Детекция головы и плечей
            person_location = self.cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)
 
            # Обводка прямоугольником головы и плечей
            if len(person_location) == 0:
                continue
            (x, y, w, h) = person_location[0]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            avg_x = x + w / 2
            avg_y = y + h / 2

            if center_x + 100 < avg_x or center_x - 100 > avg_x:
                self.board.move_x(avg_x > center_x)

            if center_y + 100 < avg_y or center_y - 100 > avg_y:
                self.board.move_y(avg_y > center_y)

            print("Average coordinates:", avg_x, avg_y)
 
            # Отображение результата
            cv2.imshow('Detected Heads and Shoulders', frame)
 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
 
        cap.release()
        cv2.destroyAllWindows()

n = Camera("/dev/cu.usbserial-110")
n.starting_stream()
