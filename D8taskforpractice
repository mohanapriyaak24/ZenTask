
#find leap year
def IsleapYear(y):
    if y%400==0 and y%100!=0 or y%4==0:
        print(1)
    else:
        print(0)

year = int(input())
IsleapYear(year)

# Reverse a string
def ReverseString(str):
    reversedstring = str[::-1]
    print(reversedstring)
    print(type(reversedstring))
string = input()
ReverseString(string)

# movie

class movie:
    def __init__(self,title,studio,rating="PG"):
        self.title = title
        self.studio = studio
        self.rating = rating

    def myfunc(self):
        print(f"The Title {self.title}, the Studio{self.studio}, and the Rating {self.rating}")


film1 = movie("Casino Royale","Eon Productions","PG13")
film2 = movie("youth","CKK")

film1.myfunc()
film2.myfunc()



#Tv class

class Tvclass:
    def __init__(self,brand,Inch,price,Onoff,channel= 1,volume =50):
        self.brand = brand
        self.Inch = Inch
        self.price = price
        self.Onoff = Onoff
        self.channel = channel
        self.volume = volume

    def Increasevolume(self):
        if self.volume < 100:
            self.volume += 1

    def Decreasevolume(self):
        if self.volume > 0:
            self.volume -= 1

    def channelnum(self):
        if self.channel < 1 and self.channel > 50:
            self.channel == self.channel

    def resetTv(self):
        self.channel = 1
        self.volume =50
    
    def currentstatus(self):
        print(f"\nPanasonic at channel {self.channel}, volume {self.volume}")

class LedTv(Tvclass):
    def __init__(self, brand, Inch, price, Onoff,screenthickness, energyusage , lifespan , Refreshrate ,  viewingAngle , Backlight ,  channel=1, volume=50):
        super().__init__(brand, Inch, price, Onoff, channel, volume)
        self.screenthickness =screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.Refreshrate = Refreshrate
        self.viewingangle= viewingAngle
        self.backlight = Backlight
        


    def featuresOfLedTv(self):
        print(f"\nDisplayFeatures are\n screenthickness: {self.screenthickness}\n Energyusage: {self.energyusage}\n Lifespan: {self.lifespan}\n Refresh rate: {self.Refreshrate}\n viewingangle: {self.viewingangle}\n Backlight: {self.backlight}")

    
class plasma(Tvclass):
    def __init__(self, brand, Inch, price, Onoff,screenthickness, energyusage , lifespan , Refreshrate ,  viewingAngle , Backlight,channel=1, volume=50):
        super().__init__(brand, Inch, price, Onoff, channel, volume)
        self.screenthickness =screenthickness
        self.energyusage = energyusage
        self.lifespan = lifespan
        self.Refreshrate = Refreshrate
        self.viewingangle= viewingAngle
        self.backlight = Backlight
    


    def featuresOfplasmaTv(self):
        print(f"\nDisplayFeatures are\n screenthickness: {self.screenthickness}\n Energyusage: {self.energyusage}\n Lifespan: {self.lifespan}\n Refresh rate: {self.Refreshrate}\n viewingangle: {self.viewingangle}\n Backlight: {self.backlight}")



Tvplasma=plasma("samsung",48,80000,"on","7cm","70 watts","20+years","60HZ","40 degrees from left to right","plasma Strip Lights")
TvLed=LedTv("oneplus",64,100000,"on","5cm","100 watts","25+years","80HZ","45 degrees from left to right","LED Strip Lights")
tv= Tvclass("sony",64,60000,"on",23,68)
Tvplasma.featuresOfplasmaTv()
TvLed.featuresOfLedTv()
tv.resetTv()
tv.currentstatus()

