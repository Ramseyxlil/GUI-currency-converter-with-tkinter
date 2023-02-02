from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Ramsey currency  Converter")
root.minsize(width=700,height=500)
root.geometry("700x500")


Canvas1 = Canvas(root)
    
Canvas1.config(bg="green")
Canvas1.pack(expand=True,fill=BOTH)

def quitroot():
    messagebox.showinfo("Thank you","Thank you for using Ramsey Currency Converter")
    root.destroy()
#define a method to convert the currencies
def currency1():
    try:
        if t.get().lower()=="dollar" and f.get().lower()=="pounds":
            messagebox.showinfo("conversion",( int( a.get())/0.844773, "dollar"))
        elif t.get().lower()=="euros" and f.get().lower()=="pounds":
            messagebox.showinfo("conversion",( int( a.get())/0.875312, "euros"))
        elif t.get().lower()=="naira" and f.get().lower()=="pounds":
            messagebox.showinfo("conversion",( int( a.get())/0.0019,"naira"))
        elif t.get().lower()=="dhiram" and f.get().lower()=="pounds":
            messagebox.showinfo("conversion", (int( a.get())/0.230472,"dhiram"))
        elif t.get().lower()=="rupees" and f.get().lower()=="pounds":
            messagebox.showinfo("conversion", (int( a.get())/0.01051,"rupees"))
        elif t.get().lower()=="euros" and f.get().lower()=="dollar":
            messagebox.showinfo("conversion", (int( a.get())/1.03727,"euros"))
        elif t.get().lower()=="naira" and f.get().lower()=="dollar":
            messagebox.showinfo("conversion",( int( a.get())/0.00226624, "naira"))
        elif t.get().lower()=="dhiram" and f.get().lower()=="dollar":
            messagebox.showinfo("conversion", (int( a.get())/0.272294, "dhiram"))
        elif t.get().lower()=="rupees" and f.get().lower()=="dollar":
            messagebox.showinfo("conversion",( int( a.get())/0.0124,"rupees"))
        elif t.get().lower()=="pounds" and f.get().lower()=="dollar":
            messagebox.showinfo("conversion", (int( a.get())/1.18375,"pounds"))
        elif t.get().lower()=="dollar" and f.get().lower()=="euros":
            messagebox.showinfo("conversion", (int( a.get())/0.964069,"dollar"))
        elif t.get().lower()=="naira" and f.get().lower()=="euros":
            messagebox.showinfo("conversion", (int( a.get())/0.0022,"naira"))
        elif t.get().lower()=="dhiram" and f.get().lower()=="euros":
            messagebox.showinfo("conversion", (int( a.get())/0.262475,"dhiram"))
        elif t.get().lower()=="rupees" and f.get().lower()=="euros":
            messagebox.showinfo("conversion",( int( a.get())/0.011969,"rupees"))
        elif t.get().lower()=="pounds" and f.get().lower()=="euros":
            messagebox.showinfo("conversion",( int( a.get())/1.138758,"pounds"))
        elif t.get().lower()=="dollar" and f.get().lower()=="naira":
            messagebox.showinfo("conversion",( int( a.get())/440.0,"dollar"))
        elif t.get().lower()=="euros" and f.get().lower()=="naira":
            messagebox.showinfo("conversion",( int( a.get())/457.394706,"euros"))
        elif t.get().lower()=="dhiram" and f.get().lower()=="naira":
            messagebox.showinfo("conversion", (int( a.get())/120.0545,"dhiram"))
        elif t.get().lower()=="rupees" and f.get().lower()=="naira":
            messagebox.showinfo("conversion", (int( a.get())/5.47449,"rupees"))
        elif t.get().lower()=="pounds" and f.get().lower()=="naira":
            messagebox.showinfo("conversion", (int( a.get())/520.044697,"pounds"))
        elif t.get().lower()=="dollar" and f.get().lower()=="dhiram":
             messagebox.showinfo("conversion",( int( a.get())/0.272294,"dollar"))
        elif t.get().lower()=="euros" and f.get().lower()=="dhiram":
             messagebox.showinfo("conversion", (int( a.get())/0.262758,"euros"))
        elif t.get().lower()=="naira" and f.get().lower()=="dhiram":
             messagebox.showinfo("conversion", (int( a.get())/119.8559,"naira"))
        elif t.get().lower()=="rupees" and f.get().lower()=="dhiram":
             messagebox.showinfo("conversion", (int( a.get())/21.928928,"rupees"))
        elif t.get().lower()=="pounds" and f.get().lower()=="dhiram":
             messagebox.showinfo("conversion", (int( a.get())/0.229995,"pounds"))
        elif t.get().lower()=="dhiram" and f.get().lower()=="rupees":
             messagebox.showinfo("conversion",( int( a.get())/21.929526 ,"dhiram"))
        elif t.get().lower()=="dollar" and f.get().lower()=="rupees":
             messagebox.showinfo("conversion",( int( a.get())/0.229995,"dollar"))
        elif t.get().lower()=="euros" and f.get().lower()=="rupees":
             messagebox.showinfo("conversion",( int( a.get())/83.550203,"euros"))
        elif t.get().lower()=="naira" and f.get().lower()=="rupees":
             messagebox.showinfo("conversion", (int( a.get())/5.47857,"naira"))
        elif t.get().lower()=="pounds" and f.get().lower()=="rupees":
             messagebox.showinfo("conversion",( int( a.get())/95.143473,"pounds"))
        else:
            messagebox.showerror("invalid input", "The currency you are converting is not possible or is not in our system. check our currency list and  try again!")

    except:
        messagebox.showerror("invalid input", " you can only convert numbers!, please try again")

