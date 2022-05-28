from tkinter import Tk, Label
from tkinter.ttk import Frame, Button, Entry


class Example(Frame):

    def __init__(self):
        super().__init__()
        self._label_to_change = None
        self.entry = None
        self.initUI()

    def calculate(self):
        value = int(self.entry.get())
        _res = "Привет" if value > 7 else 'Введите другое число'
        self._label_to_change.config(text=_res)

    def initUI(self):
        self.master.title("Enter correct value")
        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)
        cls = Button(self, text='Enter', command=self.calculate)
        cls.grid(row=0, column=2)
        lbl = Label(self, text='Number')
        lbl.grid(row=0, column=0)
       # lbl = Label(self, text='The result is:')
       # lbl.grid(row=2, column=0, columnspan=2)
        self._label_to_change = Label(self, text='')
        self._label_to_change.grid(row=1, column=1, columnspan=2)
        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()