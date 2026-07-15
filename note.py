###      calculette note stagiaire      ###
from tkinter import *
from tkinter import messagebox

root = Tk()

def moy():
    try:
        note1 = float(entry2.get())
        note2 = float(entry3.get())
        note3 = float(entry4.get())
        note4 = float(entry5.get())
    except ValueError:
        messagebox.showwarning("Erreur", "Veuillez entrer des valeurs numeriques valides.")
        return
    
    moy = ((note1*2) + (note2*3) + (note3*2) + (note4*3)) / 10
    my.config(text=moy)


    
    if moy >= 10:
        dec.config(text="admis")
    else:
        dec.config(text="non admis")

    if   moy >= 18:
        men.config(text="excellent")
    elif moy >= 16:
        men.config(text="très bien")
    elif moy >= 14:
        men.config(text="bien")
    elif moy >= 12:
        men.config(text="assez bien")
    elif moy >= 10:
        men.config(text="passable")
    elif moy >= 8:
        men.config(text="echec") 
    else:
        men.config(text="mal")

def nouvel():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    my.config(text="")
    dec.config(text="")
    men.config(text="")

def fermer():
    ask = messagebox.askquestion("fermer", "voulez vous fermer?")
    if ask == "yes":
        root.destroy()


root.geometry("800x500")
root.title("CALCULS")
root.configure(bg="light blue")
label1 = Label(root, text="stagaire", bg="light blue", font=("Arial", 20,"bold"))
label1.place(x=0, y=10)
entry1 = Entry(root, relief="solid", font=("Arial", 20,"bold"))
entry1.place(x=300, y=10)
label2 = Label(root, text="note controles", bg="light blue", font=("Arial", 20,"bold"))
entry1.place(x=300, y=10)
label2 = Label(root, text="note controles", bg="light blue", font=("Arial", 20,"bold"))
label2.place(x=0, y=50)
entry2 = Entry(root, relief="solid", font=("Arial", 20,"bold"))
entry2.place(x=300, y=50)
label3 = Label(root, text="note exam pratique:", bg="light blue", font=("Arial", 20,"bold"))
label3.place(x=0, y=90)
entry3 = Entry(root, relief="solid", font=("Arial", 20,"bold"))
entry3.place(x=300, y=90)
label4 = Label(root, text="note exam theoriques ", bg="light blue", font=("Arial", 20,"bold"))
label4.place(x=0, y=170)
entry4 = Entry(root, relief="solid", font=("Arial", 20,"bold"))
entry4.place(x=300, y=170)

label5 = Label(root, text="note soutenance:", bg="light blue", font=("Arial", 20,"bold"))
label5 = Label(root, text="note soutenance:", bg="light blue", font=("Arial", 20,"bold"))
label5.place(x=0, y=130)
entry5 = Entry(root, relief="solid", font=("Arial", 20,"bold"))
entry5.place(x=300, y=130)


 
nouvel_calcul=Button(root, text="nouvel🆕",bg="green", fg="white", font=("Arial", 20), command=nouvel)
nouvel_calcul.place(x=30, y=440)
fermer=Button(root, text="fermer❌",bg="red", fg="white", font=("Arial", 20), command=fermer)
fermer.place(x=650, y=440)


moyenne=Label(root, text="moyenne:",fg="blue", bg="light blue", font=("Arial", 20,"bold"))
moyenne.place(x=70, y=220)
my=Label(root,text="",font=("Arial", 20),bd=4,relief="ridge",highlightbackground="blue",highlightthickness=2,)
my.place(x=280, y=220, width=200)
decision=Label(root, text="decision:",fg="blue", bg="light blue", font=("Arial", 20,"bold"))
decision.place(x=70, y=270)
dec=Label(root,text="",font=("Arial", 20),bd=4,relief="ridge",highlightbackground="blue",highlightthickness=2,)
dec.place(x=280, y=270, width=200)
mention=Label(root, text="mention:",fg="blue", bg="light blue", font=("Arial", 20,"bold"))
mention.place(x=70, y=320)
men=Label(root,text="",font=("Arial", 20),bd=4,relief="ridge",highlightbackground="blue",highlightthickness=2,)
men.place(x=280, y=320, width=200)
resultat=Button(root, text="resultat✅",fg="purple",bg="yellow", font=("Arial", 20,"bold"), command=moy)   
resultat.place(x=320, y=440)




root.mainloop()

