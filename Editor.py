# read the file user-req-note
# module import section
from Tkinter import *
from tkFileDialog import *
from tkfontchooser import askfont
from tkFont  import Font
from tkMessageBox import showerror,showinfo,showwarning,askokcancel
from time import sleep
import os #Python standard Module


filename =  None
curdir = "/home/"
curdir = curdir + os.listdir(curdir)[0]       #for Windows Change this to work properly
types = [   ("All Files","*.*"),
            ("Text Documents","*.txt"),
            ("Python Documents","*.py"),
            ("C Doucuments","*.c"),
            ("CPP Documents", "*.cpp"),
            ("Java Documents", "*.java"),
            ("HTML Documents", "*.html / *.htm"),
            ("JavaScript Documents", "*.js"),
            ("CSS Documents", "*.css")
        ]


def info():
    showinfo("Text Editor",'creator --M Venkat')

window = Tk()
window.title("Text Editor")
window.geometry("680x400")
#window.iconbitmap(r"\home\mvs\giles\py\today\gr\images.xpm")
window.minsize(width = 680,height = 400)
#window.maxsize(width = 680,height = 1080)
status = Label(window, text = "",relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

class Test(Text):
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.focus_set()
        self.cur_font_fam = "Times "
        self.cur_font_size = 10
        self.cur_font_slant = "roman" # or "italic"
        self.cur_font_weight = "normal" # or "bold"
        self.cur_font_under = "normal"  # or "underline"
        self.cur_font_overstrike = "normal" # or "overstrike"
        self.bind('<Control-c>', self.copy)                 # checked
        self.bind('<Control-C>',self.copyall)               # checked
        self.bind('<Control-x>', self.cut)                  # checked
        self.bind('<Control-X>',self.cut)                   # checked
        self.bind('<Control-s>',self.saveFile)              #
        self.bind('<Control-n>',self.newFile)               # checked
        self.bind('<Control-o>',self.openFile)              # checked
        self.bind('<Control-S>',self.saveAs)                # checked
        self.bind('<Control-Q>',self.quit)                  # checked
        self.bind('<Control-l>',self.clearscreen)
        self.bind('<Control-a>',self.selectall)             # not working
        self.bind('<Control-f>',self.change_font)           # checked
        self.bind('<Control-F>',self.change_font)
        self.bind('<Button-3>',self.rClicker)               # checked
        self.bind('<Control-y>',self.redo)                  # checked
        self.bind('<Control-Y>',self.redo)
        self.bind('<KeyPress>',self.showrowcol)             #
        self.bind('<KeyRelease>',self.showrowcol)
        self.bind('<KeyPress-Up>',self.showrowcol)                   # checked
        self.bind('<KeyPress-Down>',self.showrowcol)                 # checked
        self.bind('<KeyPress-Left>',self.showrowcol)                 # checked
        self.bind('<KeyPress-Right>',self.showrowcol)                # checked
        self.bind('<Button-1>',self.showrowcol)             # checked
        self.bind('<Control-plus>',self.inc_f_size)
        self.bind('<Control-minus>',self.dec_f_size)
        self.bind('<Control-m>',self.togglebold)            # want to change
        self.bind('<Control-T>',self.togglei)               # in change
        self.configure(undo = True,autoseparators = True ,maxundo = -1)     # checked
        self.tag_configure("sel", background = "yellow",foreground = "red") # checked
        scrollbar = Scrollbar(window, command = self.yview)     # done
        self.config(yscrollcommand = scrollbar.set)             # done
        scrollbar.pack(side = RIGHT , fill = Y)
    def inc_f_size(self,event = None):
	if self.cur_font_size >= 30:
		return False
        self.cur_font_size += 1
        f = Font(size = self.cur_font_size,family = self.cur_font_fam,slant = self.cur_font_slant,weight =self.cur_font_weight,underline = 0 if self.cur_font_under == "normal" else 1,overstrike= 0 if self.cur_font_overstrike == "normal" else 1)
        self.configure(font = f)
    def dec_f_size(self,event = None):
	if self.cur_font_size <= 6:
		return
        self.cur_font_size -= 1
        f = Font(size = self.cur_font_size,family = self.cur_font_fam,slant = self.cur_font_slant,weight =self.cur_font_weight,underline=0 if self.cur_font_under == "normal" else 1,overstrike= 0 if self.cur_font_overstrike=="normal"else 1)
        self.configure(font = f)
    def togglei(self,event =None):
        if self.cur_font_slant == "roman":
            self.cur_font_slant = "italic"
        else:
            self.cur_font_slant = "roman"
        f = Font(size = self.cur_font_size,family = self.cur_font_fam,slant = self.cur_font_slant,weight =self.cur_font_weight,underline=0 if self.cur_font_under == "normal" else 1,overstrike= 0 if self.cur_font_overstrike=="normal"else 1)
        self.configure(font = f)
    def togglebold(self,event =None):
        if self.cur_font_weight == "normal":
            self.cur_font_weight = "bold"
        else:
            self.cur_font_weight = "normal"
        f = Font(size = self.cur_font_size,family = self.cur_font_fam,slant = self.cur_font_slant,weight =self.cur_font_weight,underline=0 if self.cur_font_under == "normal" else 1,overstrike= 0 if self.cur_font_overstrike=="normal"else 1)
        self.configure(font = f)
    def showrowcol(self,event = None):
        pos = str(self.index(CURRENT)).split('.')
        line = pos[0]
        col = pos[1]
        status.config(text = 'Line '+line+'  Col '+col)
    def quit(self, event=None):
        window.quit()
        return
    def clearscreen(self, event = None):
        self.delete(0.0, END)
        return
    def selectall(self,event = None):
        # self.focus_set()
        self.tag_add('sel',"1.0",'end')
        self.focus_set()
        print self.index(CURRENT)
        return
    def newFile(self, event = None):
        global filename
        status.config(text="New File is Opened")
        if filename == "Untitled":
            satus.config(text = "New file is alreday Opened")
            showinfo("New File","New File is already Opened")
            self.showrowcol()
            return False
        filname = "Untitled"
        window.title("Untitled - Text Editor")
        self.delete(0.0, END)
        sleep(.300)
        status.config(text=" ")
        return True
    def saveAs(self,event = None):
        global filename
        status.config(text = "Save As")
        f = asksaveasfile(title = "Save As",initialdir=curdir,mode = 'w',defaultextension = '.txt',filetypes = types)
        t = self.get(0.0, END)
        try:
            if f == None:
                status.config(text = "File not Saved")
                showwarning("Save As","File not saved")
                self.showrowcol()
                return False
            filename = f.name
            f.write(t.rstrip())
            window.title(os.path.basename(filename)+"- Text Editor")
            f.close()
            status.config(text = filename + " saved")
            sleep(.300)
            self.showrowcol()
            return True
        except Exception as e:
            print e
            showerror(title = "Oops!",message = "Unable to save file")
            return False
    def rClicker(self,e = None):
        try:
            nclst=[
                   (' Cut','Ctrl + x', lambda e=e: self.cut(e)),
                   (' Copy ','Ctrl + c', lambda e=e: self.copy(e)),
                   (' Paste', 'Ctrl + v',lambda e=e: self.paste(e)),
                   ]
            rmenu = Menu(None, tearoff=0, takefocus= 0 )
            for (txt,acc, cmd) in nclst:
                rmenu.add_command(label=txt,accelerator = acc, command=cmd)
            rmenu.add_separator()
            nclst =[
                    (' Undo','Ctrl+z',lambda e=e: self.undo(e)),
                    (' Redo','Ctrl+y',lambda e=e:self.redo(e)),
                    (' Font','Ctrl+f',lambda e=e:self.change_font(e))
                ]
            for (txt, acc,cmd) in nclst:
                rmenu.add_command(label=txt,accelerator = acc, command=cmd)
            rmenu.tk_popup(e.x_root+90, e.y_root+20,entry="0")
        except TclError:
            print ' - rClick menu, something wrong'
            pass
        return "break"
    def saveFile(self,event =None):
        global filename
        status.config(text = "Saving File....")
        if filename == "Untitled" or filename == None:
            return self.saveAs()
        t = self.get(0.0, END)
        try:
            f = open(filename, 'w')
            window.title(os.path.basename(filename)+" -Text Editor")
            f.write(t)
            f.close()
            status.config(text="Saved")
            sleep(.500)
            self.showrowcol()
            return True
        except:
            return False
    def openFile(self,event = None):
        global filename
        status.config(text="Opening File..")
        f = askopenfile(initialdir=curdir,title = "Select File",mode = "r",defaultextension = '.txt',filetypes = types)
        if f == None:
            status.config(text = "No File Opened..")
            showwarning("Open File","No File Opened ")
            self.showrowcol()
            return False
        else:
            t = f.read()
            filename = f.name
            window.title(os.path.basename(f.name)+" -Text Eidtor")
            self.delete(0.0, END)
            self.insert(0.0,t)
            status.config(text=filename+" is Opened...")
            sleep(.500)
            self.showrowcol()
            return True
    def copy(self, event=None):
        try:
            if self.tag_ranges("sel"):
                self.clipboard_clear()
                text = self.get("sel.first", "sel.last")
                self.clipboard_append(text)
        except Exception as e:
            print e,"copy"
    def cut(self, event = None):
        try:
            if self.tag_ranges("sel"):
                self.copy()
                self.delete("sel.first", "sel.last")
        except Exception as e:
            print e,"cut"
    def paste(self, event = None):
        try:
            if self.tag_ranges("sel"):
                print True
                text = self.clipboard_get()
                index = self.index("sel.first")
                self.delete("sel.first","sel.last")
                self.insert(index,text)
                return
            self.event_generate('<<Paste>>')
        except Exception as e:
            print e,'paste'
    def undo(self,event = None):
        try:
            self.event_generate("<<Undo>>")
        except Exception as e:
            print e,"undo"
            pass
    def redo(self,event =None):
        try:
            self.event_generate("<<Redo>>")
        except Exception as e:
            print e,"redo"
            pass
    def copyall(self, event =None):
        try:
            self.clipboard_clear()
            text = self.get(0.0,END)
            self.clipboard_append(text)
        except Exception as e:
            print e,"copy all"
    def change_font(self,event = None):
        status.config(text = "Changing Font")
        font = askfont(window,title = "Select Font",family = self.cur_font_fam , size = self.cur_font_size,slant = self.cur_font_slant,weight = self.cur_font_weight,underline =0 if self.cur_font_under == "normal" else 1,overstrike = 0 if self.cur_font_overstrike == "normal" else 1 )
        if font:
            self.cur_font_fam = font["family"]
            font['family'] = font['family'].replace(' ', '\ ')
            self.cur_font_size = font["size"]
            self.cur_font_slant = font[ "slant"]
            self.cur_font_weight = font["weight"]
            print self.cur_font_overstrike
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font['underline']:
                self.cur_font_under = 'underline'
                font_str += ' underline'
            else:
                self.cur_font_under = 'normal'
            if font['overstrike']:
                self.cur_font_overstrike = 'overstrike'
                font_str += ' normal'
            else:
                self.cur_font_overstrike = 'overstrike'
            self.configure(font=font_str)
            status.config(text = "Font is changed to "+font_str)
            sleep(.300)
            self.showrowcol()

text = Test(window, width= 400,height = 400, exportselection = 1,tabs= 5)#export selecton to 0 makes the seperate clipboard 1 makes use of universal clipboard
# text.tag_configure("sel", background = "yellow",foreground = "red")
#text.configure()
text.newFile()
text.showrowcol()
text.pack()

Mainmenu = Menu(window)

fileMenu = Menu(Mainmenu, tearoff = 0)
fileMenu.add_command(label = "New    ",underline = 0, accelerator = "Ctrl + n", command = text.newFile)
fileMenu.add_command(label = "Open   ",underline = 0, accelerator = "Ctrl + o", command = text.openFile)
fileMenu.add_command(label = "Save   ",underline = 0, accelerator = "Ctrl + s",command = text.saveFile)
fileMenu.add_command(label = "Save As   ",underline = 5,accelerator = "Ctrl+Shift+s  ",command = text.saveAs)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit    ",underline = 0, accelerator = "Ctrl+Shift+q     ",command = text.quit)
Mainmenu.add_cascade(label="File", underline = 0,menu = fileMenu)

editMenu = Menu(Mainmenu, tearoff = 0)
editMenu.add_command(label="Copy All Text  ",underline = 0, accelerator = "Ctrl+Shift+c     ", command = text.copyall)
#editMenu.add_command(label="Cut",command = text.cutall)
editMenu.add_command(label="Paste   ",underline = 0, accelerator="Ctrl+v",command = text.paste)
editMenu.add_separator()
editMenu.add_command(label="Undo    ",accelerator = "Ctrl+z     ", command = text.undo)
editMenu.add_command(label="Redo    ",accelerator = "Ctrl+y     ",command = text.redo)
Mainmenu.add_cascade(label="Edit",underline = 0,menu = editMenu)

viewMenu = Menu(Mainmenu,tearoff = 0)
fontMenu = Menu(viewMenu,tearoff = 0)
fontMenu.add_command(label = "Select   ",underline =0,command = text.change_font)
viewMenu.add_cascade(label ="Font     ",underline = 0 ,accelerator = 'Ctrl + f', menu = fontMenu)
Mainmenu.add_cascade(label="View",underline = 0,menu = viewMenu)

helpMenu = Menu(Mainmenu, tearoff = 0)
helpMenu.add_command(label="About",underline =0, command = info)
Mainmenu.add_cascade(label="Help",underline =0,menu = helpMenu)
window.config(menu=Mainmenu ,relief = SUNKEN)
mainloop()
