import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

dict = {}

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.button1 = tk.Button(self, text="input", command=lambda: self.add(self.row, dict))
        self.button1.grid(columnspan = 2)
        self.button2 = tk.Button(self, text="Start",
                            command=lambda: controller.show_frame("PageOne"))
        self.button2.grid(columnspan = 2)
        label_q = tk.Label(self, text="Question")
        label_a = tk.Label(self, text="Answer")
        label_q.grid(row=2, column=0, sticky=tk.W)
        label_a.grid(row=2, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)

        self.row = 3

        self.e1.grid(row=self.row, column=0)
        self.e2.grid(row=self.row, column=1)

    def add(self, row, dict, event=None):
        q_val = self.e1.get()
        a_val = self.e2.get()
        dict[q_val] = a_val
        self.e1.destroy()
        self.e2.destroy()
        tk.Label(self.parent, text=q_val).grid(row=self.row, column=0, sticky=tk.W)
        tk.Label(self.parent, text=a_val).grid(row=self.row, column=1, sticky=tk.W)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e1.grid(row=self.row, column=0)
        self.e2.grid(row=self.row, column=1)
        self.row += 1


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent
        self.msg = tk.Message(self, text='')

        self.button1 = tk.Button(self, text="I give up",
                           command=lambda: self.give_up())
        self.button2 = tk.Button(self, text="End", command=lambda: self.end())
        self.button1.pack()
        self.button2.pack()
        self.display("test")

    def display(self, string):
        self.msg = tk.Message(self, text=string)

    def give_up(self):





if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
