from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT
from tkinter.ttk import Frame, Label, Entry, Button
 
class Example(Frame):
   def __init__(self, parent):
     Frame.__init__(self, parent)
  
     self.parent = parent
     self.initUI()
  
   def initUI(self):
     self.parent.title("Review")
     self.pack(fill=BOTH, expand=True)

     frame0 = Frame(self)
     frame0.pack(fill=X)

     quitButton = Button(frame0, text="Close", command=self.quit,width=7)
     quitButton.pack(side=RIGHT, padx=5, pady=5)
  
     frame1 = Frame(self)
     frame1.pack(fill=X)
  
     lbl1 = Label(frame1, text="Title", width=7)
     lbl1.pack(side=LEFT, padx=5, pady=5)
  
     entry1 = Entry(frame1)
     entry1.pack(fill=X, padx=5, expand=True)
    
     frame2 = Frame(self)
     frame2.pack(fill=X)
  
     lbl2 = Label(frame2, text="Author", width=7)
     lbl2.pack(side=LEFT, padx=5, pady=5)
  
     entry2 = Entry(frame2)
     entry2.pack(fill=X, padx=5, expand=True)
  
     frame3 = Frame(self)
     frame3.pack(fill=BOTH, expand=True)
  
     lbl3 = Label(frame3, text="Review", width=7)
     lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
  
     txt = Text(frame3)
     txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
     
  
root = Tk()
root.geometry("300x300+300+300")
app = Example(root)
root.mainloop() 