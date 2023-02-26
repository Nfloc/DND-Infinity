from re import Match
from types import MappingProxyType
from guizero import App, Text, PushButton, TextBox, Combo, Box, Window
from time import sleep
import sys
import random
# import RPi.GPIO as GPIO
# from mfrc522 import SimpleMFRC522



app = App(title="DND RFID", bg="green")

def kill():
    app.destroy()
    

def write2(name,classs,race,xp,st,dex,con,intt,wis,cha,money,armor):

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
    abs=Text(wr2, text="desterity {}".format(dex),size=6)
    abs=Text(wr2, text=con,size=6)
    abs=Text(wr2, text=intt,size=6)
    abs=Text(wr2, text=wis,size=6)
    abs=Text(wr2, text=cha,size=6)
    abs=Text(wr2, text=money,size=6)
    abs=Text(wr2, text=armor,size=6)
    

    #Calculate modifiers

    Mstr = ((st-st%2)/2)-5
    Mdex = ((dex-dex%2)/2)-5
    Mcon = ((con-con%2)/2)-5
    Mint = ((intt-intt%2)/2)-5
    Mwis = ((wis-wis%2)/2)-5
    Mcha = ((cha-cha%2)/2)-5
    if race=="Human":
      Minv+=1
    if race=="elf":
      Mcha = Mcha +1
    if race=="orc":
      Mst = Mst +1
    if race=="Dwarf":
      Mcon+=1

    Mat = Mstr
    Mac = Mdex
    Msn  = Mdex
    Mar  = Mint
    Minv  = Mint
    Mins  = Mwis
    Mhe  = Mwis
    Mpec  = Mwis
    Mpes  = Mcha
    Mde  = Mcha
   
    if classs == "Barbarian":
      Mat = Mat*2 
      Mpec = Mpec*2
    if classs == "Knight":
      Mac = Mac*2 
      Mpes = Mpes*2
    if classs == "Wizard":
      Mar = Mat*2 
      Mhe = Mpec*2  


    #Calculate level
    if int(xp)<300:
      level=2
    elif int(xp)<900:
      level=3
    elif int(xp)<2700:
      level=4
    elif int(xp)<6500:
      level=5
    elif int(xp)<14000:
      level=5
    elif int(xp)<23000:
      level=6
    elif int(xp)<34000:
      level=7
    elif int(xp)<48000:
      level=8
    elif int(xp)<64000:
      level=9
    elif int(xp)<85000:
      level=10
    elif int(xp)<100000:
      level=11
    elif int(xp)<900:
      level=12
    
    abs=Text(wr2, text=armor,size=6)

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

    abs=Text(wr, text="Money",size=6)
    money =TextBox(wr)
    
    abs=Text(wr, text="Armor",size=6)
    armor =TextBox(wr)

    fwrite=PushButton(wr,text="WRITE!",command=lambda:write2(cn.value,clas.value,race.value,xp.value,st.value,dex.value,con.value,intt.value,wis.value,cha.value,money.value,armor.value))
    
def Dice2(nds):
    
    Dc2=Window(app,title="Dice2", bg="green", height=800)
    Rr = random.randint(1,nds)
    abs= Text(Dc2,text =str(Rr),width=24)
    
def Dice():

    Dc=Window(app, title="Roll Dice", bg="green", height=800)

    nds=TextBox(Dc,text="Enter Number of dice sides",width=24)

    fwrite=PushButton(Dc,text="Roll!",command=lambda:Dice2(int(nds.value)))
    

intro = Text(app, text="Figure to Text")
read = PushButton(app, text="Read Figure")
write = PushButton(app, text="Write to Figure",command=writeApp)
Dice_Roll = PushButton(app, text="Roll dice",command=Dice)

app.display()   

