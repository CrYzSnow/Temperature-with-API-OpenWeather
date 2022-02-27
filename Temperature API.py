from json.tool import main
import requests
import tkinter
from tkinter import ttk
import tkinter.font as tkfont

with open("key") as file :
    key = file.read()

with open("villes") as file :
    villes = file.read().split(" ")

ville = villes[0]

def ChoixVille(event):
    global ville
    ville = listeVille.get()
    Actualiser()

def GetTemp():
    return str(((requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ville+"&units=metric&appid="+key)).json())["main"]["temp"]) + " °C"
    
def Actualiser():
    Temperature.config(text=GetTemp())
    print("Actualisé !")

fenetre = tkinter.Tk()
fenetre.title("Température")

fontTitre = tkfont.Font(size=12,weight="bold")
Label = tkinter.Label(fenetre, text="Choisissez une ville et une heure :",height=3,font=fontTitre)
Label.grid(column=0,row=0,padx=5)

listeVille = ttk.Combobox(fenetre,state="readonly",values=villes,width=13)
listeVille.bind("<<ComboboxSelected>>",ChoixVille)
listeVille.grid(column=0,row=1)
listeVille.current(0)

boutonAct = tkinter.Button(fenetre,text='Actualiser',command=Actualiser)
boutonAct.grid(pady=12,column=0,row=2)

fontTemp = tkfont.Font(size=12)
Temperature = tkinter.Label(fenetre,text=GetTemp(),anchor='center',font=fontTemp)
Temperature.grid(column=0,row=3)

fenetre.mainloop()