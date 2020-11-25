from tkinter import *
from create_db import *
from calculatorView import *
from homeworkView import *


class MainView():
    def __init__(self, master, frame):
        self.master = master
        self.master.geometry("400x100")
        self.frame = frame
        self.frame.pack()
        self.master.title("Tolerans")

        self.l1 = Label(frame, text="Ne yapmak istiyorsunuz?",
                        font=('Times', 15, 'bold'))
        self.toleransHesabı = Button(frame,
                                     text="Tolerans Hesabı",
                                     command=self.openCalculator)
        self.toleransOdevi = Button(frame,
                                    text="Tolerans Ödevi",
                                    command=self.openOdev)

        self.l1.grid(row=0, column=0, sticky='', pady=2)
        self.toleransHesabı.grid(row=1, column=0, sticky='', pady=2)
        self.toleransOdevi.grid(row=2, column=0, sticky='', pady=2)

    def openCalculator(self):
        window = Toplevel(self.master)
        frame = Frame(window)
        calculator = CalculatorView(window, frame)

    def openOdev(self):
        window = Toplevel(self.master)
        frame = Frame(window)
        calculator = HomeworkView(window, frame)


root = Tk()
frame = Frame(root)
my_gui = MainView(root, frame)
root.mainloop()
