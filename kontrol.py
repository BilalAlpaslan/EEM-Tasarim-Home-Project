
home = False
try:
    import RPi.GPIO as GPIO
    home = True
except:
    home = False


if home:
    isikPin = 0
    kapiPin = 0
    pencerePin = 0
    klimaPin = 0

    GPIO.cleanup()  # Giriş çıkış pinlerinin verilerini sıfırladık
    GPIO.setmode(GPIO.BCM)  # BCM pin dizilimini seçtik

    GPIO.setup(isikPin, GPIO.OUT)  # Pini çıkış pini olarak tanımladık
    GPIO.setup(kapiPin, GPIO.OUT)
    GPIO.setup(pencerePin, GPIO.OUT)
    GPIO.setup(klimaPin, GPIO.OUT)


class Kontrol:

    @staticmethod
    def isikKontrol(durum: bool):
        # Pini HIGH veya LOW yani lojik 1 veya 0 olmasını amaçladık
        if home:
            GPIO.output(isikPin, durum)
        else:
            print("isik kontrol", durum)

    @staticmethod
    def kapiKontrol(durum: bool):
        if home:
            GPIO.output(kapiPin, durum)
        else:
            print("kapi kontrol", durum)

    @staticmethod
    def pencereKontrol(durum: bool):
        if home:
            GPIO.output(pencerePin, durum)
        else:
            print("pencere kontrol", durum)

    @staticmethod
    def klimaKontrol(durum: bool):
        if home:
            GPIO.output(klimaPin, durum)
        else:
            print("klima kontrol", durum)
