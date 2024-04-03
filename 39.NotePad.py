from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox

root = Tk()
root.title("NotePad")
root.geometry("650x600+20+20")

def change():
    global status
    status.config(text="")

def new(e=None):
    global box,path,status,saved
    saved = False
    box.delete("1.0",END)
    box.unbind("<Button-1>")
    path = False
    status.config(text="")

def changed(e=None):
    global saved, box
    saved = False
    box.unbind("<Key>")
    box.unbind("<Button-1>")

def open_file(e=None):
    global box,path,status
    path = filedialog.askopenfilename(initialdir="D:\python programs",title="Open File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if path:
        box.delete("1.0",END)
        box.unbind("<Button-1>")
        box.config(foreground="black")
        file = open(path,'r')
        data = file.read()
        box.insert(END,data)
        file.close()
        status.config(text="Opened")
        status.after(1000,change)
        box.bind("<Key>",changed)

def save_as(e=None):
    global box,path,status,saved
    saved = True
    saved = filedialog.asksaveasfilename(initialdir="D:\python programs",title="Save File",filetypes=(("Text Files","*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All Files","*.*")))
    if saved:
        path = saved
        file = open(path,'w')
        data = box.get("1.0",END)
        file.write(data)
        file.close()
        status.config(text="Saved")
        status.after(1000,change)
        box.bind("<Key>",changed)

def save(e=None):
    global box,path,saved
    saved = True
    if path:
        file = open(path,'w')
        data = box.get("1.0",END)
        file.write(data)
        file.close()
        status.config(text="Saved")
        status.after(1000,change)
        box.bind("<Key>",changed)
    else:
        save_as("")

def cut(e):
    global box,ccv,status
    if e:
        ccv = root.clipboard_get()
    else:
        try:
            text = box.selection_get()
        except:
            text = ""
        if text:
            ccv = box.get("sel.first","sel.last")
            box.delete("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(ccv)
            status.config(text="Copied")
            status.after(1000,change)
        else:
            ccv = ""

def copy(e):
    global box,ccv,status
    if e:
        ccv = root.clipboard_get()
    else:
        try:
            text = box.selection_get()
        except:
            text = ""
        if text:
            ccv = box.get("sel.first","sel.last")
            root.clipboard_clear()
            root.clipboard_append(ccv)
            status.config(text="Copied")
            status.after(1000,change)
        else:
            ccv = ""

def paste(e):
    global box,ccv,status
    if not(e):
        index = box.index(INSERT)
        box.insert(index,ccv)
        status.config(text="Pasted")
        status.after(1000,change)

def print_():
    pass

def redo(e):
    global box,status
    try:
        if not(e):
            box.edit_redo()
            status.config(text="Redo")
            status.after(1000,change)
    except:
        pass

def undo(e):
    global box,status
    try:
        if not(e):
            box.edit_undo()
            status.config(text="Undo")
            status.after(1000,change)
    except:
        pass

def bold(e=None):
    global box,path,status
    bold_font = font.Font(box,box.cget("font"))
    bold_font.configure(weight="bold")
    box.tag_configure("bold",font=bold_font)
    try:
        text = box.selection_get()
    except:
        text = ""
    if text:
        tag = box.tag_names("sel.first")
        if "bold" in tag:
            box.tag_remove("bold","sel.first","sel.last")
            status.config(text="Bold")
            status.after(1000,change)
        else:
            box.tag_add("bold","sel.first","sel.last")
            status.config(text="UnBold")
            status.after(1000,change)

def italic(e=None):
    global box,path,status
    italic_font = font.Font(box,box.cget("font"))
    italic_font.configure(slant="italic")
    box.tag_configure("italic",font=italic_font)
    try:
        text = box.selection_get()
    except:
        text = ""
    if text:
        tag = box.tag_names("sel.first")
        if "italic" in tag:
            box.tag_remove("italic","sel.first","sel.last")
            status.config(text="Italics")
            status.after(1000,change)
        else:
            box.tag_add("italic","sel.first","sel.last")
            status.config(text="Not Italics")
            status.after(1000,change)

def underline_(e=None):
    global box,path,status
    italic_font = font.Font(box,box.cget("font"))
    italic_font.configure(underline=True)
    box.tag_configure("Underline",font=italic_font)
    try:
        text = box.selection_get()
    except:
        text = ""
    if text:
        tag = box.tag_names("sel.first")
        if "Underline" in tag:
            box.tag_remove("Underline","sel.first","sel.last")
            status.config(text="Underline")
            status.after(1000,change)
        else:
            box.tag_add("Underline","sel.first","sel.last")
            status.config(text="")

def color(e):
    global box, path
    colour = colorchooser.askcolor()
    colour = colour[1]
    if colour != NONE:    
        if e==2:
            box.config(bg=colour)
        else:
            box.tag_configure("colored",foreground=colour)
            if e == 1:
                box.tag_add("colored","1.0",END)
            else:
                text=""
                try:
                    text = box.selection_get()
                except:
                    text = ""
                if text:
                    box.tag_add("colored","sel.first","sel.last")
        status.config(text="Changed")
        status.after(1000,change)

def night_mode(e=None):
    global box,path,night,status
    bg_night = "#1e1e1e"
    bg_light = "white"
    fg_color = ""
    if night == False:
        box.config(bg="#4f4f4f",fg="#60cee1",selectforeground="#f90000",selectbackground="yellow",highlightcolor="#60cee1")
        box.tag_configure("night",foreground="#60cee1")
        box.tag_add("night","1.0",END)
        fg_color = "#4dc7f4"
        print_button.config(bg="#4f4f4f",fg=fg_color)
        paste_button.config(bg="#4f4f4f",fg=fg_color)
        cut_button.config(bg="#4f4f4f",fg=fg_color)
        copy_button.config(bg="#4f4f4f",fg=fg_color)
        undo_button.config(bg="#4f4f4f",fg=fg_color)
        redo_button.config(bg="#4f4f4f",fg=fg_color)
        status.config(bg="#4f4f4f",fg=fg_color,text="Night Mode")
        status.after(1000,change)
        night = True
        
    else:
        box.config(bg=bg_light,fg="black",selectbackground="light blue",selectforeground="green")
        box.tag_remove("night","1.0",END)
        bg_night = "SystemButtonFace"
        fg_color = "black"
        print_button.config(bg=bg_night,fg=fg_color)
        paste_button.config(bg=bg_night,fg=fg_color)
        cut_button.config(bg=bg_night,fg=fg_color)
        copy_button.config(bg=bg_night,fg=fg_color)
        undo_button.config(bg=bg_night,fg=fg_color)
        redo_button.config(bg=bg_night,fg=fg_color)
        status.config(bg="#dbdbdb",fg="black",text="Light Mode")
        status.after(1000,change)
        night = False
    frame.config(bg=bg_night)
    frame2.config(bg=bg_night)
    root.config(bg=bg_night)
    vscroll.config(bg=bg_night)
    hscroll.config(bg=bg_night)
    my_menu.config(bg=bg_night,fg=fg_color)
    file_menu.config(bg=bg_night,fg=fg_color)
    edit.config(bg=bg_night,fg=fg_color)
    view.config(bg=bg_night,fg=fg_color)

def activate():
    global entry2,entry1,replace_all,replace_one,rep
    entry2['state']= NORMAL
    replace_one['state']= NORMAL
    entry2.delete(0,END)
    replace_all['state']= NORMAL

def counter(e=None):
    global entry1,entry2
    entry1.config(fg="black")
    entry2.config(fg="black")
    entry1.delete(0,END)
    entry2.delete(0,END)
    #entry1.unbind("<FocusOn>")
    entry1.unbind("<Button-1>")
    #entry2.unbind("<FocusOn>")
    entry2.unbind("<Button-1>")

def search(e=None,s=-10):
    global entry1,box,path,label,inside1,inside2,number,nos,a,highlighted_first,highlighted,highlighted_last,all
    box.tag_remove("highlight1","1.0",END)
    box.tag_remove("highlight2","1.0",END)
    to_find = str(inside1.get())
    all = []
    if e != "":
        a = str(e)
    b = 1.0
    h = 0
    no = 1
    pos = a.find("'")
    temp = a.find("keycode")
    if a[temp+8:temp+10] != "8 " and e != "":
        to_find = to_find + str(a[pos+1])
    elif e != "":
        to_find = to_find[:-1]
    text = box.get("1.0",END)
    if to_find:
        count = text.count(to_find)
        if s != -10 and s != 0 and s!=count+1:
            nos = s
        if count != 0:
            label.config(text=str(nos)+" of "+str(count))
        else:
            label.config(text="0 of 0")
        number = 0
        for i in text:
            c = len(to_find)
            if i == to_find[0]:
                d = text.find(i,number)
                g = text[d:d+c]
                number = d+1
                if g == to_find:
                    f = str(b).find(".")
                    first = (str(b)[:f+1])+str(h)
                    last = (str(b)[:f+1])+str(h+c)
                    if no == nos:
                        box.tag_add("highlight2",first,last)
                        highlighted = to_find
                        highlighted_first = first
                        highlighted_last = last
                    else:
                        box.tag_add("highlight1",first,last)
                    t = [to_find,first,last]
                    all.append(t)    
                    no = no + 1
            h = h+1
            if i == "\n":
                b = b + 1
                h = 0

def RO():
    global entry2,inside2, highlighted_last, highlighted,highlighted_first,box,nos
    to_replace = str(inside2.get())
    box.delete(highlighted_first,highlighted_last)
    box.insert(highlighted_first,to_replace)
    #box.tag_remove("highlight2",highlighted_first,highlighted_last)
    search("",1)

def close():
    global entry1, entry2,replace_all,nos,a,all
    entry1.delete(0,END)
    entry2['state'] = NORMAL
    entry2.delete(0,END)
    all = []
    nos = 1
    a = ""
    box.tag_remove("highlight1","1.0",END)
    box.tag_remove("highlight2","1.0",END)
    level.destroy()

def RA():
    global entry2, inside2, highlighted_last,highlighted_first,highlighted,box,nos,all
    to_replace = str(inside2.get())
    for i in all:
        box.delete(i[1],i[2])
        box.insert(i[1],to_replace)
    search("",1)

def erase(e=None):
    global box
    box.delete("1.0",END)
    box.config(foreground="black")

def find(e=None):
    global box,path,rep,side,entry2,entry1,up,down,replace_all,replace_one,label,inside1,inside2,level
    level = Toplevel(root)
    level.title("Find the Word")
    side = Button(level,text=">",command=activate)
    entry1 = Entry(level,fg="grey",textvariable=inside1)
    label = Label(level,text="     ")
    up = Button(level,text="\\/",command=lambda:search("", nos+1 ))
    down = Button(level,text="/\\",command = lambda:search("",nos-1))
    entry2 = Entry(level,fg="grey",textvariable=inside2)
    replace_one = Button(level,text="RO",command=RO)
    replace_all = Button(level,text="RA",command=RA)
    entry1.insert(0,"Find...")
    entry2.insert(0,"Replace...")
    entry1.bind("<Key>",search)
    entry1.bind("<Button-1>",counter)
    entry2.bind("<Button-1>",counter)

    side.grid(row=0,column=0,padx=5,pady=5)
    entry1.grid(row=0,column=1,padx=5,pady=5)
    label.grid(row=0,column=2,padx=5,pady=5)
    up.grid(row=0,column=3,padx=5,pady=5)
    down.grid(row=0,column=4,padx=5,pady=5)
    entry2.grid(row=1,column=1,padx=5,pady=5)
    replace_one.grid(row=1,column=2,padx=5,pady=5)
    replace_all.grid(row=1,column=3,padx=5,pady=5)
    label.config(text="0 of 0")
    level.protocol("WM_DELETE_WINDOW",close)
    if rep == False:
        entry2['state'] = DISABLED
        replace_one['state'] = DISABLED
        replace_all['state'] = DISABLED

def replace(e=None):
    global rep
    rep = True
    find()

def main_close():
    global saved
    if saved:
        root.quit()
    else:
        file = messagebox.askyesnocancel("Save File","Do you want to save this file?")
        if file == True:
            save()
            root.quit()
        elif file == False:
            root.quit()

def nothing(e=None):
    global box
    a = box.index(INSERT)
    print(a)
    #x = a.index(".")
    #e = int(a[x+1:])
    #e = float("0." + str(e + 1))
    #e = str(float(box.index(INSERT))+e)
    #box.mark_set("insert",e)

frame = Frame(root,width=30)
frame.pack(side=LEFT,pady=5)

frame2 = Frame(root)
frame2.pack(side=TOP,pady=5)

vscroll = Scrollbar(frame,orient=VERTICAL)
vscroll.pack(fill=Y,side=RIGHT,pady=5)

hscroll = Scrollbar(frame,orient=HORIZONTAL)
hscroll.pack(fill=X,side=BOTTOM,pady=5)

box = Text(frame,height=40,width=60,undo=True,font=("Times New Roman",14),yscrollcommand=vscroll.set,xscrollcommand=hscroll.set,selectbackground="light blue",selectforeground="green",wrap="none")
box.config(foreground="grey")
box.insert(END,"Notepad...")
box.pack(pady=10,padx=15)

vscroll.config(command=box.yview)
hscroll.config(command=box.xview)

path = False
saved = True
inside1 = StringVar()
inside2 = StringVar()
level = Toplevel()
level.destroy()
all = []
highlighted_last = ""
highlighted_first = ""
highlighted = ""
ccv = ""
night = False
rep = False
nos = 1
a = ""
number = 0
box.tag_config("highlight1",background="black",foreground="white")
box.tag_config("highlight2",background="yellow",foreground="blue")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New File",command=lambda:new(""),accelerator="      (Ctrl+N)")
file_menu.add_command(label="Open File",command=lambda:open_file(""),accelerator="      (Ctrl+O)")
file_menu.add_command(label="Save",command = lambda:save(""),accelerator="      (Ctrl+S)")
file_menu.add_command(label="Save As",command=lambda:save_as(""),accelerator="      (Ctrl+Shift+S)")
file_menu.add_command(label="Print",accelerator="      (Ctrl+P)")
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit,accelerator="      (Alt+F4)")

edit = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit)
edit.add_command(label="Undo",accelerator="      (Ctrl+Z)",command=lambda:undo(""))
edit.add_command(label="Redo",accelerator="      (Ctrl+Y)",command=lambda:redo(""))
edit.add_separator()
edit.add_command(label="Cut",accelerator="      (Ctrl+X)",command=lambda:cut(""))
edit.add_command(label="Copy",accelerator="      (Ctrl+C)",command=lambda:copy(""))
edit.add_command(label="Paste",accelerator="      (Ctrl+V)",command=lambda:paste(""))
edit.add_separator()
edit.add_command(label="Bold",accelerator="      (Ctrl+B)",command=bold)
edit.add_command(label="Italic",accelerator="      (Ctrl+Shift+I)",command=italic)
edit.add_command(label="Underline",accelerator="      (Ctrl+U)",command=underline_)
edit.add_separator()
edit.add_command(label="Find",accelerator="      (Ctrl+F)",command=find)
edit.add_command(label="Replace",accelerator="      (Ctrl+R)",command=replace)

view = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="View",menu=view)
view.add_checkbutton(label="Night Mode",accelerator="      (Ctrl+M)",command=night_mode)
view.add_separator()
view.add_command(label="Selected Font Color",command=lambda:color(0))
view.add_command(label="All Font Color",command=lambda:color(1))
view.add_command(label="Background Color",command=lambda:color(2))

print_button = Button(frame2,text="Print",command=print_)
cut_button = Button(frame2,text="Cut",command=lambda:cut(""))
copy_button = Button(frame2,text="Copy",command=lambda:copy(""))
paste_button = Button(frame2,text="Paste",command=lambda:paste(""))
undo_button = Button(frame2,text="Undo",command=lambda:undo(""))
redo_button = Button(frame2,text="Redo",command=lambda:redo(""))
ind = Button(frame2,text="ind",command=nothing)

print_button.grid(row=0,column=1,pady=5,padx=5)
cut_button.grid(row=1,column=1,pady=5,padx=5)
copy_button.grid(row=2,column=1,pady=5,padx=5)
paste_button.grid(row=3,column=1,pady=5,padx=5)
undo_button.grid(row=4,column=1,pady=5,padx=5)
redo_button.grid(row=5,column=1,pady=5,padx=5)
ind.grid(row=6,column=1,pady=5,padx=5)

side = Button()
entry1 = Entry()
up = Button()
down = Button()
entry2 = Entry()
replace_one = Button()
label = Label()
replace_all = Button()

root.bind("<Control-c>",copy)
box.bind("<Key>",changed)
entry1.bind("<Key>",search)
root.bind("<Control-v>",paste)
root.bind("<Control-x>",cut)
root.bind("<Control-z>",undo)
root.bind("<Control-y>",redo)
root.bind("<Control-n>",new)
root.bind("<Control-o>",open_file)
root.bind("<Control-s>",save)
root.bind("<Control-b>",bold)
root.bind("<Control-Shift-I>",italic)
root.bind("<Control-u>",underline_)
root.bind("<Control-m>",night_mode)
root.bind("<Control-f>",find)
root.bind("<Control-r>",replace)
root.bind("<Control-Shift-Key-S>",save_as)
box.bind("<Button-1>",erase)

status = Label(root,text="",relief=SUNKEN,bg="#dbdbdb")
status.pack(side=BOTTOM,fill=X,ipady=5)

root.protocol("WM_DELETE_WINDOW",main_close)

root.mainloop()