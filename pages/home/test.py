from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

import cv2

import handTrackingModule as htm

class CamApp(App):

    def build(self):
        self.img1=Image()
        layout = BoxLayout()
        layout.add_widget(self.img1)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        # cv2.namedWindow("CV2 Image")

        self.detector = htm.handDetector(detectionCon=0.7)

        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, img = self.capture.read()
        # cv2.imshow("CV2 Image", img)

        img = self.detector.findHands(img)
        lmList = self.detector.findPosition(img)
        # convert it to texture
        buf1 = cv2.flip(img, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        #if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()