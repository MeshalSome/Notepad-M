#Code by: Meshal
#To do:
#Custom Fonts
#Custom Select colour
#Custom fonts sizes
#Custom font colour
#Make it a .exe file (last thing)

from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox

root = Tk()
root.title("Notepad-M")
root.geometry("824x467")
my_frame = Frame(root)
my_frame.pack(pady=5)

global open_status_name
open_status_name = False

global selected
selected = False

def saved_message():
    response = messagebox.showinfo("File saved", "Saved")

def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Notepad-M")
    status_bar.config(text="New File   ")
    global open_status_name
    open_status_name = False

def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="Desktop", title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))

    if text_file:
        global open_status_name
        open_status_name = text_file
        
    name = text_file
    status_bar.config(text=f'{name}        ')
    name = name.replace("Desktop", "")
    root.title(f'{name} - Notepad-M')
    text_file = open(text_file, 'r')
    stuff = text_file.read()
    my_text.insert(END, stuff)
    text_file.close()
    
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", initialdir="Desktop", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("All Files", "*.*")))
    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        name = name.replace("Desktop", text_file)
        root.title(f'{name} - Notepad-M')
        text_file = open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        
        status_bar.config(text=f'Saved: {open_status_name}        ')
        saved_message()
    else:
        save_as_file()
        saved_message()

def cut_text(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()
        my_text.delete("sel.first", "sel.last")

def copy_text(e):
    global selected
    if my_text.selection_get():
        selected = my_text.selection_get()

def paste_text(e):
    if selected:
        position = my_text.index(INSERT)
        my_text.insert(position, selected)

def bold_text():
    bold_font = font.Font(my_text, my_text.cget("font"))
    bold_font.configure(weight="bold")
    my_text.tag_configure("bold", font=bold_font)
    current_tags = my_text.tag_names("sel.first")
    if "bold" in current_tags:
        my_text.tag_remove("bold", "sel.first", "sel.last")
    else:
        my_text.tag_add("bold", "sel.first", "sel.last")

def italics_text():
    italics_font = font.Font(my_text, my_text.cget("font"))
    italics_font.configure(slant="italic")
    my_text.tag_configure("italic", font=italics_font)
    current_tags = my_text.tag_names("sel.first")
    if "italic" in current_tags:
        my_text.tag_remove("italic", "sel.first", "sel.last")
    else:
        my_text.tag_add("italic", "sel.first", "sel.last")

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

x_scroll = Scrollbar(my_frame, orient='horizontal')
x_scroll.pack(side=BOTTOM, fill=X)

my_text = Text(my_frame, width=97, height=26, font=("Helvetica", 11), selectforeground="black", undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=x_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)
x_scroll.config(command=my_text.xview)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: cut_text(1), accelerator="Ctrl+x")
edit_menu.add_command(label="Copy", command=lambda: copy_text(1), accelerator="Ctrl+c")
edit_menu.add_command(label="Paste", command=lambda: paste_text(1), accelerator="Ctrl+v")
edit_menu.add_command(label="Undo", command=my_text.edit_undo, accelerator="Ctrl+z")
edit_menu.add_command(label="Redo", command=my_text.edit_redo, accelerator="Ctrl+y")

text_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Text", menu=text_menu)
text_menu.add_command(label="Bold", command=bold_text)
text_menu.add_command(label="Italics", command=italics_text)

status_bar = Label(root, text="Ready          ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

root.mainloop()
