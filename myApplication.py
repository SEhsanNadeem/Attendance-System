import tkinter as tk
import os
import shutil

class myApplication():

    def __init__(self, master):
        self.master = master

        pageLabel = tk.Label(self.master, text = "MAIN MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        pageLabel.place(x = 400, y = 0)

        loginBtn = tk.Button(self.master, text = "LOGIN", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.login(self.master))
        loginBtn.place(x = 500, y = 200)

        instructBtn = tk.Button(self.master, text = "INSTRUCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.instruct(self.master))
        instructBtn.place(x = 500, y = 300)

        exitBtn = tk.Button(self.master, text = "EXIT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(self.master))
        exitBtn.place(x = 500, y = 400)

    def instruct(self, root):

        instructPage = tk.Toplevel(root)
        instructPage.title("Instructions")
        instructPage.configure(bg = "black")
        instructPage.wm_state("zoomed")

        instructLabel = tk.Label(instructPage, text = "INSTRUCTIONS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        instructLabel.place(x = 400, y = 0)

        instructions = tk.Label(instructPage, bg = 'black', fg='yellow', font='Times 14 italic', text=
        """ This is the instructions section. This application acts as a reliable and quick
            source of file transmission between students and teachers. Through this app,
            teachers can easily send assignments and/or any other kind of file, e.g. tutorial
            video or notes to the desired student. Moreover, the students can also send
            their completed assignments to their respective teachers. Both the students and
            teachers can access their accounts using the id Number/ roll Number assigned
            to them by the Management Staff. Their is also a section for viewing the
            recieved files by a person, telling which file was sent to him/her and by whom.
            Another feature of this Application is that it allows Students to view topics
            updated by different teachers on their subjects. Thus, in short this Application
            provides easy file transmission and management for students and teachers and also
            provides a source of reviewing various topics of various subjects as per updated
            by the subject teachers.....................................................""" ,borderwidth=10, relief=tk.RAISED)
        instructions.place(x = 200, y = 100, width= 750)
        
        backBtn = tk.Button(instructPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(instructPage))
        backBtn.place(x = 500, y = 500)
    
    def login(self, root):

        loginPage = tk.Toplevel(root)
        loginPage.title("Login Panel")
        loginPage.configure(bg = "black")
        loginPage.wm_state("zoomed")

        loginLabel = tk.Label(loginPage, text = "LOGIN PANEL", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        loginLabel.place(x = 400, y = 0)

        signinBtn = tk.Button(loginPage, text = "SIGNIN", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.signin(self.master))
        signinBtn.place(x = 500, y = 200)
        
        backBtn = tk.Button(loginPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(loginPage))
        backBtn.place(x = 500, y = 300)
        
    def signin(self, root):

        signinPage = tk.Toplevel(root)
        signinPage.title("SignIn Account")
        signinPage.configure(bg = "black")
        signinPage.wm_state("zoomed")

        signinLabel = tk.Label(signinPage, text = "SIGNIN ACCOUNT", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        signinLabel.place(x = 400, y = 0)

        idLabel = tk.Label(signinPage, text = "Enter your ID number: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        idLabel.place(x = 100, y = 100, width = 500)
        
        idEntry = tk.Entry(signinPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        idEntry.place(x = 650, y = 100)

        usernameLabel = tk.Label(signinPage, text = "Enter your username: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        usernameLabel.place(x = 100, y = 200, width = 500)
        
        usernameEntry = tk.Entry(signinPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        usernameEntry.place(x = 650, y = 200)

        passwordLabel = tk.Label(signinPage, text = "Enter your password: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        passwordLabel.place(x = 100, y = 300, width = 500)
        
        passwordEntry = tk.Entry(signinPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        passwordEntry.place(x = 650, y = 300)

        studentBtn = tk.Button(signinPage, text = "STUDENT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.checkFile('studentUsers.txt', usernameEntry.get(), passwordEntry.get(), idEntry.get()))
        studentBtn.place(x = 500, y = 400)

        teacherBtn = tk.Button(signinPage, text = "TEACHER", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.checkFile('teacherUsers.txt', usernameEntry.get(), passwordEntry.get(), idEntry.get()))
        teacherBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(signinPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(signinPage))
        backBtn.place(x = 500, y = 600)

    def checkFile(self, filename, user, passw, idNum):
        with open(filename) as f:
            f1 = f.read().split('\n')
            if str(user + ',' + idNum) in f1:
                f = open('pass' + filename)
                f2 = f.read().split('\n')
                if str(passw + ',' + idNum) in f2:
                    if filename == 'studentUsers.txt':
                        optPage = StudentOptions(self.master, idNum)
                    elif filename == 'teacherUsers.txt':
                        optPage = TeacherOptions(self.master, idNum)
                else:
                    mes = Message(self.master, "Invalid Password Entered")
            else:
                mes = Message(self.master, "Invalid Username or ID Entered")
    
    def delete(self, root):
         root.destroy()
        

class Message():

    def center(self, root):
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def __init__(self, master, text):
        self.master = master
        self.text = text
        
        message = tk.Toplevel(self.master)
        message.title('Message')
        self.center(message)
        message.configure(bg = 'black')
        messageLabel = tk.Label(message, bg='black', fg='yellow', text=self.text , font='Times 10 italic')
        messageLabel.place(x = 0, y = 40, width = 200)
        okBtn = tk.Button(message, bg='black', fg='yellow', text='OK', borderwidth=4, relief=tk.RAISED, command= lambda: self.delete(message))
        okBtn.place(x = 50, y = 100, width = 50)

    def delete(self, root):
        root.destroy()

class StudentOptions():

    def __init__(self, master, user):
        self.master = master
        self.user = user
        
        optPage = tk.Toplevel(self.master)
        optPage.title("App Options")
        optPage.configure(bg = "black")
        optPage.wm_state("zoomed")

        optLabel = tk.Label(optPage, text = "STUDENT MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        optLabel.place(x = 400, y = 0)

        sendBtn = tk.Button(optPage, text = "SEND FILE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.send(self.master))
        sendBtn.place(x = 500, y = 200)

        recieveBtn = tk.Button(optPage, text = "VIEW RECIEVED", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.recieve(self.master))
        recieveBtn.place(x = 500, y = 300)

        topicsBtn = tk.Button(optPage, text = "STUDY TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topics(self.master))
        topicsBtn.place(x = 500, y = 400)
        
        exitBtn = tk.Button(optPage, text = "LOGOUT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(optPage))
        exitBtn.place(x = 500, y = 500)

    def send(self, root):

        sendPage = tk.Toplevel(root)
        sendPage.title("Send Files")
        sendPage.configure(bg = "black")
        sendPage.wm_state("zoomed")

        sendLabel = tk.Label(sendPage, text = "SEND FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        sendLabel.place(x = 400, y = 0)

        fileLabel = tk.Label(sendPage, text = "Enter the filenaem to send: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        fileLabel.place(x = 100, y = 200, width = 500)
        
        fileEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        fileEntry.place(x = 650, y = 200)

        recieverLabel = tk.Label(sendPage, text = "Enter the user to send to: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        recieverLabel.place(x = 100, y = 300, width = 500)
        
        recieverEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        recieverEntry.place(x = 650, y = 300)

        sendfileBtn = tk.Button(sendPage, text = "SEND", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.sendFile(str(fileEntry.get()),recieverEntry.get()))
        sendfileBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(sendPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(sendPage))
        backBtn.place(x = 500, y = 600)

    def recieve(self, root):

        recievePage = tk.Toplevel(root)
        recievePage.title("Recieved Files")
        recievePage.configure(bg = "black")
        recievePage.wm_state("zoomed")

        recieved = self.readfile('D:/Hassan Files/Python Programming/OOP Semester Project/studentUsers/' + str(self.user) + '/recieved.txt')

        recieveLabel = tk.Label(recievePage, text = "RECIEVED FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        recieveLabel.place(x = 400, y = 0)

        reciever = tk.Label(recievePage, text = recieved, bg = "black", fg = "yellow", bd = 16, font = "Times 10 italic", relief = tk.RAISED)
        reciever.place(x = 200, y = 200, width = 500)

        backBtn = tk.Button(recievePage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(recievePage))
        backBtn.place(x = 500, y = 600)

    def topics(self, root):

        topicsPage = tk.Toplevel(root)
        topicsPage.title("Topics")
        topicsPage.configure(bg = "black")
        topicsPage.wm_state("zoomed")

        topicsLabel = tk.Label(topicsPage, text = "STUDY TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicsLabel.place(x = 400, y = 0)

        OOPBtn = tk.Button(topicsPage, text = "OOP", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.OOP(self.master))
        OOPBtn.place(x = 500, y = 100)
        
        DAABtn = tk.Button(topicsPage, text = "DAA", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DAABtn.place(x = 500, y = 200)

        DSBtn = tk.Button(topicsPage, text = "DS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DSBtn.place(x = 500, y = 300)

        backBtn = tk.Button(topicsPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicsPage))
        backBtn.place(x = 500, y = 400)
        
    def sendFile(self, filename, dest):

        DEST = r'D:/Hassan Files/Python Programming/OOP Semester Project/teacherUsers/'  +  dest
        SOURCE = r'D:/Hassan Files/Python Programming/OOP Semester Project/studentUsers/' + str(self.user)

        for root, subdirs, files in os.walk(SOURCE):

            if str(filename) in files:
                path = os.path.join(root, filename)
                shutil.copy(path, DEST)

                f = open(DEST + '/' + 'recieved.txt', 'a') 
                sentFile = str(filename) + ' sent by ' + str(self.user) + '\n'
                f.write(sentFile)
            else:
                print("Invalid File Entry")

    def readfile(self, filename):
        with open(filename) as f:
            return f.read()

    def OOP(self, root):

        OOPPage = tk.Toplevel(root)
        OOPPage.title("OOP Topics")
        OOPPage.configure(bg = "black")
        OOPPage.wm_state("zoomed")

        OOPLabel = tk.Label(OOPPage, text = "OOP TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        OOPLabel.place(x = 400, y = 0)

        ClassBtn = tk.Button(OOPPage, text = "Classes", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.Class(self.master))
        ClassBtn.place(x = 500, y = 100)
        
        InhBtn = tk.Button(OOPPage, text = "Inheritance", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        InhBtn.place(x = 500, y = 200)

        PolyBtn = tk.Button(OOPPage, text = "Polymorphism", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        PolyBtn.place(x = 500, y = 300)

        backBtn = tk.Button(OOPPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(OOPPage))
        backBtn.place(x = 500, y = 400)

    def Class(self, root):

        classPage = tk.Toplevel(root)
        classPage.title("About Class")
        classPage.configure(bg = "black")
        classPage.wm_state("zoomed")

        definition = self.readfile('D:\Hassan Files\Python Programming\OOP Semester Project\Study Topics\OOP\Class.txt')

        classLabel = tk.Label(classPage, text = "ABOUT CLASSES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        classLabel.place(x = 400, y = 0)

        defLabel = tk.Label(classPage, text = definition, bg = "black", fg = "yellow", bd = 16, font = "Times 20 italic", relief = tk.RAISED)
        defLabel.place(x = 250, y = 200, width = 1000)

        backBtn = tk.Button(classPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(classPage))
        backBtn.place(x = 500, y = 600)
        
    def delete(self, root):
        root.destroy()

class TeacherOptions():

    def __init__(self, master, user):
        self.master = master
        self.user = user
        
        optPage = tk.Toplevel(self.master)
        optPage.title("App Options")
        optPage.configure(bg = "black")
        optPage.wm_state("zoomed")

        optLabel = tk.Label(optPage, text = "TEACHER MENU", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        optLabel.place(x = 400, y = 0)

        sendBtn = tk.Button(optPage, text = "SEND FILE", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.send(self.master))
        sendBtn.place(x = 500, y = 200)

        recieveBtn = tk.Button(optPage, text = "VIEW RECIEVED", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.recieve(self.master))
        recieveBtn.place(x = 500, y = 300)

        topicsBtn = tk.Button(optPage, text = "EDIT TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.topics(self.master))
        topicsBtn.place(x = 500, y = 400)
        
        exitBtn = tk.Button(optPage, text = "LOGOUT", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(optPage))
        exitBtn.place(x = 500, y = 500)

    def send(self, root):

        sendPage = tk.Toplevel(root)
        sendPage.title("Send Files")
        sendPage.configure(bg = "black")
        sendPage.wm_state("zoomed")

        sendLabel = tk.Label(sendPage, text = "SEND FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        sendLabel.place(x = 400, y = 0)

        fileLabel = tk.Label(sendPage, text = "Enter the filenaem to send: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        fileLabel.place(x = 100, y = 200, width = 500)
        
        fileEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        fileEntry.place(x = 650, y = 200)

        recieverLabel = tk.Label(sendPage, text = "Enter the user to send to: ", bg = "black", fg = "yellow", bd = 16, font = "Times 28 bold italic", relief = tk.RAISED)
        recieverLabel.place(x = 100, y = 300, width = 500)
        
        recieverEntry = tk.Entry(sendPage, bg = "black", fg = "yellow", font = "Times 28 italic")
        recieverEntry.place(x = 650, y = 300)

        sendfileBtn = tk.Button(sendPage, text = "SEND", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.sendFile(str(fileEntry.get()),recieverEntry.get()))
        sendfileBtn.place(x = 500, y = 500)
        
        backBtn = tk.Button(sendPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(sendPage))
        backBtn.place(x = 500, y = 600)

    def recieve(self, root):

        recievePage = tk.Toplevel(root)
        recievePage.title("Recieved Files")
        recievePage.configure(bg = "black")
        recievePage.wm_state("zoomed")

        recieved = self.readfile('D:/Hassan Files/Python Programming/OOP Semester Project/teacherUsers/' + str(self.user) + '/recieved.txt')

        recieveLabel = tk.Label(recievePage, text = "RECIEVED FILES", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        recieveLabel.place(x = 400, y = 0)

        reciever = tk.Label(recievePage, text = recieved, bg = "black", fg = "yellow", bd = 16, font = "Times 10 italic", relief = tk.RAISED)
        reciever.place(x = 200, y = 200, width = 500)

        backBtn = tk.Button(recievePage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(recievePage))
        backBtn.place(x = 500, y = 600)


    def topics(self, root):

        topicsPage = tk.Toplevel(root)
        topicsPage.title("Topics")
        topicsPage.configure(bg = "black")
        topicsPage.wm_state("zoomed")

        topicsLabel = tk.Label(topicsPage, text = "EDIT TOPICS", bg = "black", fg = "yellow", bd = 16, font = "Times 32 bold italic", relief = tk.RAISED)
        topicsLabel.place(x = 400, y = 0)

        OOPBtn = tk.Button(topicsPage, text = "OOP", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        OOPBtn.place(x = 500, y = 100)
        
        DAABtn = tk.Button(topicsPage, text = "DAA", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DAABtn.place(x = 500, y = 200)

        DSBtn = tk.Button(topicsPage, text = "DS", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED)
        DSBtn.place(x = 500, y = 300)

        backBtn = tk.Button(topicsPage, text = "BACK", bg = "black", fg = "yellow", bd = 16, font = "Times 16 bold italic", relief = tk.RAISED, command = lambda: self.delete(topicsPage))
        backBtn.place(x = 500, y = 400)
    
    
    def sendFile(self, filename, dest):

        DEST = r'D:/Hassan Files/Python Programming/OOP Semester Project/studentUsers/'  +  dest
        SOURCE = r'D:/Hassan Files/Python Programming/OOP Semester Project/teacherUsers/' + str(self.user)

        for root, subdirs, files in os.walk(SOURCE):

            if str(filename) in files:
                path = os.path.join(root, filename)
                shutil.copy(path, DEST)

                f = open(DEST + '/' + 'recieved.txt', 'a') 
                sentFile = str(filename) + ' sent by ' + str(self.user) + '\n'
                f.write(sentFile)
            else:
                print("Invalid File Entry")

    def readfile(self, filename):
        with open(filename) as f:
            return f.read()
    
    def delete(self, root):
        root.destroy()
    
def main():
    main = tk.Tk()
    main.title("My Application")
    main.configure(bg = "black")
    main.wm_state("zoomed")
    run = myApplication(main)
    main.mainloop()

if __name__ == "__main__":
    main()

        
