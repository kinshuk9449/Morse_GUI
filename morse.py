from tkinter import * 
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
 
root = Tk()
 
def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
 
    result = myEntry.get()
    list_of_letters = list(result)
    for  a in list:
     letters_morse(a)
    resultLabel.config(text=result)
    myEntry.delete(0,END)
 
# Create the Entry widget
myEntry = Entry(root, width=20)
myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.pack()
 
# Create the Enter button
enterEntry = Button(root, text= "Enter", command=returnEntry)
enterEntry.pack(fill=X)
 
# Create and emplty Label to put the result in
resultLabel = Label(root, text = "")
resultLabel.pack(fill=X)

def dot():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8,GPIO.LOW)

def dash():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(8,GPIO.LOW)

def letters_morse(letter):

    if letter == "A":
        dot()
        time.sleep(1)
        dash()

    elif letter == "B":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()

    elif letter == "C":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()

    elif letter == "D":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()

    elif letter == "E":
        dot()

    elif letter == "F":
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()

    elif letter == "G":
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()

    elif letter == "H":
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()

    elif letter == "I":
        dot()
        time.sleep(1)
        dot()

    elif letter == "J":
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()

    elif letter == "K":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)

    elif letter == "L":
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()

    elif letter == "M":
        dash()
        time.sleep(1)
        dash()

    elif letter == "N":
        dash()
        time.sleep(1)
        dot()

    elif letter == "O":
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()

    elif letter == "P":
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()

    elif letter == "Q":
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()

    elif letter == "R":
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()

    elif letter == "S":
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()

    elif letter == "T":
        dash()

    elif letter == "U":
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()

    elif letter == "V":
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()

    elif letter == "W":
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()

    elif letter == "X":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()

    elif letter == "Y":
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dash()
        time.sleep(1)
        dash()

    elif letter == "Z":
        dash()
        time.sleep(1)
        dash()
        time.sleep(1)
        dot()
        time.sleep(1)
        dot()
