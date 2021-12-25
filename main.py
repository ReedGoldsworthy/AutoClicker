import time, pyautogui , keyboard , threading
from tkinter import *

window = Tk()

#Functions
def clickedStart():
    time.sleep(3)

    run = True
    interval_int = None

    try:
        interval_int = int(txt.get())
    except:
        pass

    start = time.time()

    while run == True:
        if keyboard.is_pressed('0'):
            run = False
            break

        if interval_int != None:
            if time.time() >= (start + interval_int):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()

#Title
window.title("Reed's AutoClicker")

#Label
lbl = Label(window, text="Click Delay")
lbl.grid(column=1, row=0, padx=(180, 10),  pady=(10, 10))

#text
txt = Entry(window, width=10)
txt.grid(column=1, row=1, padx=(180, 10))

#Buttons
btn = Button(window, text="Start Bot", command=clickedStart, bg="green", fg="lightgreen")
btn.grid(column=1, row=2, padx=(180, 10), pady=(30, 30))

#Window size
window.geometry('500x250')

#Change ICON


#Run app
txt.focus()
window.mainloop()


