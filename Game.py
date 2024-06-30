from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog
import cv2
import numpy as np
import mediapipe as mp
import time
import os
import HandTrackingModule as htm

#video_capture
cap = cv2.VideoCapture(0)
#print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


def show_frame():
    ret, frame = cap.read()
    ret = cap.set(0,110)
    ret = cap.set(0,400)
    frame = cv2.flip(frame, 2)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk    
    lmain.after(10, show_frame)


m = Tk()
m.title(" TRIAL ")
m.geometry ("1500x1000")
Label(m, text = " HAND CRICKET GAME ",bd = 25,anchor =CENTER,font = 'Alaska 22 bold').pack()
#creating_canvas
canvas = Canvas(m , width = 2000 , height = 5000)
canvas.pack()
canvas.create_line(750,1000,750,0, fill = 'black',width = 5)
canvas.create_text(300,50, text = ' PLAYER 1 -           ' , fill='black' ,font=('Alaska 15 bold'))
canvas.create_text(1100,50, text = ' PLAYER 2 - Computer ' , fill='black' ,font=('Helvetica 15 bold'))




def on_click():
    messagebox.showinfo(" EXIT " , " Thanks For Playing ! ")
def start():
    import video


   
#start_But
pc = PhotoImage(file = r"C:\Users\DELL\Desktop\Gokul CYBER SECURITY\Class_12\Comp Proj\download.png")
pc1 = pc.subsample(2,2)
bt = Button(m,text = " START ",padx = 50,bg ='LawnGreen', command = start, font ='Alaska 22 bold',image = pc1,).place(x = 10, y = 5)
label = Label(m, text ="", font=('Calibri 15')).pack()
#exit_But
btn = Button(m,text = " EXIT ", padx = 50, command = on_click).place(x = 1350, y = 40)

#img_player-computer
img = ImageTk.PhotoImage(Image.open("1.png"))


m.mainloop()

 
