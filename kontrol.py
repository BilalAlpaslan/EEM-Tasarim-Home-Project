
# import RPi.GPIO as GPIO

class Kontrol:
    GPIO.cleanup() # Giriş çıkış pinlerinin verilerini sıfırladık
    GPIO.setmode(GPIO.BCM) #BCM pin dizilimini seçtik
    isikPin = 0
    kapiPin = 0
    pencerePin = 0
    klimaPin = 0
    GPIO.setup(isikPin, GPIO.OUT)# Pini çıkış pini olarak tanımladık
    GPIO.setup(kapiPin, GPIO.OUT)
    GPIO.setup(pencerePin, GPIO.OUT)
    GPIO.setup(klimaPin, GPIO.OUT)
    def isikKontrol(self, durum:bool):
        GPIO.output(self.isikPin,durum)# Pini HIGH veya LOW yani lojik 1 veya 0 olmasını amaçladık
    def kapiKontrol(self, durum:bool):
        GPIO.output(self.kapiPin,durum)
    def pencereKontrol(self, durum:bool):
        GPIO.output(self.pencerePin,durum)
    def klimaKontrol(self, durum:bool):
        GPIO.output(self.klimaPin,durum)
