from tkinter import *
from time import sleep

class Dialogue:
    def __init__(self, scenario, image):
        self.scenario = scenario
        self.image = image
        self.prompts = {}

    @property
    def scenario(self):
        return self._scenario

    @scenario.setter
    def scenario(self, value):
        self._scenario = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def prompts(self):
        return self._prompts

    @prompts.setter
    def prompts(self, value):
        self._prompts = value

    def addPrompt(self, prompt, scenario):
        self._prompts[prompt] = scenario

class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)

        # player input (temporary, to be removed or changed in favor of GPIO)
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # image, to be changed to top side and expanded on x-axis
        # Height will be // by 1.5
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # text, to be changed to bottom side and expanded on x-axis
        # Height will be // by 2.5
        text_frame = Frame(self, width=WIDTH // 2)
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    def createScenario(self):
        s1 = Dialogue("p1", "placeholder.gif")
        s2 = Dialogue("p2", "placeholder2.gif")
        s3 = Dialogue("p3", "placeholder3.gif")
        s4 = Dialogue("p4", "placeholder4.gif")
        s5 = Dialogue("p5", "placeholder5.gif")

        s1.addPrompt("p2", s2)
        s1.addPrompt("p3", s3)
        s1.addPrompt("p4", s4)
        s2.addPrompt("p5", s5)
        s3.addPrompt("p5", s5)
        s4.addPrompt("p5", s5)
        
        Game.currentScenario = s1

    def setScenarioImage(self):
        Game.img = PhotoImage(file=Game.currentScenario.image)
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    def setResponse(self, response):
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.text.insert(END, response)
        Game.text.config(state=DISABLED)

    def play(self):
        self.createScenario()
        self.setupGUI()
        self.setScenarioImage()
        self.setResponse("Begin with Enter")

    def process(self, event):
        global firstRun
        global finalRun
        global completedRun
        global LL
        if firstRun == True:
            response, LL = dialogueSearch("start")
            self.setResponse(response)
            self.setScenarioImage()
            firstRun = False
        elif finalRun == True:
            if completedRun == True:
                Game.player_input.delete(0, END)
            else:
                userIn = Game.player_input.get()
                index = userInput(userIn, LL)
                if index == 0:
                    response = "Error: Invalid Input"
                    self.setResponse(response)
                    completedRun = True
                else:
                    response, changeScenario = dialogueSearch(index)
                    self.setResponse(response)
                    if(changeScenario in Game.currentScenario.prompts):
                        Game.currentScenario = Game.currentScenario.prompts[changeScenario]
                    self.setScenarioImage()
                    Game.player_input.delete(0, END)
                    completedRun = True
        else:
            userIn = Game.player_input.get()
            index = userInput(userIn, LL)
            if index == 0:
                response = "Error: Invalid Input"
                self.setResponse(response)
                completedRun = True
            else:
                response, LL, changeScenario = dialogueSearch(index)
                self.setResponse(response)
                if(changeScenario in Game.currentScenario.prompts):
                    Game.currentScenario = Game.currentScenario.prompts[changeScenario]
                self.setScenarioImage()
                Game.player_input.delete(0, END)
        

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append_item(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.count += 1

    def __getitem__(self, index):
        if index > self.count - 1:
            return "Error: Index out of range"
        current_val = self.tail
        for n in range(index):
            current_val = current_val.next
        return current_val.data

# test (start) (s1)
# prompt1 (p1)
#  - response1 (r1)
#       promt2 (p2) (s2)
#        - response4 (r4)
#           answer1
#        - response5 (r5)
#           answer2
#        - response6 (r6)
#           answer3
#  - response2 (r2)
#       promt3 (p3) (s3)
#        - response7 (r7)
#           answer4
#        - response8 (r8)
#           answer5
#  - response3 (r3)
#       promt4(p4) (s4)
#        - response9 (r9)
#           answer6
#        - response10 (r10)
#           answer7
#        - response11 (r11)
#           answer8


def dialogueSearch(index):
    global finalRun
    global TwoPrompt
    global LL
    if index == "start":
        a = LinkedList()
        response = ("test" \
              "\nprompt" \
              "\n - response1" \
              "\n - response2" \
              "\n - response3")
        a.append_item("r1")
        a.append_item("r2")
        a.append_item("r3")
        LL = a
        return response, LL
    if index == "r1":
        b = LinkedList()
        response = ("promt2" \
              "\n - response4" \
              "\n - response5" \
              "\n - response6")
        b.append_item("r4")
        b.append_item("r5")
        b.append_item("r6")
        LL = b
        currentScenario = "p2"
        finalRun = True
        return response, LL, currentScenario
    if index == "r2":
        c = LinkedList()
        response = ("promt3" \
              "\n - response7" \
              "\n - response8")
        c.append_item("r7")
        c.append_item("r8")
        TwoPrompt = True
        LL = c
        currentScenario = "p3"
        finalRun = True
        return response, LL, currentScenario
    if index == "r3":
        d = LinkedList()
        response = ("prompt4" \
              "\n - response9" \
              "\n - response10" \
              "\n - response11")
        d.append_item("r9")
        d.append_item("r10")
        d.append_item("r11")
        LL = d
        currentScenario = "p4"
        finalRun = True
        return response, LL, currentScenario
    if index == "r4":
        response = "answer1"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r5":
        response = "answer2"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r6":
        response = "answer3"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r7":
        response = "answer4"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r8":
        response = "answer5"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r9":
        response = "answer6"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r10":
        response = "answer7"
        currentScenario = "p5"
        return response, currentScenario
    if index == "r11":
        response = "answer8"
        currentScenario = "p5"
        return response, currentScenario

def userInput(userIn, LL):
    global TwoPrompt
    if userIn == "1":
        index = LL[0]
        return index
    elif userIn == "2":
        index = LL[1]
        return index
    elif(userIn == "3" and TwoPrompt != True):
        index = LL[2]
        return index
    else:
        index = 0
        return index

######################################################
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("DS^2")

firstRun = True
finalRun = False
completedRun = False
TwoPrompt = False
g = Game(window)
g.play()

window.mainloop()

