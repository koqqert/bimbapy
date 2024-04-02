from customtkinter import *

class MyRadiobuttonFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = CTkLabel(self, text="Радиокнопки")
        self.radio_button1 = CTkRadioButton(self, text="Кнопка 1")
        self.radio_button2 = CTkRadioButton(self, text="Кнопка 2")
        self.radio_button3 = CTkRadioButton(self, text="Кнопка 3")
        
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='nswe')
        self.radio_button1.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
        self.radio_button2.grid(row=2, column=0, padx=10, pady=10, sticky='nswe')
        self.radio_button3.grid(row=3, column=0, padx=10, pady=10, sticky='nswe')

class App(CTk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Радиокнопки")
        self.radiobutton_frame = MyRadiobuttonFrame(self)
        self.radiobutton_frame.grid(row=0, column=0, padx=10, pady=10)

app = App()
app.mainloop()