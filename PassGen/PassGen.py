from tkinter import *
import random
import linecache

#Questions for first box
OPTIONS1 = [
    "In what city or town does your nearest sibling live?",
    "What was the last name of your fifth grade teacher?",
    "What was the name of your second dog/cat/goldfish/etc?",
    "Where were you when you had your first kiss?",
    "Custom Answer",
    "Random"
]
#Questions for second box
OPTIONS2 = [
    "When you were young, what did you want to be when you grew up?",
    "What is your oldest cousin's first and last name?",
    "What is your youngest brother's/sister's birthday?",
    "What was the name of your elementary / primary school?",
    "Custom Answer",
    "Random"
]

# STRING =''.join(map(randUpper, STRING))
def randUpper(command):
    if random.random() > 0.5:
        return command.upper()
    return command.lower()

def getRandomWord():
    line_num1 = random.randint(0, 58109)  # Choose random integer of lines on file
    return linecache.getline('wordlist', line_num1)[:-1] #Get that random integer

def setRandom(entry):
    entry.delete(0,END)
    entry.insert(0, getRandomWord())

def make1337():
    leetlist = { #Letters to change
        'a':'4',
        'e':'3',
        'g':'6',
        'i':'1',
        'o':'0',
        's':'5',
        't':'7'
    }
    global newPass
    newPass = password1[0]
    for i in password1[1:]:
        if i in leetlist:
            if random.random() > 0.5:
                newPass += leetlist[i]
            else:
                newPass += i
        else:
            newPass += i



#Main Window
def window():

    #Commands

    def OptionMenu_SelectionEvent1(event): #When option menu one is changed

        check_for_rand1 = initialOpt1.get() #Check for choice

        if check_for_rand1 == "Random": #If option menu one is random selection
            setRandom(entry1)
        else:
            pass

    def OptionMenu_SelectionEvent2(event): #When option menu two is changed

        check_for_rand2 = initialOpt2.get() #Check for choice

        if check_for_rand2 == "Random": #If option menu two is random selection
            setRandom(entry2)
        else:
            pass

    def done_and_done():
        newWin = Tk()
        newWin.title("Your new password is: ")

        text1 = entry1.get()
        text2 = entry2.get()

        global password1
        password1 = text1 + text2
        password1 = password1.replace(" ", "")
        password1 = ''.join(map(randUpper, password1))
        make1337()
        theLabel = Label(newWin, text='Your password is: ')
        theLabel.pack(side=TOP)
        finalPass = Label(newWin, text=newPass)
        finalPass.pack()

        #Make copy to clip button

        def CopyIt():
            newWin.clipboard_clear()
            newWin.clipboard_append(newPass)
        #Create Button
        clippybutton = Button(newWin, text='Copy to Clipboard?', command=CopyIt)
        clippybutton.pack(side=BOTTOM)





    #Initialize the Main Window

    root = Tk()
    root.title("Passwords for all!")

    #Initial Options for Drop/Option Menus
    global initialOpt1
    global initialOpt2
    initialOpt1 = StringVar(root)
    initialOpt1.set('Choose One')
    initialOpt2 = StringVar(root)
    initialOpt2.set('Choose One')

    #Insert Widgets

    drop1 = OptionMenu(root, initialOpt1, *OPTIONS1, command=OptionMenu_SelectionEvent1)
    drop1.pack() #End of Drop1

    entry1 = Entry(root)
    entry1.pack(side=TOP)
    entry1.insert(0, "Answer here!") #Tells user where to input
    #End of Entry1

    drop2 = OptionMenu(root, initialOpt2, *OPTIONS2, command=OptionMenu_SelectionEvent2)
    drop2.pack() #End of Drop2

    entry2 = Entry(root)
    entry2.pack(side=TOP)
    entry2.insert(0, "Answer here!")
    #End of Entry2

    button1 = Button(root, text='Submit', command=done_and_done)
    button1.pack()
    #End

    mainloop() #Loop window
window()