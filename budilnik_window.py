from datetime import datetime
from playsound import playsound
from time import *
from tkinter import *
import threading

#код для будильника
def cancel_alarm():
    label_2.configure(text='---Будильник удален')
    label_3.configure(text='')
    label_4.configure(text='')
def validate_and_set_alarm():
    def validate_time(alarm_time):
        if len(alarm_time) != 8:
            return "введено неверно"
        else:
            if int(alarm_time[0:2]) < 24 and int(alarm_time[3:5]) < 60 and int(alarm_time[7:8]) < 60:
                return 'введено верно!'

    alarm_time = entry.get()
    entry.delete(0, END)
    validate = validate_time(alarm_time)
    if validate == 'введено верно!':
        label_2.configure(text=f'---Будильник установлен на {alarm_time}')
        label_3.configure(text=f'---Ждите!')
    alarm_hour = int(alarm_time[0:2])
    alarm_min = int(alarm_time[3:5])
    alarm_sec = int(alarm_time[7:8])
    threading.Thread(target=check_alarm, args=(alarm_hour, alarm_min, alarm_sec)).start()
def check_alarm(alarm_hour, alarm_min, alarm_sec):
    while True:
        now = datetime.now()
        current_hour = now.hour
        current_min = now.minute
        current_sec = now.second
        if alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec:
            label_4.configure(text='---Подъём!')
            playsound('C:\\Users\\User\\.vscode\\extensions\\bimbapy\\alarm.mp3')
            break
#код для окна
window = Tk()
window.title("Будильник")
window.geometry('500x300')
window.configure(bg='gray38')
entry = Entry(bg='gray85')
entry.place(anchor='center', relx=0.5, rely=0.40, relwidth=0.43, relheight=0.1)

btn = Button(text="Активировать будильник", bg='gray85', command=validate_and_set_alarm)
btn.pack()
btn.place(anchor='c', relx=0.5, rely=0.5, relwidth=0.36, relheight=0.1)

cancel_btn = Button(text="Удалить будильник", bg='gray85', command=cancel_alarm)
cancel_btn.pack()
cancel_btn.place(anchor='e', relx=1, rely=0.8, relwidth=0.36, relheight=0.1)

label_1 = Label(text="Время будильника в формате ЧЧ:ММ:СС", bg='gray38', font=('Arial Black', 11))
label_1.place(anchor='center', relx=0.5, rely=0.30, relwidth=0.7, relheight=0.1)

label_2 = Label(bg='gray38') #85
label_2.place(anchor='w', relx=0, rely=0.60)

label_3 = Label(bg='gray38')
label_3.place(anchor='w', relx=0, rely=0.66) 

label_4 = Label(bg='gray38')
label_4.place(anchor='w', relx=0, rely=0.72)

window.mainloop()