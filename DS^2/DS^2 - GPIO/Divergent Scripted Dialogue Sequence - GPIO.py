from tkinter import *
import RPi.GPIO as GPIO
from pygame import mixer

mixer.init()

buttonConfirm = 18
button1 = 19
button2 = 20
button3 = 21
button4 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonConfirm, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
        Game.player_input = Entry(self, bg="white", width=WIDTH // 500)
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=RIGHT)
        Game.player_input.focus()

        img = None
        Game.image = Label(self, height=int(HEIGHT // 1.25), image=img)
        Game.image.image = img
        Game.image.pack(side=TOP, fill=X)
        Game.image.pack_propagate(False)

        text_frame = Frame(self, height=int(HEIGHT // 3))
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=X, expand=1)
        text_frame.pack(side=BOTTOM, fill=X)
        text_frame.pack_propagate(False)

    def createScenario(self):
        s1 = Dialogue("entrance", "entrance.gif")
        s2 = Dialogue("leavePositive", "leavePositive.gif")
        s3 = Dialogue("leaveNegative", "leaveNegative.gif")
        s4 = Dialogue("neutral1", "neutral1.gif")
        s5 = Dialogue("neutral2", "neutral2.gif")
        s6 = Dialogue("neutral3", "neutral3.gif")
        s7 = Dialogue("positive1", "positive1.gif")
        s8 = Dialogue("positive2", "positive2.gif")
        s9 = Dialogue("positive3", "positive3.gif")
        s10 = Dialogue("negative1", "negative1.gif")
        s11 = Dialogue("negative2", "negative2.gif")
        s12 = Dialogue("negative3", "negative3.gif")
        s13 = Dialogue("endBest", "endBest.gif")
        s14 = Dialogue("endGood", "endGood.gif")
        s15 = Dialogue("endNeutral", "endNeutral.gif")
        s16 = Dialogue("endBad", "endBad.gif")
        s17 = Dialogue("endWorst", "endWorst.gif")
        s18 = Dialogue("endLoop", "endLoop.gif")
        s19 = Dialogue("blank", "blank.gif")

        s1.addPrompt("neutral1", s4)
        s1.addPrompt("neutral2", s5)
        s1.addPrompt("neutral3", s6)
        s1.addPrompt("positive1", s7)
        s1.addPrompt("positive2", s8)
        s1.addPrompt("positive3", s9)
        s1.addPrompt("negative1", s10)
        s1.addPrompt("negative2", s11)
        s1.addPrompt("negative3", s12)
        s2.addPrompt("endBest", s13)
        s2.addPrompt("endGood", s14)
        s2.addPrompt("endNeutral", s15)
        s2.addPrompt("endBad", s16)
        s2.addPrompt("endWorst", s17)
        s2.addPrompt("endLoop", s18)
        s3.addPrompt("endBest", s13)
        s3.addPrompt("endGood", s14)
        s3.addPrompt("endNeutral", s15)
        s3.addPrompt("endBad", s16)
        s3.addPrompt("endWorst", s17)
        s3.addPrompt("endLoop", s18)
        s4.addPrompt("leavePositive", s2)
        s4.addPrompt("leaveNegative", s3)
        s4.addPrompt("neutral1", s4)
        s4.addPrompt("neutral2", s5)
        s4.addPrompt("neutral3", s6)
        s4.addPrompt("positive1", s7)
        s4.addPrompt("positive2", s8)
        s4.addPrompt("positive3", s9)
        s4.addPrompt("negative1", s10)
        s4.addPrompt("negative2", s11)
        s4.addPrompt("negative3", s12)
        s5.addPrompt("leavePositive", s2)
        s5.addPrompt("leaveNegative", s3)
        s5.addPrompt("neutral1", s4)
        s5.addPrompt("neutral2", s5)
        s5.addPrompt("neutral3", s6)
        s5.addPrompt("positive1", s7)
        s5.addPrompt("positive2", s8)
        s5.addPrompt("positive3", s9)
        s5.addPrompt("negative1", s10)
        s5.addPrompt("negative2", s11)
        s5.addPrompt("negative3", s12)
        s6.addPrompt("leavePositive", s2)
        s6.addPrompt("leaveNegative", s3)
        s6.addPrompt("neutral1", s4)
        s6.addPrompt("neutral2", s5)
        s6.addPrompt("neutral3", s6)
        s6.addPrompt("positive1", s7)
        s6.addPrompt("positive2", s8)
        s6.addPrompt("positive3", s9)
        s6.addPrompt("negative1", s10)
        s6.addPrompt("negative2", s11)
        s6.addPrompt("negative3", s12)
        s7.addPrompt("leavePositive", s2)
        s7.addPrompt("leaveNegative", s3)
        s7.addPrompt("neutral1", s4)
        s7.addPrompt("neutral2", s5)
        s7.addPrompt("neutral3", s6)
        s7.addPrompt("positive1", s7)
        s7.addPrompt("positive2", s8)
        s7.addPrompt("positive3", s9)
        s7.addPrompt("negative1", s10)
        s7.addPrompt("negative2", s11)
        s7.addPrompt("negative3", s12)
        s7.addPrompt("endLoop", s18)
        s8.addPrompt("leavePositive", s2)
        s8.addPrompt("leaveNegative", s3)
        s8.addPrompt("neutral1", s4)
        s8.addPrompt("neutral2", s5)
        s8.addPrompt("neutral3", s6)
        s8.addPrompt("positive1", s7)
        s8.addPrompt("positive2", s8)
        s8.addPrompt("positive3", s9)
        s8.addPrompt("negative1", s10)
        s8.addPrompt("negative2", s11)
        s8.addPrompt("negative3", s12)
        s9.addPrompt("leavePositive", s2)
        s9.addPrompt("leaveNegative", s3)
        s9.addPrompt("neutral1", s4)
        s9.addPrompt("neutral2", s5)
        s9.addPrompt("neutral3", s6)
        s9.addPrompt("positive1", s7)
        s9.addPrompt("positive2", s8)
        s9.addPrompt("positive3", s9)
        s9.addPrompt("negative1", s10)
        s9.addPrompt("negative2", s11)
        s9.addPrompt("negative3", s12)
        s10.addPrompt("leavePositive", s2)
        s10.addPrompt("leaveNegative", s3)
        s10.addPrompt("neutral1", s4)
        s10.addPrompt("neutral2", s5)
        s10.addPrompt("neutral3", s6)
        s10.addPrompt("positive1", s7)
        s10.addPrompt("positive2", s8)
        s10.addPrompt("positive3", s9)
        s10.addPrompt("negative1", s10)
        s10.addPrompt("negative2", s11)
        s10.addPrompt("negative3", s12)
        s11.addPrompt("leavePositive", s2)
        s11.addPrompt("leaveNegative", s3)
        s11.addPrompt("neutral1", s4)
        s11.addPrompt("neutral2", s5)
        s11.addPrompt("neutral3", s6)
        s11.addPrompt("positive1", s7)
        s11.addPrompt("positive2", s8)
        s11.addPrompt("positive3", s9)
        s11.addPrompt("negative1", s10)
        s11.addPrompt("negative2", s11)
        s11.addPrompt("negative3", s12)
        s12.addPrompt("leavePositive", s2)
        s12.addPrompt("leaveNegative", s3)
        s12.addPrompt("neutral1", s4)
        s12.addPrompt("neutral2", s5)
        s12.addPrompt("neutral3", s6)
        s12.addPrompt("positive1", s7)
        s12.addPrompt("positive2", s8)
        s12.addPrompt("positive3", s9)
        s12.addPrompt("negative1", s10)
        s12.addPrompt("negative2", s11)
        s12.addPrompt("negative3", s12)
        s19.addPrompt("entrance", s1)
        
        Game.currentScenario = s19

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
        self.setResponse("Press the confirm button to begin!")

    def process(self, event):
        global firstRun
        global completedRun
        global LL
        if firstRun == True:
            response, LL, changeScenario, voice = dialogueSearch("start")
            self.setResponse(response)
            if(changeScenario in Game.currentScenario.prompts):
                    Game.currentScenario = Game.currentScenario.prompts[changeScenario]
            self.setScenarioImage()
            mixer.music.load(voice)
            mixer.music.play()
            firstRun = False
            return
        if completedRun == True:
            ending, changeScenario = determineEnding()
            if(changeScenario in Game.currentScenario.prompts):
                Game.currentScenario = Game.currentScenario.prompts[changeScenario]
            self.setScenarioImage()
            self.setResponse(ending)
            Game.player_input.delete(0, END)
        else:
            userIn = Game.player_input.get()
            index = userInput(userIn, LL)
            if index == 0:
                response = ("Error: Invalid Input" \
                           "\nTry a Valid Input")
                self.setResponse(response)
                Game.player_input.delete(0, END)
                return
            else:
                response, LL, changeScenario, voice = dialogueSearch(index)
                self.setResponse(response)
                if(changeScenario in Game.currentScenario.prompts):
                    Game.currentScenario = Game.currentScenario.prompts[changeScenario]
                self.setScenarioImage()
                mixer.music.load(voice)
                mixer.music.play()
                Game.player_input.delete(0, END)
                if LL == "1":
                    completedRun = True
        

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

##################################################
    
def dialogueSearch(index):
    global partnerOpinion
    global TwoPrompt
    global ThreePrompt
    global LL
    global loopEnding
    TwoPrompt = False
    ThreePrompt = False
    if index == "start":
        a = LinkedList()
        response = ("Hey, I'll be your partner for this assignment." \
                    "\nI hope we get along." \
                    "\n\n 1 - I hope so too." \
                    "\n 2 - As long as we get the work done." \
                    "\n 3 - Somehow, I doubt that.")
        a.append_item("a1")
        a.append_item("a2")
        a.append_item("a3")
        partnerOpinion = 0
        LL = a
        voice = "start.mp3"
        currentScenario = "entrance"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "a1":
        b = LinkedList()
        response = ("With optimism like that, I'm sure we will." \
                    "\nSo, any ideas for the assignment?" \
                    "\n\n 1 - Maybe a robot of some sort?" \
                    "\n 2 - How about a program to demonstrate some particular skill?" \
                    "\n 3 - I'm not quite sure yet.")
        b.append_item("c1")
        b.append_item("c2")
        b.append_item("c3")
        partnerOpinion += 2
        LL = b
        voice = "a1.mp3"
        currentScenario = "positive1"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "a2":
        c = LinkedList()
        response = ("I'm sure everything will work out." \
                    "\nSo, any ideas for the assignment?" \
                    "\n\n 1 - Maybe a robot of some sort?" \
                    "\n 2 - How about a program to demonstrate some particular skill?" \
                    "\n 3 - I'm not quite sure yet.")
        c.append_item("c1")
        c.append_item("c2")
        c.append_item("c3")
        LL = c
        voice = "a2.mp3"
        currentScenario = "neutral1"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "a3":
        d = LinkedList()
        response = ("Come on, man. Don't be like that." \
                    "\nTry being more optimistic." \
                    "\n\n 1 - You're right. I'm sorry." \
                    "\n 2 - Sorry. I didn't mean anything by that." \
                    "\n 3 - Try being less annoying.")
        d.append_item("b1")
        d.append_item("b2")
        d.append_item("b3")
        partnerOpinion -= 1
        LL = d
        voice = "a3.mp3"
        currentScenario = "negative1"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "b1":
        e = LinkedList()
        response = ("That's the spirit! Let's do this!" \
                    "\nSo, any ideas for the assignment?" \
                    "\n\n 1 - Maybe a robot of some sort?" \
                    "\n 2 - How about a program to demonstrate some particular skill?" \
                    "\n 3 - I'm not quite sure yet.")
        e.append_item("c1")
        e.append_item("c2")
        e.append_item("c3")
        partnerOpinion += 1
        LL = e
        voice = "b1.mp3"
        currentScenario = "positive2"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "b2":
        f = LinkedList()
        response = ("I guess the stress is getting to you." \
                    "\nJust remember, we can't work well together if we don't understand each other." \
                    "\nSo, any ideas for the assignment?" \
                    "\n\n 1 - Maybe a robot of some sort?" \
                    "\n 2 - How about a program to demonstrate some particular skill?" \
                    "\n 3 - I'm not quite sure yet.")
        f.append_item("c1")
        f.append_item("c2")
        f.append_item("c3")
        LL = f
        voice = "b2.mp3"
        currentScenario = "neutral2"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "b3":
        g = LinkedList()
        response = ("I feel like I'm going to regret this." \
                    "\nSo, any ideas for the assignment?" \
                    "\n\n 1 - Maybe a robot of some sort?" \
                    "\n 2 - How about a program to demonstrate some particular skill?" \
                    "\n 3 - I'm not quite sure yet.")
        g.append_item("c-pa1")
        g.append_item("c-pa2")
        g.append_item("c-pa3")
        partnerOpinion -= 2
        LL = g
        voice = "b3.mp3"
        currentScenario = "negative2"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "c1":
        h = LinkedList()
        response = ("That's... not really my area of expertise." \
                    "\nIf we're going to do this, we need to support each other." \
                    "\n\n 1 - No worries, I have confidence in us." \
                    "\n 2 - We'll see as we go along.")
        h.append_item("d1")
        h.append_item("d2")
        LL = h
        voice = "c1.mp3"
        currentScenario = "neutral3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "c2":
        i = LinkedList()
        response = ("That sounds really fun! I wonder what we will be able to do." \
                    "\nDo you think you'll be able to handle the work involved?" \
                    "\n\n 1 - Absolutely! Bring it on!" \
                    "\n 2 - We'll see.")
        i.append_item("j1")
        i.append_item("j2")
        LL = i
        voice = "c2.mp3"
        currentScenario = "positve3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "c3":
        response = ("No big deal! It's the first day, anyway." \
                    "\nWe might be able to create something naturally." \
                    "\nAs long as we stay on task, it'll turn out fine." \
                    "\nTalk to you later! Hopefully with an idea." \
                    "\n\nPress 'Enter' to continue")
        LL = "1"
        voice = "c3.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "c-pa1":
        j = LinkedList()
        response = ("That's not my area of expertise." \
                    "\nAnd besides, how can I trust you'll actually do your part?" \
                    "\n\n 1 - Look, I'm sorry. I'll do my part, I swear." \
                    "\n 2 - I'll try, but I can't make any promises.")
        j.append_item("d-pa1")
        j.append_item("d-pa2")
        LL = j
        voice = "c-pa1.mp3"
        currentScenario = "neutral2"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "c-pa2":
        k = LinkedList()
        response = ("Ok, maybe that could work." \
                    "\nDo you have any ideas in mind?" \
                    "\n\n 1 - How about a word-sorter?" \
                    "\n 2 - We could do something with a GUI." \
                    "\n 3 - Oh! A soundboard!" \
                    "\n 4 - No, do you?")
        k.append_item("k-pa1")
        k.append_item("k-pa2")
        k.append_item("k-pa3")
        k.append_item("k-pa4")
        LL = k
        voice = "c-pa2.mp3"
        currentScenario = "neutral1"
        return response, LL, currentScenario, voice
    if index == "c-pa3":
        response = ("You know what, screw this." \
                    "\nTalk to me when you have an idea. Otherwise, don't bother." \
                    "\n\nPress 'Enter' to contnue")
        partnerOpinion -= 1
        LL = "1"
        voice = "c-pa3.mp3"
        currentScenario = "leaveNegative"
        return response, LL, currentScenario, voice
    if index == "d1":
        l = LinkedList()
        response = ("That's good to hear." \
                    "\nMaybe this project will be easier than I thought." \
                    "\n\n 1 - I sure hope so." \
                    "\n 2 - Isn't that a little too optimisitc?")
        l.append_item("e1")
        l.append_item("e2")
        partnerOpinion += 1
        LL = l
        voice = "d1.mp3"
        currentScenario = "positive3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "d2":
        m = LinkedList()
        response = ("I suppose you have a point." \
                    "\nCan't know anything until we try, right?" \
                    "\n\n 1 - Not a bad outlook." \
                    "\n 2 - Granted, it would be better if we knew before.")
        m.append_item("f1")
        m.append_item("f2")
        LL = m
        voice = "d2.mp3"
        currentScenario = "neutral3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "d-pa1":
        n = LinkedList()
        response = ("Hm, if you say so." \
                    "\nMaybe I misjudged you at first? You don't seem as unreasonable anymore." \
                    "\nHope things continue this way as we work on the project." \
                    "\n\n 1 - I hope so too." \
                    "\n 2 - Isn't that a little too optimistic?")
        n.append_item("e1")
        n.append_item("e2")
        partnerOpinion += 1
        LL = n
        voice = "d-pa1.mp3"
        currentScenario = "positive1"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "d-pa2":
        o = LinkedList()
        response = ("As much as I hate to admit it, I guess you have a point." \
                    "\nCan't know anything unless we try, right?" \
                    "\n\n 1 - Not a bad outlook." \
                    "\n 2 - Granted, it would be better if we knew before.")
        o.append_item("f1")
        o.append_item("f2")
        LL = o
        voice = "d-pa2.mp3"
        currentScenario = "neutral1"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "e1":
        p = LinkedList()
        response = ("Don't think about it too much!" \
                    "\nWe'll cross that bridge when we get there." \
                    "\nAnyway, should we meet again later?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        p.append_item("g1")
        p.append_item("g2")
        LL = p
        voice = "e1.mp3"
        currentScenario = "neutral2"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "e2":
        q = LinkedList()
        response = ("This early on? Maybe, but it's a good mindset, right?" \
                    "\nWe should remain optimistic if we want to get anywhere." \
                    "\n\n 1 - Maybe you're right." \
                    "\n 2 - I don't know about that...")
        q.append_item("h1")
        q.append_item("h2")
        partnerOpinion -= 1
        LL = q
        voice = "e2.mp3"
        currentScenario = "negative1"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "f1":
        r = LinkedList()
        response = ("I'm glad you agree!" \
                    "\nSo, should we meet again later?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        r.append_item("g1")
        r.append_item("g2")
        partnerOpinion += 1
        LL = r
        voice = "f1.mp3"
        currentScenario = "positive2"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "f2":
        s = LinkedList()
        response = ("Well, I won't say you're wrong there." \
                    "\nBut what's the fun in that?" \
                    "\nDon't you think this'll be fun?" \
                    "\n\n 1 - I think it will be, if we work together." \
                    "\n 2 - If all goes well, it could be." \
                    "\n 3 - I don't particularly enjoy projects, so not really.")
        s.append_item("i1")
        s.append_item("i2")
        s.append_item("i3")
        LL = s
        voice = "f2.mp3"
        currentScenario = "neutral2"
        ThreePrompt = True
        return response, LL, currentScenario, voice
    if index == "g1":
        response = ("Cool, looking forward to working with you!" \
                    "\nSee you later, yeah?" \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion += 1
        LL = "1"
        voice = "g1.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "g2":
        response = ("Oh, that's fine. Just let me know when you're free." \
                    "\nTalk to you later!" \
                    "\n\nPress 'Enter' to continue.")
        LL = "1"
        voice = "g2.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "g-pa1":
        response = ("Great to see you're onboard." \
                    "\nSee you later, yeah?" \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion += 1
        LL = "1"
        voice = "g-pa1.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "g-pa2":
        response = ("You do realise that this is a big part of our final grade, right?" \
                    "\nWhenever you're ready, come find me." \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion -= 1
        LL = "1"
        voice = "g-pa2.mp3"
        currentScenario = "leaveNegative"
        return response, LL, currentScenario, voice
    if index == "h1":
        response = ("I know I'm right!" \
                    "\nAnyway, it's getting late, so I'll be off." \
                    "\nSee you later!" \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion += 1
        LL = "1"
        voice = "h1.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "h2":
        response = ("Oh, come on, lighten up a little!" \
                    "\nWell, I've gotta go." \
                    "\nWe'll talk about this later." \
                    "\n\nPress 'Enter' to continue.")
        LL = "1"
        voice = "h2.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "i1":
        response = ("You had me worried there for a minute. Thought I'd have to kill ya." \
                    "\nWell, I'll talk to you later." \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion += 1
        LL = "1"
        voice = "i1.mp3"
        currentScenario = "leavePositive"
        return response, LL, currentScenario, voice
    if index == "i2":
        response = ("I think you missed the point." \
                    "\nThis isn't about success or failure." \
                    "\nIt's about our progress as students and future workers." \
                    "\nWell, I'll leave you to it. See you on the flip side." \
                    "\n\nPress 'Enter' to continue.")
        LL = "1"
        voice = "i2.mp3"
        currentScenario = "leaveNegative"
        return response, LL, currentScenario, voice
    if index == "i3":
        response = ("That's not the greatest mindset for a group project." \
                    "\nIt'll only make it harder to work, you know?" \
                    "\nEither way, we'll work it out later. Take care." \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion -= 1
        LL = "1"
        voice = "i3.mp3"
        currentScenario = "leaveNegative"
        return response, LL, currentScenario, voice
    if index == "j1":
        t = LinkedList()
        response = ("That's what I like to hear!" \
                    "\nDo you have a particular skill you'd like to show off?" \
                    "\n\n 1 - How about a word-sorter?" \
                    "\n 2 - We could do something with a GUI." \
                    "\n 3 - Oh! A soundboard!" \
                    "\n 4 - Do you have any ideas?")
        t.append_item("k1")
        t.append_item("k2")
        t.append_item("k3")
        t.append_item("k4")
        partnerOpinion += 1
        LL = t
        voice = "j1.mp3"
        currentScenario = "positive2"
        return response, LL, currentScenario, voice
    if index == "j2":
        u = LinkedList()
        response = ("A little concerning, since this is your idea." \
                    "\nBut I'm here to help." \
                    "\nDo you have a particular skill you'd like to show off?" \
                    "\n\n 1 - How about a word-sorter?" \
                    "\n 2 - We could do something with a GUI." \
                    "\n 3 - Oh! A soundboard!" \
                    "\n 4 - Do you have any ideas?")
        u.append_item("k1")
        u.append_item("k2")
        u.append_item("k3")
        u.append_item("k4")
        LL = u
        voice = "j2.mp3"
        currentScenario = "neutral1"
        return response, LL, currentScenario, voice
    if index == "k1":
        v = LinkedList()
        response = ("Hey, that's really cool!" \
                    "\nWe could use classes for something. We'd need to flesh this out more." \
                    "\nCan you meet next week?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        v.append_item("g1")
        v.append_item("g2")
        LL = v
        voice = "k1.mp3"
        currentScenario = "positive1"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k2":
        w = LinkedList()
        response = ("That's... vague. But don't worry, we can flesh it out as we go." \
                    "\nCan you meet next week?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        w.append_item("g1")
        w.append_item("g2")
        LL = w
        voice = "k2.mp3"
        currentScenario = "neutral2"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k3":
        x = LinkedList()
        response = ("Yes, yes! That's a really good use of the breadboard!" \
                    "\nCan we meet next week to flesh this out?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        x.append_item("g1")
        x.append_item("g2")
        LL = x
        voice = "k3.mp3"
        currentScenario = "positive3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k4":
        y = LinkedList()
        response = ("Umm... how about a choose-your-own-adventure?" \
                    "\nI have a really good idea for it." \
                    "\n\n 1 - Yeah, that sounds good." \
                    "\n 2 - I'm not sure about this idea.")
        y.append_item("l1")
        y.append_item("l2")
        LL = y
        voice = "k4.mp3"
        currentScenario = "neutral3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k-pa1":
        z = LinkedList()
        response = ("Not a bad idea." \
                    "\nWe can make this work." \
                    "\nCan you meet next week?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        z.append_item("g-pa1")
        z.append_item("g-pa2")
        LL = z
        voice = "k-pa1.mp3"
        currentScenario = "neutral2"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k-pa2":
        aa = LinkedList()
        response = ("That's... vague." \
                    "\nCan you meet next week? I'll need more details." \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        aa.append_item("g-pa1")
        aa.append_item("g-pa2")
        LL = aa
        voice = "k-pa2.mp3"
        currentScenario = "neutral3"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k-pa3":
        bb = LinkedList()
        response = ("Ok. That's a good use of a breadboard." \
                    "\nCan you meet next week?" \
                    "\n\n 1 - Yeah, that sounds like a good idea." \
                    "\n 2 - I can't, I'm busy.")
        bb.append_item("g-pa1")
        bb.append_item("g-pa2")
        LL = bb
        voice = "k-pa3.mp3"
        currentScenario = "positive1"
        TwoPrompt = True
        return response, LL, currentScenario, voice
    if index == "k-pa4":
        response = ("No, I don't." \
                    "\nI guess today is not a good day for brainstorming." \
                    "\nLet's try again later." \
                    "\n\nPress 'Enter' to continue.")
        partnerOpinion -= 1
        LL = "1"
        voice = "k-pa4.mp3"
        currentScenario = "leaveNegative"
        return response, LL, currentScenario, voice
    if index == "l1":
        response = ("Alright! We can take a meta angle." \
                    "\nOne with two partners talking about what to do for a final project..." \
                    "\n\nPress 'Enter' to continue.")
        LL = "1"
        voice = "l1.mp3"
        currentScenario = "positive1"
        loopEnding = True
        return response, LL, currentScenario, voice
    if index == "l2":
        cc = LinkedList()
        response = ("Do you have a better idea?" \
                    "\n\n 1 - How about a word-sorter?" \
                    "\n 2 - We could do something with a GUI." \
                    "\n 3 - Oh! A soundboard!" \
                    "\n 4 - Do you have any ideas?")
        cc.append_item("k1")
        cc.append_item("k2")
        cc.append_item("k3")
        cc.append_item("k4")
        LL = cc
        voice = "l2.mp3"
        currentScenario = "neutral2"
        return response, LL, currentScenario, voice
    
def userInput(userIn, LL):
    global TwoPrompt
    global ThreePrompt
    if userIn == "1":
        index = LL[0]
        return index
    elif userIn == "2":
        index = LL[1]
        return index
    elif(userIn == "3" and TwoPrompt != True):
        index = LL[2]
        return index
    elif(userIn == "4" and TwoPrompt != True and ThreePrompt != True):
        index = LL[3]
        return index
    else:
        index = 0
        return index

def determineEnding():
    global partnerOpinion
    global loopEnding
    if(loopEnding == True):
        ending = ("Ending: Infinite Loop" \
                  "\n\nThey never finished their project." \
                  "\nThe two partners got stuck in a fractal plan." \
                  "\nIt was so dense that the though created a black hole." \
                  "\nThe black hole grew and destroyed the entire world." \
                  "\nThey never received their final grade.")
        currentScenario = "endLoop"
    elif(partnerOpinion > 3):
        ending = ("Ending: Best Ending" \
                  "\n\nAnd so the pair worked hard." \
                  "\nTheir friendship and understanding helped them finish the project." \
                  "\nPlenty of time remained before the presentation." \
                  "\nAt the EXPO, people crowded around their display." \
                  "\nThey were marveling at the wonderful project the two made." \
                  "\nTheir final grade was an A.")
        currentScenario = "endBest"
    elif(partnerOpinion > 1 and partnerOpinion < 4):
        ending = ("Ending: Good Ending" \
                  "\n\nThe pair worked reasonably hard." \
                  "\nThey worked well together, despite 1 or 2 rough patches." \
                  "\nAt the EXPO, a small group of people saw the fruit of their labor." \
                  "\nTheir final grade was a B.")
        currentScenario = "endGood"
    elif(partnerOpinion > -2 and partnerOpinion < 2):
        ending = ("Ending: Neutral Ending" \
                  "\n\nAnd so they worked." \
                  "\nThey never really bonded as friends, but they were not enemies either." \
                  "\nAt the EXPO, their project appeared perfectly average." \
                  "\nThey didn't get any more attention than anyone else." \
                  "\nIt wasn't bad or good, just mediocre." \
                  "\nTheir final grade was a C.")
        currentScenario = "endNeutral"
    elif(partnerOpinion > -4 and partnerOpinion < 1):
        ending = ("Ending: Bad Ending" \
                  "\n\nThe project began." \
                  "\nThe two partners never really saw eye-to-eye." \
                  "\nAs such, they didn't do quite as well as they could have." \
                  "\nAt the EXPO, no-one saw their barely functional project." \
                  "\nTheir final grade was a D.")
        currentScenario = "endBad"
    elif(partnerOpinion < -3):
        ending = ("Ending: Worst Ending" \
                  "\n\nThe two partners were bitter towards each other." \
                  "\nThis caused their project to be all but well put-together." \
                  "\nAt the EXPO, people gathered around, marveling at their spectacular failure of a project." \
                  "\nThey blame each other to this day." \
                  "\nTheir final grade was an F.")
        currentScenario = "endWorst"
    return ending, currentScenario

######################################################

WIDTH = 500
HEIGHT = 400

window = Tk()
window.title("DS^2")

firstRun = True
completedRun = False
loopEnding = False
TwoPrompt = False
ThreePrompt = False
g = Game(window)
g.play()

window.mainloop()

