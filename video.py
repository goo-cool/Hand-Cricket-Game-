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
import HandTrackingModule as htm



def start():
        
    #canvas for score to be chasen

    win= Tk()
    win.title("    ScOrE    ")
    win.geometry('500x150')

    

    
    

    hnd =  Label(win, text = "  THE SCORE TO B CHASEN :   ",bd = 15,anchor =N,font = 'Alaska 22 ')
    hnd.pack(ipadx = 1 ,ipady =10 ) 


    H = Label(win, text = orig_score,bd = 15,anchor =N,font = 'Alaska 22 bold')
    H.pack(ipadx = 15 , ipady = 50)


    bt = Button(win, text = ' START NOW ', padx = 20 ,command = update).place(x=25,y = 100)


    


def photo_image(img_1):
    h, w = img_1.shape[:2]
    data = f'P6 {w} {h} 255 '.encode() + img_1[..., ::-1].tobytes()
    return PhotoImage(width=w, height=h, data=data, format='PPM')


play = True
def update():
    global userscore
    global play
    global l
    detector = htm.handDetector(detectionCon = 0)
    tipIds = [ 4, 8, 12, 16, 20]
    ret, img_1 = cap.read()
    img_1 = detector.findHands(img_1)
    lmlist = detector.findPosition(img_1, draw = False)
    #print(lmlist)
    fingers = []
    compso = random.randint(1,5)


    if len(lmlist) != 0:        
        #thumb
        if lmlist[tipIds[0]][1] < lmlist[tipIds[0]- 1][1]:
            fingers.append(0)
        else:
            fingers.append(1)

        #four fingers
        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]- 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)

    if play :
        TotalFingers =  fingers.count(1)       
    
        print(" Player 1- ",TotalFingers)
        userscore+=TotalFingers                       
        Label(root, text = str(TotalFingers),bg='white',font = 'Alaska 45 bold').place(x = 630,y=35)
        ind = l[compso-1]
        print(" Player 2- " ,ind)
        Label(root,text =ind,bg='white',font = 'Alaska 45 bold').place(x = 830,y = 35)
        
        print(userscore)
            
        time.sleep(0.1)


       
    if ret:
        photo = photo_image(img_1)
        cnv.create_image(15, 220, image=photo, anchor=NW)
        cnv.image = photo

        
    root.after(10, update)

            
             

root = Toplevel()
root.title("Video")
root.geometry('1530x680')

wCam, hCam = 500,500
cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

#canvas
cnv = Canvas(root, width=1530, height=1530,bg='white')
cnv.pack()

cnv.create_line(750,1000,750,0, fill = 'black',width = 5)
cnv.create_text(300,50, text = ' PLAYER 1 -   USER        ' , fill='black' ,font=('Alaska 15 bold'))
cnv.create_text(1100,50, text = ' PLAYER 2 -   Computer   ' , fill='black' ,font=('Helvetica 15 bold'))
cnv.create_rectangle(600,30,700,130,outline = 'black',width = 5)
cnv.create_rectangle(800,30,900,130,outline = 'red',width = 5)


#random
l=[1,2,3,4,5]
#score
userscore = 0

#original score
orig_score = 15 #original score
    

###image for comp


start()
root.mainloop()
cap.release()
