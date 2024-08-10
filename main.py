import tkinter as tk
from tkinter import ttk
from tkinter import *


class Window(tk.Tk):
    def __init__(self,size,title):
        super().__init__()

        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0],size[1])
        self.title(title)
        # self.attributes('-alpha',0.85)


        #placing button frame

        self.display_frame = Display_frame(self)
        self.button_frame = Frame_Buttons(self,self.display_frame.text_input)




#crating frame for the widgets

class Display_frame(ttk.Frame):
    def __init__(self,parent):
        super().__init__(master=parent)
        self.pack(expand =True,fill = 'both',side = 'top')
      #display frame
        self.text_input = StringVar()
        self.entry_fild = ttk.Entry(self, textvariable=self.text_input)
        self.entry_fild.pack(expand=True, fill='both',side = 'right')




#frame for the button widget

class Frame_Buttons(ttk.Button):
    def __init__(self,parent,text_input):
        super().__init__(master = parent)
        self.pack(side='bottom',expand = True,fill = 'x',pady=25,padx = 25)

        # self.buttons()
        self.text_input = text_input
        self.funct = Function(self.text_input)
        self.numb_press = self.funct.numb_press
        self.delete = self.funct.delete
        self.clear = self.funct.clear
        self.eval = self.funct.eval

    # def buttons(self):

        button1 = ttk.Button(self, text="1", command=lambda: self.numb_press('1'))
        button2 = ttk.Button(self, text="2", command=lambda: self.numb_press('2'))
        button3 = ttk.Button(self, text="3", command=lambda: self.numb_press('3'))
        button4 = ttk.Button(self, text="4", command=lambda: self.numb_press('4'))
        button5 = ttk.Button(self, text="5", command=lambda: self.numb_press('5'))
        button6 = ttk.Button(self, text="6", command=lambda: self.numb_press('6'))
        button7 = ttk.Button(self, text="7", command=lambda: self.numb_press('7'))
        button8 = ttk.Button(self, text="8", command=lambda: self.numb_press('8'))
        button9 = ttk.Button(self, text="9", command=lambda: self.numb_press('9'))
        button0 = ttk.Button(self, text="0", command=lambda: self.numb_press('0'))
        # opoaration button
        but_add = ttk.Button(self, text="+",command=lambda: self.numb_press('+'))
        but_sub = ttk.Button(self, text="-",command=lambda: self.numb_press('-'))
        but_mul = ttk.Button(self, text="*",command=lambda: self.numb_press('*'))
        but_div = ttk.Button(self, text="/",command=lambda: self.numb_press('/'))
        but_per = ttk.Button(self, text="%",command=lambda: self.numb_press('%'))
        but_bra = ttk.Button(self, text='(',command=lambda: self.numb_press('('))
        but_bra2 = ttk.Button(self, text=')',command=lambda:self.numb_press(')'))
        but_eql = ttk.Button(self, text="=", command=self.eval)
        but_del = ttk.Button(self, text="DEL", command=self.delete)
        but_clr = ttk.Button(self, text="CLR", command=self.clear)

        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)
        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)
        button6.grid(row=1, column=2)
        button7.grid(row=2, column=0)
        button8.grid(row=2, column=1)
        button9.grid(row=2, column=2)
        button0.grid(row=3, column=1)

        but_add.grid(column=3, row=0)
        but_sub.grid(column=3, row=1)
        but_mul.grid(column=3, row=2)
        but_div.grid(column=4, row=0)
        but_del.grid(column=4, row=1)
        but_clr.grid(column=4, row=2)
        but_per.grid(column=3, row=3)
        but_eql.grid(column=4, row=3)
        but_bra.grid(column=0, row=3)
        but_bra2.grid(column=2, row=3)




class Function():
    def __init__(self,text_ver):
        self.text_ver = text_ver


    def numb_press(self,numb):
        self.text_ver.set(self.text_ver.get()+numb)

    def clear(self):
        self.expression = ""
        self.text_ver.set(self.expression)

    def delete(self):
        temp = self.text_ver.get()
        self.text_ver.set(str(temp[:-1]))

    def eval(self):
        try:
            temp = eval(self.text_ver.get())
            self.text_ver.set(str(temp))
        except:
            self.text_ver.set('error')


if __name__ == '__main__':
    app =Window((500,450),'CALCULATOR')
    app.mainloop()