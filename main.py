# Main file for light sensor

from tkinter import *
from tkinter import Button
from gpiozero import Button,LED
import time

is_on = False

btnOn = Button(2)
btnSignal = Button(3)
led = LED(4)
led.off()

class AppWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.after(500, self.scanUpdate)
        self.signals = [False]*5
        self.textCooldown = 240

    def scanUpdate(self):
        """Run every 0.25 seconds."""
        # print("updated")
        self.signals = [self.scanSignal()] + self.signals[:-1]
        if all(self.signals):
            self.sendText()
        self.after(250, self.scanUpdate)

    def scanSignal(self):
        """Return whether we need to send a warning."""


        # This is the "button" (binary state) that tells if the connection was broken
        if btnSignal.is_pressed:
            print("buttonSignal is pressed")
            return False




        ######################## Not sure if this goes here
        if btnOn.is_pressed:
            print("buttonOn is pressed")
            is_on = True


        if is_on == True:
            led.on()
        else:
            led.off()
        #######################




        # TODO: RASPI CODE
        return False

    def sendText(self):
        """Send a warning text with the current timecode."""
        # TODO: Rupanti's code here
        self.textCooldown = 240


root = Tk()
app = AppWindow(root)
button = Button(root, text="Press")
button.pack(pady=200)


# set window title
# root.state('zoomed')
root.attributes('-fullscreen', True)
root.wm_title("Tkinter window")

# show window
root.mainloop()
