from tkinter import *

#widgets = GUI elemts: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

window = Tk() #Instantiate an instance of a window
window.geometry("720x720")
window.title("Homosapien Servers")

notation = PhotoImage(file='Screenshot 2026-05-25 160947.png')
window.iconphoto(True, notation)
window.config(background='WHITE')


#label = an area widget that holds text and/or an image within a window
notation1 = PhotoImage(file='icons8-hand-32.png')
label = Label(window, 
              text="Humanity", 
              font=('Arial', 20, 'bold'), 
              fg='#000001', #Foreground
              bg='#910921', #Background
              relief=RAISED, #or SUNKEN
              bd=10,#Border
              padx=20, #pixel space X
              pady=20, #Pixel space Y
              image=notation1,
              compound='bottom'
              ) 
label.pack()
label1 = Label(window, text="Water")
label1.place(x=0, y=0)
window.mainloop()