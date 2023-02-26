from guizero import App, Text, PushButton, TextBox, Combo, Box, Window
from time import sleep
import sys
import random
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522



app = App(title="DND RFID", bg="green")

def kill():
    app.destroy()
    

def write2(name,classs,race,xp,st,dex,con,intt,wis,cha):

    wr2=Window(app,title="DND RFID WRITE2", bg="green", height=800)
    
    #Sets up the area
    abs=Text(wr2,text="\n\n")
    cn=Text(wr2,text=name)
    clas=Text(wr2,text=classs)
    race=Text(wr2,text=race)
    x=Text(wr2,text=xp)

    #The Ability Score section of inputes all in Text Boxes
    abs=Text(wr2, text="\n\nAbility Scores")
    abs=Text(wr2, text=st,size=6)
    abs=Text(wr2, text=dex,size=6)
    abs=Text(wr2, text=con,size=6)
    abs=Text(wr2, text=intt,size=6)
    abs=Text(wr2, text=wis,size=6)
    abs=Text(wr2, text=cha,size=6)

    #Calculate Skills
    


    kille=PushButton(wr2,text="Exit",command=kill)
   
    


# def readApp():
#     reader = SimpleMFRC522()
#     try:
#          id, text = reader.read()
#          print(id)
#          print(text)
#     finally:
#          GPIO.cleanup()


#Create the write
def writeApp():

    
    wr=Window(app, title="DND RFID WRITE", bg="green", height=800)
    
    abs=Text(wr,text="\n\n")
    cn=TextBox(wr,text="Enter Name",width=24)
    clas=Combo(wr, options=["Select Class","Knight", "Wizard", "Barbarian"])
    race=Combo(wr, options=["Select Race","Human", "Elf", "Dwarf"])
    xp=TextBox(wr,text="Enter XP",width=15)
    abs=Text(wr, text="\n\nAbility Scores")

    abs=Text(wr, text="STR",size=6)
    st=TextBox(wr)
    
    abs=Text(wr, text="DEX",size=6)
    dex=TextBox(wr)
    
    abs=Text(wr, text="CON",size=6)
    con=TextBox(wr)
    
    abs=Text(wr, text="INT",size=6)
    intt=TextBox(wr)
    
    abs=Text(wr, text="WIS",size=6)
    wis=TextBox(wr)
    
    abs=Text(wr, text="CHA",size=6)
    cha=TextBox(wr)

    fwrite=PushButton(wr,text="WRITE!",command=lambda:write2(cn.value,clas.value,race.value,xp.value,st.value,dex.value,con.value,intt.value,wis.value,cha.value))
    
    


intro = Text(app, text="Figure to Text")
Dice = TextBox(app,width=15)
read = PushButton(app, text="Read Figure")
write = PushButton(app, text="Write to Figure",command=writeApp)

app.display()   