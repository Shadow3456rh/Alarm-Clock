from tkinter import *
from tkinter import filedialog, messagebox
import datetime
import time
from threading import Thread, Event
import pygame
import ctypes
from tkinter import messagebox as msg


root = Tk()
root.geometry("600x400")
root.resizable(False, False)
root.config(bg="light gray")

def Threading():
    t1 = Thread(target=alarm)
    t1.start()

stop_alarm = Event()
audio_thread = None
selected_audio_file = ""

def browse_audio_file():
    global selected_audio_file
    selected_audio_file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load(selected_audio_file)
    pygame.mixer.music.play()

def stop_audio():
    pygame.mixer.music.stop()

def show_windows_notification(title, message):
    a = ctypes.windll.user32.MessageBoxW(0, message, title, 0x40 | 0x1)
    if a == 1:
        stop_audio()

def alarm():
    msg.showinfo("Success", "Your alarm has successfully been set")
    while True:
        if stop_alarm.is_set():
            stop_alarm.clear()
            if audio_thread and audio_thread.is_alive():
                stop_audio()
            break
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)
        if current_time == set_alarm_time:
            print("Time to Wake up")
            audio_thread = Thread(target=play_audio)
            audio_thread.start()
            show_windows_notification("Alarm", "Time to Wake Up!")

Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red", bg="light gray").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold"), bg="light gray").pack()
frame = Frame(root)
frame.pack()
img = PhotoImage(file=r"D:\Abhishek\Py\Python Project\Project\clock (1).png")
imglabel=Label(root, image=img, bg="light gray").place(x=400, y=30)
imglabel1=Label(root, image=img, bg="light gray").place(x=40, y=30)

hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24')
hour.set(hours[0])
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', 
         '24','25','26','27','28','29','30','31','32','33',
         '34','35','36','37','38','39','40','41','42','43',
         '44','45','46','47','48','49','50','51','52','53',
         '54','55','56','57','58','59','60')


minute.set(minutes[0])
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', 
         '24','25','26','27','28','29','30','31','32','33',
         '34','35','36','37','38','39','40','41','42','43',
         '44','45','46','47','48','49','50','51','52','53',
         '54','55','56','57','58','59','60')


second.set(seconds[0])
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)

set_alarm_button = Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).place(x=190, y=130)

select_audio_button = Button(root, text="Select Audio File", font=("Helvetica 15"), command=browse_audio_file).place(x=300, y=200)

stop_alarm_button = Button(root, text="Stop Alarm", font=("Helvetica 15"), command=stop_alarm.set).place(x=300, y=130)

stop_audio_button = Button(root, text="Stop Music", font=("Helvetica 15"), command=stop_audio).place(x=170, y=200)

root.mainloop()