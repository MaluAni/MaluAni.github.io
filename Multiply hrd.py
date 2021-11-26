import tkinter as Chat
import random
import time


LARGE_FONT = ("Minion Pro Med", 24)
NORMAL_FONT = ("Minion Pro Med", 18)
SMALL_FONT = ("Minion Pro Med", 12)

class StartFrame(Chat.Tk):
    def __init__(self, *args, **kwargs):
        Chat.Tk.__init__(self, *args, **kwargs)
        container = Chat.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        # frame loop
        for F in (MainPage, ):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MainPage)

    # using tkraise() to show the frame
    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()

class MainPage(Chat.Frame):
    def __init__(self, parent, controller):
        Chat.Frame.__init__(self, parent)
        frame = Chat.Frame(self)

        now = time.time()
        global First
        global Second
        global counterCorrect
        global counterWrong
        first = First[random.randint(0, len(First) - 1)]
        second = Second[random.randint(0, len(Second) - 1)]
        result = first * second
        def CheckAnswer(event=None):
            global counterCorrect
            global counterWrong
            global timeCounter
            global sec
            global points
            sec = time.time() - now
            if int(typebox.get()) == result:
                label = Chat.Label(self, text="Correct in " + str(int(sec)) + " seconds", font=LARGE_FONT)
                label.place(x=300, y=200)
                counterCorrect += 1
                if sec < 6:
                    points += 30 - sec
                else:
                    points = points
            else:
                label = Chat.Label(self, text="Wrong in " + str(int(sec)) + " seconds", font=LARGE_FONT)
                label.place(x=300, y=200)
                counterWrong += 1
            timeCounter += int(sec)

        def Again(event=None):
            global app
            global sec
            app.destroy()
            sec = 0
            app = StartFrame()
            app.title("Multiply Game")
            app.geometry("650x440")
            app.resizable(width=False, height=False)
            app.focus_force()
            app.mainloop()
            
        
        label = Chat.Label(self, text="How much is " + str(first) + " times " + str(second) + " ?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        label = Chat.Label(self, text=str(first) + " X " + str(second) + " = ", font=LARGE_FONT)
        label.place(x=150, y=100)
        typedmessage = Chat.StringVar()
        typebox = Chat.Entry(self, text=typedmessage, font=LARGE_FONT)
        typebox.focus_set()
        typebox.place(x=315, y=100, width=60)
        typebox.bind('<Return>', CheckAnswer)
        typebox.bind('<+>', Again)
        button = Chat.Button(self, text="Check", font=NORMAL_FONT,
                             command=CheckAnswer)
        
        button.pack(pady=10, padx=10)
        button.place(x=300, y=150)
        button = Chat.Button(self, text="Again?", font=NORMAL_FONT,
                             command=Again)
        button.pack(pady=10, padx=10)
        button.place(x=300, y=250)
        
        label = Chat.Label(self, text="Correct Answers:  " + str(counterCorrect), font=NORMAL_FONT)
        label.pack(pady=10, padx=10)
        label.place(x=100, y=300)
        label = Chat.Label(self, text="Wrong Answers:  " + str(counterWrong), font=NORMAL_FONT)
        label.pack(pady=10, padx=10)
        label.place(x=100, y=350)
        label = Chat.Label(self, text="Time:  " + str(timeCounter) + "seconds" +"\nPoints: " + str(int(points))  , font=SMALL_FONT)
        label.pack(pady=10, padx=10)
        label.place(x=100, y=400)
        button = Chat.Button(self, text="Exit", font=NORMAL_FONT,
                             command=lambda: app.destroy())
        button.pack(pady=10, padx=10, side=Chat.RIGHT)
        button.place(x=580, y=393)
        

First = [3, 4, 6, 7, 8, 9, 11, 12]
Second = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
counterCorrect = 0
counterWrong = 0
timeCounter = 0
sec = 0
points = 0
app = StartFrame()
app.title("Multiply Game")
app.geometry("650x440")
app.resizable(width=False, height=False)
app.mainloop()