def clear():
    f.delete(0, "end")
    t.delete(0, "end")
    a.delete(0,"end")

        
headingFrame1 = Frame(root,bg="yellow",bd=5)
headingFrame1.place(relx=0.23,rely=0.1,relwidth=0.5,relheight=0.13)

#heading title
headingLabel = Label(headingFrame1, text="Welcome to \n Ramsey currency conveter", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

descrframe= Frame(root, bg='blue',bd=5 )
descrframe.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.1)

#label
descrlabel = Label(descrframe, text="We only convert the following currencies \n Dollars. Naira. Pounds. Euros. Rupees. Dhiram", bg='white', fg='black', font=('Courier',15))
descrlabel.place(relx=0,rely=0, relwidth=1, relheight=1)



labelFrame = Frame(root,bg='black')
labelFrame.place(relx=0.1,rely=0.44,relwidth=0.8,relheight=0.4)

#currency froms
lb1 = Label(labelFrame,text="currency from : ", fg='white', bg='black',font=('Arial', 10, 'bold'))
lb1.place(relx=0.05,rely=0.2, relheight=0.1)

ff = StringVar()        
f = Entry(labelFrame, textvariable=ff)
f.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.1)
        
# currency to
lb2 = Label(labelFrame,text="Currency to: ",bg='black', fg='white', font=('Arial', 10, 'bold'))
lb2.place(relx=0.05,rely=0.4, relheight=0.1)

tt = StringVar()        
t = Entry(labelFrame, textvariable=tt)
t.place(relx=0.3,rely=0.4, relwidth=0.62, relheight=0.1)

#amount
lb3 = Label(labelFrame,text="Amount : ", bg='black', fg='white',font=('Arial', 10, 'bold'))
lb3.place(relx=0.05,rely=0.6, relheight=0.1)


aa = StringVar()        
a = Entry(labelFrame, textvariable=aa)
a.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.1)

convertBtn = Button(root,text="Convert",bg='yellow', fg='black',command=currency1)
convertBtn.place(relx=0.1,rely=0.88, relwidth=0.18,relheight=0.05)

clearBtn = Button(root,text="Clear",bg='yellow', fg='black', command=clear)
clearBtn.place(relx=0.4,rely=0.88, relwidth=0.18,relheight=0.05)

quitBtn = Button(root,text="Quit",bg='yellow', fg='black', command=quitroot)
quitBtn.place(relx=0.7,rely=0.88, relwidth=0.18,relheight=0.05)
root.mainloop()
        
