from tkinter import *
from tkcalendar import *
import datetime
import pygame
import time
import winsound
from backend.db import db
from threading import *


#########################################################################################
# Author: Joshua Ellis                                                                  #
# Description: A small, simple alarm clock. I will change the structure and possible    #
# add more functions later.                                                             #
#                                                                                       #
#########################################################################################


root = Tk()
dbase = db() 
pymix = pygame.mixer
pymix.init()
# Set geometry
root.geometry("400x200")
root.title("AlarmClock")
root.geometry("800x850")
root.config(bg="#25467a")
hour_string=''
min_string=''
last_value_sec = ''
last_value = ''
f = ('Times', 20)
 
# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

#stops the alarm could add a snooze function
def stopAlarm():
    pymix.music.stop()

def displayCurTime():    
        string = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        lbl2.config(text = string)
        lbl2.after(1000, displayCurTime)

#plays alarm until stopped
def playSound():
    pymix.music.load("./backend/sounds/Alarm-Slow-B1-www.fesliyanstudios.com.mp3")
    pymix.music.play(-1)
    return

def alarm():
    # Infinite Loop
    cal_date = cal.get_date()
    hour = hour_sb.get()
    mins = sec_hour.get()
    secs = sec.get()
    
   
    userTime = hour + ':' + mins + ':' + secs
    datime = cal_date + ' ' + userTime
    dbase.addAlarm(datime)
    while True:
        # Set Alarm
        alarmlist_raw = dbase.getAlarms()
        alarmlist = [i[0] for i in alarmlist_raw]
        for dTime in alarmlist:

 
            time.sleep(1)
    
            # Get current time
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Check whether set alarm is equal to current time or not
            if current_time ==  dTime:
                dbase.deleteAlarm(dTime) # could be put in another function if snooze function is added
                playSound()      
                
                
# Add Labels, Frame, Button, Optionmenus


root.title("AlarmClock")
root.geometry("800x850")
root.config(bg="#25467a")
lbl1 = Label(root, font=('calibri', 40, 'bold'),
    background= '#25467a',
    foreground= 'white')
lbl2 = Label(root, font=('calibri', 30, 'bold'),
    background= '#25467a',
    foreground= 'white')
lbl1.pack(anchor='center')
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
lbl3 = Label(root, font=('calibri', 30, 'bold'),
    background='#25467a',
    foreground='white')
lbl4 = Label(root, font=('calibri', 15, 'bold'), background='#25467a', foreground= 'white')
lbl4.place(relx=0.5, rely=0.7, anchor='center')
lbl3.place(relx=0.5, rely=0.25, anchor='center')
lbl2.place(relx=0.5, rely=0.18, anchor='center')
lbl3.config(text="Choose date and time")
lbl1.config(text="Alarm Clock")
hour_sb = Spinbox(
    root,
    from_=00,
    to=23,
    wrap=True,
    textvariable=hour_string,
    width=3,
    state="readonly",
    font=f,
    format="%02.0f",
    justify=CENTER
)
sec_hour = Spinbox(
    root,
    from_=00,
    to=59,
    wrap=True,
    textvariable=min_string,
    font=f,
    format="%02.0f",
    width=3,
    justify=CENTER
)

sec = Spinbox(
    root,
    from_=00,
    to=59,
    wrap=True,
    textvariable=sec_hour,
    width=3,
    font=f,
    format="%02.0f",
    justify=CENTER
)
displayCurTime()
cal.place(relx=0.5, rely=0.4, anchor='center')
hour_sb.place(relx=0.4, rely=0.55, anchor='center')
sec_hour.place(relx=0.5, rely=0.55, anchor='center')
sec.place(relx=0.6, rely=0.55, anchor='center') 

button = Button(root, text="Set Alarm", command=Threading)
button.place(relx=0.45, rely=0.6, anchor='center')
stopButton = Button(root, text="Stop Alarm", command=stopAlarm)
stopButton.place(relx=0.59, rely=0.6, anchor='center')
 
# Execute Tkinter
root.mainloop()