from tkinter import Tk, Frame, Menu
from tkinter import messagebox

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
        self.parent = parent        
        self.initUI()
        
    def initUI(self):
        self.parent.title("Simple menu")
        
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
        #fileMenu = Menu(menubar)
        fileMenu = Menu(menubar, tearoff=0)  # убирает пунктирную линию свертки меню
        menubar.add_cascade(label="File", menu=fileMenu)

        submenu = Menu(fileMenu)
        submenu.add_command(label="New feed")
        submenu.add_command(label="Bookmarks")
        submenu.add_command(label="Mail")

        fileMenu.add_cascade(label='Import', menu=submenu, underline=0)
        fileMenu.add_command(label="Mess", command=self.clicked1)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.onExit)
 
    def onExit(self):
        self.quit()

    def clicked1(self):
        res = messagebox.askyesnocancel('Заголовок', 'Текст')
        return res
 
def main():
    root = Tk()
    root.geometry("250x150+300+300")
    app = Example(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()
