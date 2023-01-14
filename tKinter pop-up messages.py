from tkinter import *

root = Tk()
root.title('Helful TIP')
root.iconbitmap("images/wQ.png")
root.geometry('200x200')

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title('Chess Training App')
    pop.geometry('250x150')
    pop.config(bg='white')

    global me
    me = PhotoImage(file="images/wQ.png")

    

    pop_label = Label(pop, text='Press to continue', bg='green')
    pop_label.pack(pady=10)
    

button = Button(root, text='You are able to move the pawn', command=clicker)
button.pack(pady=50)

root.mainloop()
