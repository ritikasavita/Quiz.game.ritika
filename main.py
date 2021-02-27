import tkinter
from tkinter import *
import random


#======================= ROOT WINDOW CREATION ===============================

root = tkinter.Tk()
root.title("Quiz")
root.geometry('700x500')
root.config(background="#ffffff")
root.resizable(False,False)



#===================== QUESION=====================================

Question = [
    "the First Prime minister of Bangladesh was ?",
    "The longest river in the world ?",
    "The longest highway in the world ?",
    "The  country that accounts for nearly one third of the total teak production of the world is ?",
    "The largest coffee growing country in the world is ?",
    "Which separate Pakistan and Afghanistan is ?",
    "The country which ranks second in the terms of land area is ?",
    "Which one is the Smallest Ocean in the World ?",
    "who has been recently named as the new ruler/sultan of Oman?",
    "Which One is the first artificial satellite to orbit Earth ?"
]

#=========================== SELECTED CHOICE ANSWER ==============================

selected_Answer = [
    ["Mahummed Mansur Ali","Mujibar Rehman","AturRahman Khan","Mouded Ahmed"],
    ["Nile","Amazon","Missouri","Yangtze"],
    ["Trans canada","Pan american highway","Trans siberian highway","Golden quadrilateral"],
    ["India","Thailand","Laos","Myanmar"],
    ["Vietnam","Colombia","Indonesia","Brazil"],
    ["Macmohan line","Redcliffe line","Durand line","Sir creek"],
    ["Russia","Canada","China","United States"],
    ["Indian Ocean","Pacific Ocean","Atlantic Ocean","Arctic Ocean"],
    ["Qusem solemani","Quboos bin said al said","Haitham bin Tariq","Mahjoob Zweiri"],
    ["sputniki 1","Explorer 1","Vanguard 1","Discoverer 1"]
]

#============================= RIGHT ANSWER ==========================================

answer=[1,0,1,3,3,2,1,3,2,0]

#====================== FOR APPEND RANDOM INDEXES ====================================

index = []


def gen():

    global index
    while(len(index)<5):
        x = random.randint(0,9)
        if x in index:
            continue
        else:

            index.append(x)


#=========================== SHOWING RESULT =============================================

def result(score):

    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelimg2 = Label(
        root,
        background="#ffffff",


    )
    labelimg2.pack(pady=(20,20))

    labelresulttext=Label(
        root,
        font=("Times",24,"bold"),
        width=100,
        background = "#900C3F"
    )
    labelresulttext.pack()
    
    
    if score >= 20:
        img3=PhotoImage(file="great.png")
        labelimg2.configure(image = img3)
        labelimg2.image = img3
        labelresulttext.configure(text="You are Excellent")
    
    elif score<20 and score >=10:
        img3=PhotoImage(file="ok.png")
        labelimg2.configure(image=img3)
        labelimg2.image=img3
        labelresulttext.configure(text="you are Good!")

    else:
        img3=PhotoImage(file="bad.png")
        labelimg2.configure(image=img3)
        labelimg2.image=img3
        labelresulttext.configure(text="you Should work hard!")


#======================= FOR CALCULATING TOTAL MARKS =====================================


def calc():
    global User_answer,answer,index
    x=0
    score=0
    for i in index:
        if User_answer[x]==answer[i]:
            score=score+5
        x=x+1
    print(score)
    result(score)


#============================== SELECTED USER ANSWER / CHANGING QUESTION ==============================

global User_answer
User_answer=[]
ques = 1
def selected():
    global radiovar,User_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    User_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=Question[index[ques]])
        r1['text'] = selected_Answer[index[ques]][0]
        r2['text'] = selected_Answer[index[ques]][1]
        r3['text'] = selected_Answer[index[ques]][2]
        r4['text'] = selected_Answer[index[ques]][3]
        ques += 1
    else:
        calc()


#============================= QUESTION /ANSWER SESSION ================================ 

def labelQuestion():

    global lblQuestion,r1,r2,r3,r4


    lblQuestion = Label(
        root,
        text=Question[index[0]],
        font=("Times",14,"bold"),
        background="#33FFE5",
        width=500,
        justify="center",
        wraplength = 400
    
    )
    lblQuestion.pack(pady=(50,20))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1=Radiobutton(
        root,
        text=selected_Answer[index[0]][0],
        value=0,
        variable=radiovar,
        background="#ffffff",
        command=selected,
        font = ("Times",14,"bold")
    )
    r1.pack(pady=(0,30))

    r2=Radiobutton(
        root,
        text=selected_Answer[index[0]][1],
        value=1,
        variable=radiovar,
        background="#ffffff",
        command=selected,
        font = ("Times",14,"bold") 
    )
    r2.pack(pady=(0,30))

    r3=Radiobutton(
        root,
        text=selected_Answer[index[0]][2],
        value=2,
        variable=radiovar,
        background="#ffffff",
        command=selected,
        font = ("Times",14,"bold")
    )
    r3.pack(pady=(0,30))

    r4=Radiobutton(
        root,
        text=selected_Answer[index[0]][3],
        value=3,
        variable=radiovar,
        background="#ffffff",
        command=selected,
        font = ("Times",14,"bold") 
    )
    r4.pack()




#============================ FRONT WINDOW =======================================
    

def btnpress():
    labelimg1.destroy(),
    labelinst.destroy(),
    labelrules.destroy(),
    labeltext.destroy(),
    btnstart.destroy(),
    gen()
    labelQuestion()

img1=PhotoImage(file="transparentGradHat.png")

labelimg1 = Label(
    root,
    image=img1,
    background="#ffffff"
)
labelimg1.pack()

labeltext = Label(
    root,
    text="QUIZ GAME",
    font=("Comic sans MS",24,"bold"),
    background="#ffffff"
)
labeltext.pack(pady=(0,20))

img2=PhotoImage(file="Frame.png")

btnstart=Button(
    root,
    image=img2,
    background="#ffffff",
    relief=FLAT,
    border=0,
    command=btnpress
    
)
btnstart.pack()

labelinst=Label(
    root,
    text="click on start button\n and read the instructions carefully",
    justify=CENTER,
    font=("Consolas",12),
    background="#ffffff"
)
labelinst.pack(pady=(5,86))

labelrules=Label(
    root,
    text=("There is five questions\nyou can select your answer by click on radiobutton\nOnce clicking the radio button it would be your final answer\nSo think before select"),
    width=100,
    font=("Times new roman",14),
    background="#000000",
    foreground="#FACA2F"
)
labelrules.pack()

root.mainloop()