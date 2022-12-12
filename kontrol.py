
# import RPi.GPIO as GPIO

class Kontrol:
    isikPin = 0
    kapiPin = 0
    pencerePin = 0
    klimaPin = 0
    
    def isikKontrol(self, durum:bool):
        ...

    def kapiKontrol(self, durum:bool):
        ...

    def pencereKontrol(self, durum:bool):
        ...

    def klimaKontrol(self, durum:bool):
        ...