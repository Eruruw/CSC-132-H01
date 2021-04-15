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

# test (start)
# prompt1 (p1)
#  - response1 (r1)
#       promt2 (p2)
#        - response4 (r4)
#           answer1
#        - response5 (r5)
#           answer2
#        - response6 (r6)
#           answer3
#  - response2 (r2)
#       promt3 (p3)
#        - response7 (r7)
#           answer4
#        - response8 (r8)
#           answer5
#  - response3 (r3)
#       promt4(p4)
#        - response9 (r9)
#           answer6
#        - response10 (r10)
#           answer7
#        - response11 (r11)
#           answer8


def diolagueSearch(index):
    TwoPromt = False
    global TwoPrompt
    global LL
    if index == "start":
        print("test" \
              "\nprompt" \
              "\n - response1" \
              "\n - response2" \
              "\n - response3")
        a.append_item("r1")
        a.append_item("r2")
        a.append_item("r3")
        LL = a
        userInput()
    if index == "r1":
        b = LinkedList()
        print("promt2" \
              "\n - response4" \
              "\n - response5" \
              "\n - response6")
        b.append_item("r4")
        b.append_item("r5")
        b.append_item("r6")
        LL = b
        userInput()
    if index == "r2":
        c = LinkedList()
        print("promt3" \
              "\n - response7" \
              "\n - response8")
        c.append_item("r7")
        c.append_item("r8")
        TwoPrompt = True
        LL = c
        userInput()
    if index == "r3":
        d = LinkedList()
        print("prompt4" \
              "\n - response9" \
              "\n - response10" \
              "\n - response11")
        d.append_item("r9")
        d.append_item("r10")
        d.append_item("r11")
        LL = d
        userInput()
    if index == "r4":
        print("answer1")
    if index == "r5":
        print("answer2")
    if index == "r6":
        print("answer3")
    if index == "r7":
        print("answer4")
    if index == "r8":
        print("answer5")
    if index == "r9":
        print("answer6")
    if index == "r10":
        print("answer7")
    if index == "r11":
        print("answer8")

def userInput():
    global TwoPrompt
    global LL
    userIn = input()
    if userIn == "1":
        index = LL[0]
        diolagueSearch(index)
    elif userIn == "2":
        index = LL[1]
        diolagueSearch(index)
    elif(userIn == "3" and TwoPrompt != True):
        index = LL[2]
        diolagueSearch(index)
    else:
        print("Error, invalid input")
        
TwoPrompt = False
a = LinkedList()
diolagueSearch("start")









    

    
