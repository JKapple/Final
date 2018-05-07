from tkinter import *
import os

creds = 'info.temp'


def Signup():
    global pwordL
    global nameL
    global nameE
    global cust
    global pwordE
    global roots

    roots = Tk()
    roots.title('Welcome')
    intruction = Label(roots,
                       text='Please enter the information required below\n')
    intruction.grid(row=0, column=0,
                    sticky=E)

    nameL = Label(roots, text='First name: ')
    pwordL = Label(roots, text='Last name: ')
    nameE = Label(roots, text='Address: ')
    cust = Label(roots, text='Phone: ')
    pwordE = Label(roots, text='Email: ')





    nameL.grid(row=1, column=0,sticky=W)
    pwordL.grid(row=2, column=0, sticky=W)
    nameE.grid(row=3, column=0,sticky=W)
    cust.grid(row=4, column=0, sticky=W)
    pwordE.grid(row= 5, column = 0, sticky=W)






    nameL = Entry(roots)
    pwordL= Entry(roots)
    nameE = Entry(roots,
                  show='*')
    cust = Entry(roots)
    pwordE = Entry(roots)



    nameL.grid(row=1, column=1)
    pwordL.grid(row=2, column=1)
    nameE.grid(row=3, column=1)
    cust.grid(row=4, column=1)
    pwordE.grid(row=5, column=1)

    signupButton = Button(roots, text='Enter',
                          command=FSSignup)
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()


def FSSignup():
    with open(creds, 'w') as f:
        f.write(
            nameL.get(),
        )#
        f.write('\n')
        f.write(pwordL.get())
        f.write('\n')
        f.write(
            nameE.get()
        )
        f.write('\n')
        f.write(
            cust.get()
        )
        f.write('\n')
        f.write(
            pwordE.get()
        )

        f.close()

    roots.destroy()
    Login()


def Login():
    global nameEL
    global pwordEL
    global rootA

    rootA = Tk()
    rootA.title('Login')

    intruction = Label(rootA, text='Please Login\n')
    intruction.grid(sticky=E)

    nameL = Label(rootA, text='First Name: ')
    pwordL = Label(rootA, text='Last Name: ')
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)

    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='Login',
                    command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)

    rmuser = Button(rootA, text='Delete User', fg='red',
                    command=DelUser)
    rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()


def CheckLogin():
    with open(creds) as f:
        data = f.readlines()
        uname = data[0].rstrip()
        pword = data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword:
        r = Tk()
        r.title(':D')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[+] Logged In')
        rlbl.pack()  #
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Info')
        rlbl.pack()
        r.mainloop()


def DelUser():
    os.remove(creds)  
    rootA.destroy()
    Signup()


if os.path.isfile(creds):
    Login()
else:
    Signup()