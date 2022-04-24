import datetime
from pygame import mixer

alarm_h = int(input("hr? "))
alarm_m = int(input("min? "))
am_pm = str(input("am/pm? "))
mp3 = 'sample.mp3'
if am_pm == "pm":
    alarm_h = alarm_h + 12

while True:
    if alarm_h == datetime.datetime.now().hour and alarm_m == datetime.datetime.now().minute:
        print("wake up")
        mixer.init()
        mixer.music.load(mp3)
        mixer.music.play()
        status = str(input("Press S To Stop Alarm "))
        if status == "s":
            break
print("exited")
