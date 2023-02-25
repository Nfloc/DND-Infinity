from guizero import App, Text, PushButton, TextBox, Combo, Box
from time import sleep
import sys
import random




app = App(title="DND RFID", bg="green")

def readApp():
    return

def writeApp():
    app.destroy()
    wr=App(title="DND RFID", bg="green")
    box=Box(wr,layout="grid")
    abs=Text(wr,text="\n\n\n")
    cn=TextBox(wr,text="Enter Name",width=24)
    clas=Combo(wr, options=["Select Class","Knight", "Wizard", "Barbarian"])
    race=Combo(wr, options=["Select Race","Human", "Elf", "Dwarf"])
    xp=TextBox(wr,text="Enter XP",width=15)
    abs=Text(wr, text="\n\nAbility Scores")

    abs=Text(wr, text="STR",size=6)
    str=TextBox(wr,width=15)
    
    abs=Text(wr, text="DEX",size=6)
    dex=TextBox(wr,width=15)
    
    abs=Text(wr, text="CON",size=6)
    con=TextBox(wr,width=15)
    
    abs=Text(wr, text="INT",size=6)
    intt=TextBox(wr,width=15)
    
    abs=Text(wr, text="WIS",size=6)
    wis=TextBox(wr,width=15)
    
    abs=Text(wr, text="CHA",size=6)
    cha=TextBox(wr,width=15)

    abs=Text(wr,text="Dice!",)
    Dice_N = TextBox(wr,width=15, text= "enter number of dice faces")
    def D1(Dice_N):
        D2 = random.randint(1,Dice_N)
        abs=Text(wr, text=str(D2),size=6)
    dice = PushButton(wr, text="Roll dice",command=D1)
    
intro = Text(app, text="Figure to Text")
read = PushButton(app, text="Read Figure")
write = PushButton(app, text="Write to Figure",command=writeApp)

app.display()   

