# This Python file uses the following encoding: utf-8
import sys
from threading import Thread

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Signal,QThread
from PySide6.QtGui import QImage,QPixmap

from cv2 import VideoCapture , cvtColor, COLOR_BGR2GRAY , equalizeHist

from numpy import sum,uint8


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from SSG_MOLD_FEATURE.ui_form import Ui_MainWindow
from Algorithm.back_end import template_handler

class data_run(QThread):
    img=Signal(QImage)
    storage = []


    def pre_processing(self,image,store = 10):
        image = equalizeHist(cvtColor(image,
                                            COLOR_BGR2GRAY))
        
        self.storage.append(image)
        if len(self.storage) >= store:
            self.storage.pop(0) 

        return uint8((sum(self.storage,axis=0))/len(self.storage))
      
    def run(self):
        t=0
        cap =VideoCapture(0)
        while(1):
            _,frame=cap.read()
            if _:
                
                frame_n= self.pre_processing(frame)
              
                h, w = frame_n.shape
                q_image = QImage(frame_n, w, h,  QImage.Format_Grayscale8)

                #q_image = QPixmap.fromImage(q_image)
                
                
                
                
                self.img.emit( q_image)

           
            


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.train)
        self.camera = data_run()
        self.camera.img.connect(self.set_image)
        self.ui.pushButton.clicked.connect(self.video_stream)
        
       

    def train(self):
        self.template_handler = template_handler(VideoCapture(0))
        t_handler = Thread(target=self.template_handler.main)
        t_handler.setDaemon(True)
        t_handler.start()

    def set_image(self,img):
        self.ui.graphicsView.clear()
        img = QPixmap(img)
        self.ui.graphicsView.setPixmap(img)

    def video_stream(self):
        self.camera.start()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
