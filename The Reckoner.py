#################################################################
# Name: Nicholas Derosa
# Date: 02/03/2021
# Description: The Reckoner
#################################################################
from tkinter import *

# the main GUI
class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setupGUI()

    def setupGUI(self):
        self.display = Label(self, text = "", anchor = E, bg = "white", height = 1, font = ("Arial", 50))
        self.display.grid(row = 0, column = 0, columnspan = 4, sticky = E+W+N+S)
        self.pack(fill = BOTH, expand = 1)

        for row in range(7):
            Grid.rowconfigure(self, row, weight = 1)
        for column in range(4):
            Grid.columnconfigure(self, column, weight = 1)
        
        # The first row
        # (
        img = PhotoImage(file = "images/lpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("("))
        button.image = img
        button.grid(row = 1, column = 0, sticky = N+S+E+W)

        # )
        img = PhotoImage(file = "images/rpr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process(")"))
        button.image = img
        button.grid(row = 1, column = 1, sticky = N+S+E+W)

        # AC
        img = PhotoImage(file = "images/clr.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("AC"))
        button.image = img
        button.grid(row = 1, column = 2, sticky = N+S+E+W)

        # bak
        img = PhotoImage(file = "images/bak.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("bak"))
        button.image = img
        button.grid(row = 1, column = 3, sticky = N+S+E+W)

        # The second row
        # 7
        img = PhotoImage(file = "images/7.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("7"))
        button.image = img
        button.grid(row = 2, column = 0, sticky = N+S+E+W)

        # 8
        img = PhotoImage(file = "images/8.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("8"))
        button.image = img
        button.grid(row = 2, column = 1, sticky = N+S+E+W)

        # 9
        img = PhotoImage(file = "images/9.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("9"))
        button.image = img
        button.grid(row = 2, column = 2, sticky = N+S+E+W)

        # div
        img = PhotoImage(file = "images/div.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("/"))
        button.image = img
        button.grid(row = 2, column = 3, sticky = N+S+E+W)

        # The third row
        # 4
        img = PhotoImage(file = "images/4.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("4"))
        button.image = img
        button.grid(row = 3, column = 0, sticky = N+S+E+W)

        # 5
        img = PhotoImage(file = "images/5.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("5"))
        button.image = img
        button.grid(row = 3, column = 1, sticky = N+S+E+W)

        # 6
        img = PhotoImage(file = "images/6.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("6"))
        button.image = img
        button.grid(row = 3, column = 2, sticky = N+S+E+W)

        # mul
        img = PhotoImage(file = "images/mul.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("*"))
        button.image = img
        button.grid(row = 3, column = 3, sticky = N+S+E+W)

        # The fourtn row
        # 1
        img = PhotoImage(file = "images/1.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("1"))
        button.image = img
        button.grid(row = 4, column = 0, sticky = N+S+E+W)

        # 2
        img = PhotoImage(file = "images/2.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("2"))
        button.image = img
        button.grid(row = 4, column = 1, sticky = N+S+E+W)

        # 3
        img = PhotoImage(file = "images/3.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("3"))
        button.image = img
        button.grid(row = 4, column = 2, sticky = N+S+E+W)

        # sub
        img = PhotoImage(file = "images/sub.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("-"))
        button.image = img
        button.grid(row = 4, column = 3, sticky = N+S+E+W)

        # The fifth row
        # 0
        img = PhotoImage(file = "images/0.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("0"))
        button.image = img
        button.grid(row = 5, column = 0, sticky = N+S+E+W)

        # dot
        img = PhotoImage(file = "images/dot.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("."))
        button.image = img
        button.grid(row = 5, column = 1, sticky = N+S+E+W)

        # add
        img = PhotoImage(file = "images/add.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("+"))
        button.image = img
        button.grid(row = 5, column = 3, sticky = N+S+E+W)

        # The sixth row
        # eql-wide
        img = PhotoImage(file = "images/eql-wide.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("="))
        button.image = img
        button.grid(row = 6, columnspan = 2, sticky = N+S+E+W)

        # pow
        img = PhotoImage(file = "images/pow.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("**"))
        button.image = img
        button.grid(row = 6, column = 2, sticky = N+S+E+W)

        # mod
        img = PhotoImage(file = "images/mod.gif")
        button = Button(self, bg = "white", image = img, borderwidth = 0, highlightthickness = 0, activebackground = "white", command = lambda : self.process("%"))
        button.image = img
        button.grid(row = 6, column = 3, sticky = N+S+E+W)

        # pack the GUI
        self.pack(fill = BOTH, expand = 0)

    # Processes button presses
    def process(self, button):
        # AC clears the display
        if(button == "AC"):
            # Clear the display
            self.display["text"] = ""
        elif(button == "bak"):
            st = self.display["text"]
            self.display["text"] = st[:-1]                                
        # = starts an evaluation of whatever is on the diaplay
        elif(button == "="):
            expr = self.display["text"]
            try:
                result = eval(expr)                                   # Fix with help lines 179 - 181 
                self.display["text"] = str(result)[:14]
                if(str(result) >= str(result)[:14]):
                    self.display["text"] = str(result)[:11] + "..."
            except:
                self.display["text"] = "ERROR"
            while(self.display["text"] == str(result)):
                if(button == 0 or button == 1 or button == 2 or button == 3 or button == 4 or button == 5 or button == 6 or button == 7 or button == 8 or button == 9):
                    self.display["text"] = "" + button
        else:
            self.display["text"] += button
            st = self.display["text"]
            self.display["text"] = st[:14]

##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()

