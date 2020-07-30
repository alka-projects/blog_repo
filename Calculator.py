from tkinter import *

t=Tk()
t.geometry("300x435")
t.resizable(0,0)
t.title("Calculator")
t.configure(background="light blue")

#FRAME CREATING

frame1=Frame(t,width=300,bd=10,height=50,bg="gray",relief=RIDGE)
frame1.pack(pady=5)

frame2=Frame(t,width=300,bd=10,height=350,relief=RIDGE)
frame2.pack()

#VARIABLE

num=StringVar()


data=['','/','*','7','8','9','-','4','5','6','+','1','2','3','0','.','=']

def show(b):
	num.set(num.get()+b)
	c=num.get()

def equal():
	try:
		a=num.get()
		num.set(eval(a))
	except:
		num.set("ERROR")

def clear():
	num.set("")

def back():
	i=len(num.get())
	i=i-1
	a=num.get()
	num.set(a[:i])





#ENTRY FOR CALCULATION

entry=Entry(frame1,textvariable=num,font=("Arial",30),bd=2,fg="white",width=30,bg="grey",justify=RIGHT)
entry.pack()

#BUTTONS

b1=Button(frame2,text='AC',font=("Arial",22),width=3,bg='red',command=clear)
b1.grid(row=0,column=0,sticky=W+S+N+E,padx=4,pady=4)

b2=Button(frame2,text='C',font=("Arial",22),width=3,command=back)
b2.grid(row=0,column=1,sticky=W+S+N+E,padx=4,pady=4)

b3=Button(frame2,text=data[1],font=("Arial",22),width=3,command=lambda:show(data[1]))
b3.grid(row=0,column=2,sticky=W+S+N+E,padx=4,pady=4)


b4=Button(frame2,text=data[2],font=("Arial",22),width=3,bg='orange',command=lambda:show(data[2]))
b4.grid(row=0,column=3,sticky=W+S+N+E,padx=4,pady=4)

b5=Button(frame2,text=data[3],font=("Arial",22),width=3,command=lambda:show(data[3]))
b5.grid(row=1,column=0,sticky=W+S+N+E,padx=4,pady=4)

b6=Button(frame2,text=data[4],font=("Arial",22),width=3,command=lambda:show(data[4]))
b6.grid(row=1,column=1,sticky=W+S+N+E,padx=4,pady=4)

b7=Button(frame2,text=data[5],font=("Arial",22),width=3,command=lambda:show(data[5]))
b7.grid(row=1,column=2,sticky=W+S+N+E,padx=4,pady=4)

b8=Button(frame2,text=data[6],font=("Arial",22),width=3,bg='orange',command=lambda:show(data[6]))
b8.grid(row=1,column=3,sticky=W+S+N+E,padx=4,pady=4)


b9=Button(frame2,text=data[7],font=("Arial",22),width=3,command=lambda:show(data[7]))
b9.grid(row=2,column=0,sticky=W+S+N+E,padx=4,pady=4)

b10=Button(frame2,text=data[8],font=("Arial",22),width=3,command=lambda:show(data[8]))
b10.grid(row=2,column=1,sticky=W+S+N+E,padx=4,pady=4)

b11=Button(frame2,text=data[9],font=("Arial",22),width=3,command=lambda:show(data[9]))
b11.grid(row=2,column=2,sticky=W+S+N+E,padx=4,pady=4)

b12=Button(frame2,text=data[10],font=("Arial",22),width=3,bg='orange',command=lambda:show(data[10]))
b12.grid(row=2,column=3,sticky=W+S+N+E,padx=4,pady=4,rowspan=2)

b13=Button(frame2,text=data[11],font=("Arial",22),width=3,command=lambda:show(data[11]))
b13.grid(row=3,column=0,sticky=W+S+N+E,padx=4,pady=4)

b14=Button(frame2,text=data[12],font=("Arial",22),width=3,command=lambda:show(data[12]))
b14.grid(row=3,column=1,sticky=W+S+N+E,padx=4,pady=4)

b15=Button(frame2,text=data[13],font=("Arial",22),width=3,command=lambda:show(data[13]))
b15.grid(row=3,column=2,sticky=W+S+N+E,padx=4,pady=4)

b16=Button(frame2,text=data[14],font=("Arial",22),width=3,command=lambda:show(data[14]))
b16.grid(row=4,column=0,sticky=W+S+N+E,padx=4,pady=4,columnspan=2)

b17=Button(frame2,text=data[15],font=("Arial",22),width=3,command=lambda:show(data[15]))
b17.grid(row=4,column=2,sticky=W+S+N+E,padx=4,pady=4)

b18=Button(frame2,text=data[16],font=("Arial",22),width=3,bg="orange",command=equal)
b18.grid(row=4,column=3,sticky=W+S+N+E,padx=4,pady=4)



t.mainloop()