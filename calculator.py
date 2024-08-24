from tkinter import *

def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)

def btnclear():
    global val
    val=""
    data.set("")
def btnequal():
    global val
    result=str(eval(val))
    data.set(result)
root=Tk()
root.title("my calculator")
root.geometry("361x381+500+200")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btn_add=Button(root,text="+",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("+"))
btn_add.grid(row=1,column=3)
btn4=Button(root,text="4",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btn_mul=Button(root,text="x",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("*"))
btn_mul.grid(row=2,column=3)
btn1=Button(root,text="1",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btn_sub=Button(root,text="-",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("-"))
btn_sub.grid(row=3,column=3)
btnc=Button(root,text="C",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btnc.grid(row=4,column=0)
btn0=Button(root,text="0",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick(0))
btn0.grid(row=4,column=1)
btn_div=Button(root,text="/",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnclick("/"))
btn_div.grid(row=4,column=2)
btn_equal=Button(root,text="=",font=("Artiel",12,"bold"),bd=12,height=2,width=6,command=btnequal)
btn_equal.grid(row=4,column=3)
root.mainloop()

