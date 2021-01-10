#Lớp Tk được dùng để tạo cửa sổ, lớp Frame dùng để quản lý các widget.
from tkinter import Tk, Frame, BOTH, RAISED
#create tạo button
from tkinter.ttk import Button, Style
 
class Example(Frame):
     #khởi tạo
     def __init__(self, parent):
          Frame.__init__(self, parent,background='blue')
          #Chúng ta dùng thuộc tính parent để lưu lại đối tượng root.
          self.parent = parent
          #Chúng ta định nghĩa phương thức initUI() dùng để tạo các widget trên cửa sổ.
          self.initUI()
  
     def initUI(self):
          #Phương thức title() sẽ thay đổi tiêu đề cửa sổ.
          self.parent.title("Simple")
          #Phương thức pack() có tác dụng sắp xếp vị trí các widget trước khi gắn chúng lên cửa sổ chính.
          #Tham số fill=BOTH sẽ dãn widget ra theo chiều ngang và chiều rộng, 
          #tức là widget đó sẽ chiếm toàn bộ không gian cửa sổ.
          self.pack(fill=BOTH, expand=1)
          #nút button
          quitButton = Button(self, text="Quit", command=self.quit)
          quitButton.place(x=50, y=50)
#Ở dòng trên chúng ta tạo một cửa sổ và gán vào biến root để quản lý.
root = Tk()
#Phương thức geometry() quy định kích thước cửa sổ và vị trí hiển thị trên màn hình.
#Hai tham số đầu tiên là kích thước cửa sổ, hai phương thức sau là vị trí của cửa sổ trên màn hình.
root.geometry("300x200+200+200")
#Dòng code trên chúng ta tạo một Frame và gắn nó vào cửa sổ chính.
app = Example(root)
root.mainloop()