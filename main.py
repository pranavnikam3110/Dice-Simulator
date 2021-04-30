from tkinter import *
from PIL import Image,ImageTk
import random
from playsound import playsound


root=Tk()
root.geometry("700x700")
root.iconbitmap("dice.ico")

root.title("DICE SIMULATOR")

l0=Label(root,text="Wish You, ALL THE BEST!",fg="white",bg="black",font="Roboto 20 bold",width=100,height=2)
l0.pack()

dice=['1.png','2.png','3.png','4.png','5.png','6.png']
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))

l11=Label(root,image=image1)
l11.image=image1

l11.pack(expand=True)

def rolling_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))

    l11.configure(image=image1)

    l11.image=image1

    playsound('1.wav')




button=Button(root,text="ROLL DICE",font="Roboto 15 bold",command=rolling_dice,width=30,height=2,bg="orange",fg="black")
button.pack(expand=True)



root.mainloop()