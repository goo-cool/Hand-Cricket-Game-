#modules-
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog

import cv2
import numpy as np
import mediapipe as mp
import time
import os
import random




m = Tk()
m.title(" HAND CRICKET GAME ")
m.geometry ("1600x900")

hnd =  Label(m, text = " HAND CRICKET GAME ",bd = 25,anchor =CENTER,font = 'Alaska 22 bold')
hnd.pack(padx=10,pady=10)

#canvas

canvas = Canvas(m,height=2000,width=10000,bg='white')
canvas.pack(ipadx = 0,ipady=150)



def start():
       import video  



    
def exit_but():
    messagebox.showinfo(" EXIT " , " Thanks For Playing ! ")


#original score
orig_score = random.randint(10,20) #original score
    

#start_But
pc = PhotoImage(file = "download.png")
pc1 = pc.subsample(2,2)
bt = Button(m,text = " START ",padx = 50,bg ='LawnGreen', command = start, font ='Alaska 22 bold',image = pc1,).place(x = 10, y = 5)
label = Label(m, text ="", font=('Calibri 15')).pack()
#exit_But
btn = Button(m,text = " EXIT ", padx = 50, command = exit_but).place(x = 1350, y = 40)


m.mainloop()


