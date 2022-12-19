import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image

t=tkinter.Tk()





t.title('DATA BASE')

t.geometry('1000x600')

z=Image.open("D:\\Relin.m\\PY PROJECTS\\project\\relin.png")
z=z.resize((1000,600))
z=ImageTk.PhotoImage(z)

pic=tkinter.Label(t,image=z)
pic.place(x=0,y=0)

a=tkinter.Label(text="PERSONAL DATA BASE",bg="White",fg="Black",font=("Lucida Bright",36,'bold'))
a.place(x=190,y=10)



b=tkinter.Label(text=" 1)  First Name -",bg="white",fg="Black",font=("Calibri",15,))
b.place(x=0,y=100)

c=tkinter.Entry(width=30)
c.place(x=180,y=110)


d=tkinter.Label(text=" 2)  Last Name -",bg="white",fg="Black",font=("Calibri",15,))
d.place(x=0,y=150)

e=tkinter.Entry(width=30)
e.place(x=180,y=160)

f=tkinter.Label(text=" 3)  Age -",bg="white",fg="Black",font=("Calibri",15,))
f.place(x=0,y=200)

g=tkinter.Entry(width=30)
g.place(x=180,y=210)

h=tkinter.Label(text=" 4)  Email ID -",bg="white",fg="Black",font=("Calibri",15,))
h.place(x=0,y=250)

i=tkinter.Entry(width=30)
i.place(x=180,y=260)

j=tkinter.Label(text=" 5)  Phone Number -",bg="white",fg="Black",font=("Calibri",15,))
j.place(x=0,y=300)

k=tkinter.Entry(width=30)
k.place(x=180,y=310)

l=tkinter.Label(text=" 6)  Gender -",bg="white",fg="black",font=("Calibri",15,))
l.place(x=0,y=350)

m=tkinter.Entry(width=30)
m.place(x=180,y=360)

n=tkinter.Label(text=" 7)  Location -",bg="white",fg="black",font=("Calibri",15,))
n.place(x=0,y=400)

o=tkinter.Entry(width=30)
o.place(x=180,y=410)


def fun():
    firstname=c.get()
    lastname=e.get()
    age=g.get()
    emailid=i.get()
    phonenumber=k.get()
    gender=m.get()
    location=o.get()

    if(firstname==""or lastname=="" or age=="" or emailid=="" or phonenumber=="" or gender=="" or location==""):
        tkinter.messagebox.showerror("Error Message","Please Complete Fields")

    else:
        import pymysql
    
        x=pymysql.connect(host ="localhost", user = "root", password = "relin", db = "project" )
        cur=x.cursor()
        cur.execute("insert into data values('"+firstname+"','"+lastname+"','"+age+"','"+emailid+"','"+phonenumber+"','"+gender+"','"+location+"')")
        x.commit()
        x.close()
    
        tkinter.messagebox.askyesno("Save","Do You Want to Save")
        tkinter.messagebox.showinfo("Thank You","Thanks For Visiting")
        t.destroy()
    
p=tkinter.Button(text="Submit",fg="black",font=("Calibri",15),command=fun)
p.place(x=500,y=500)








t.mainloop()
