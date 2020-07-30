from tkinter import *
from tkinter import messagebox

t=Tk()
t.geometry("390x520")
t.resizable(0,0)
t.title("Tic Tac")
#t.iconbitmap(r'favicon.ico')



b=StringVar()
click=True

#function for printing X and O on the buttons

def show(b):
	global click
	if b["text"]=="" and click==True:
		b["text"]="X"
		click=False
		scorekeeper()
	elif b["text"]=="" and click==False:
		b["text"]="O"
		click=True
		scorekeeper()

#condition for winnig games

def scorekeeper():
	if	B1["text"]=="O" and B2["text"]=="O" and B3["text"]=="O":
		B1.configure(background="light green")
		B2.configure(background="light green")
		B3.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B1["text"]=="X" and B2["text"]=="X" and B3["text"]=="X":
		B1.configure(background="pink")
		B2.configure(background="pink")
		B3.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")
	
	if	B4["text"]=="O" and B5["text"]=="O" and B6["text"]=="O":
		B4.configure(background="light green")
		B5.configure(background="light green")
		B6.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B4["text"]=="X" and B5["text"]=="X" and B6["text"]=="X":
		B4.configure(background="pink")
		B5.configure(background="pink")
		B6.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")
	
	if	B7["text"]=="O" and B8["text"]=="O" and B9["text"]=="O":
		B7.configure(background="light green")
		B8.configure(background="light green")
		B9.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B7["text"]=="X" and B8["text"]=="X" and B9["text"]=="X":
		B7.configure(background="pink")
		B8.configure(background="pink")
		B9.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")

	if	B1["text"]=="O" and B4["text"]=="O" and B7["text"]=="O":
		B1.configure(background="light green")
		B4.configure(background="light green")
		B7.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B1["text"]=="X" and B4["text"]=="X" and B7["text"]=="X":
		B1.configure(background="pink")
		B4.configure(background="pink")
		B7.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")
	
	if	B2["text"]=="O" and B5["text"]=="O" and B8["text"]=="O":
		B2.configure(background="light green")
		B5.configure(background="light green")
		B8.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B2["text"]=="X" and B5["text"]=="X" and B8["text"]=="X":
		B2.configure(background="pink")
		B5.configure(background="pink")
		B8.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")
	
	if	B3["text"]=="O" and B6["text"]=="O" and B9["text"]=="O":
		B3.configure(background="light green")
		B6.configure(background="light green")
		B9.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B3["text"]=="X" and B6["text"]=="X" and B9["text"]=="X":
		B3.configure(background="pink")
		B6.configure(background="pink")
		B9.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")

	if	B1["text"]=="O" and B5["text"]=="O" and B9["text"]=="O":
		B1.configure(background="light green")
		B5.configure(background="light green")
		B9.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B1["text"]=="X" and B5["text"]=="X" and B9["text"]=="X":
		B1.configure(background="pink")
		B5.configure(background="pink")
		B9.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")
	
	if	B3["text"]=="O" and B5["text"]=="O" and B7["text"]=="O":
		B3.configure(background="light green")
		B5.configure(background="light green")
		B7.configure(background="light green")
		n=float(playero.get())
		score=(n+1)
		playero.set(score)
		messagebox.showinfo("Congratulations..","Player O Wins game...")

	if	B3["text"]=="X" and B5["text"]=="X" and B7["text"]=="X":
		B3.configure(background="pink")
		B5.configure(background="pink")
		B7.configure(background="pink")
		n=float(playerx.get())
		score=(n+1)
		playerx.set(score)
		messagebox.showinfo("Congratulations..","Player X Wins game...")

#Function for Reset game....

def reset():
	B1['text']=""
	B2['text']=""
	B3["text"]=''
	B4["text"]=''
	B5["text"]=''
	B6["text"]=''
	B7["text"]=''
	B8["text"]=''
	B9["text"]=''

	B1.configure(background="white")
	B2.configure(background="white")
	B3.configure(background="white")
	B4.configure(background="white")
	B5.configure(background="white")
	B6.configure(background="white")
	B7.configure(background="white")
	B8.configure(background="white")
	B9.configure(background="white")

#function for new game....

def new_start():
	reset()
	playerx.set(0)
	playero.set(0)

#frame1 and frame 2

frame3=Frame(t,bd=5,width=390,height=50,bg="pink",relief=RIDGE)
frame3.pack(side=TOP)

frame1=Frame(t,bd=20,width=400,height=400,bg="pink",relief=RIDGE)
frame1.pack(side=TOP)

frame2=Frame(t,bd=5,width=390,height=100,bg="pink",relief=RIDGE)
frame2.pack(side=BOTTOM)

L3=Label(frame3,text="Tic Tok",font="Times 26 bold",width=20,bg="pink",relief=RIDGE,bd=10)
L3.pack()


#Buttons for tictok....

B1=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B1))
B1.grid(row=0,column=0,sticky=S+N+E+W)

B2=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B2))
B2.grid(row=0,column=1,sticky=S+N+E+W)

B3=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B3))
B3.grid(row=0,column=2,sticky=S+N+E+W)

B4=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B4))
B4.grid(row=1,column=0,sticky=S+N+E+W)

B5=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B5))
B5.grid(row=1,column=1,sticky=S+N+E+W)

B6=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B6))
B6.grid(row=1,column=2,sticky=S+N+E+W)

B7=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B7))
B7.grid(row=2,column=0,sticky=S+N+E+W)

B8=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B8))
B8.grid(row=2,column=1,sticky=S+N+E+W)

B9=Button(frame1,text="",width=5,height=2,bg="white",font="Times 26 bold",command=lambda:show(B9))
B9.grid(row=2,column=2,sticky=S+N+E+W)

#Variable for players

playerx=IntVar()
playero=IntVar()

#for set value....

playerx.set(0)
playero.set(0)

#Labels and Entry for player X

L1=Label(frame2,text="Player X",font=("Arial",15,"bold"),padx=2,pady=3,bg="Cadet Blue",width=10)
L1.grid(row=0,column=0,sticky=W)
E1=Entry(frame2,textvariable=playerx,font=("Arial",15,"bold"),bd=2,fg="black",width=10)
E1.grid(row=0,column=1)

#Labels and Entry for player O

L2=Label(frame2,text="Player O",font=("Arial",15,"bold"),padx=2,pady=3,bg="Cadet Blue",width=10)
E2=Entry(frame2,textvariable=playero,font=("Arial",15,"bold"),bd=2,fg="black",width=10)
E2.grid(row=1,column=1)
L2.grid(row=1,column=0,sticky=S)

#reset button
resetb=Button(frame2,text="Reset",font=("Arial 13 bold"),width=12,command=reset)
resetb.grid(row=0,column=2,sticky=E)

#new start button
newstartb=Button(frame2,text="New Start",font=("Arial 13 bold"),width=12,command=new_start)
newstartb.grid(row=1,column=2,sticky=E)


#mainloop for holding main window
t.mainloop()