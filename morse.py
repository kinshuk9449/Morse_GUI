import RPi.GPIO as GPIO
import time
from Tkinter import *
import tkFont
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)

win = Tk()
win.title("Task 5.3D Morse Code")
myFont = tkFont.Font(family='Helvetica',size = 12, weight="bold")

### Label creation
Lb1 = Label(win, text = "Please enter your name ")
Lb1.pack()

### Word Limit
word = StringVar()

def letter_limit(*arg):
	user_input =text.get()
	if len(user_input)>12:
		word.set(user_input[:12])
word.trace_variable("w",letter_limit)

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

def runProgram():
	text = textBox.get()
	for answer in text.lower():
		letters_morse(answer)

def closeProgram():
	GPIO.cleanup()
	win.quit()

### WIDGETS ###
generateButton = Button(win, text = 'Generate', font = myFont, command = runProgram,bg ='green',height =1, width = 5)
generateButton.pack(side=TOP)

exitButton = Button(win, text = 'Exit', font = myFont, command = closeProgram,bg ='red',height =1, width = 5)
exitButton.pack(side= BOTTOM)

win.mainloop()