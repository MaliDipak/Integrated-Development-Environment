# An integrated development environment (IDE) GUI application using Python Tkinter
import os
import subprocess
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import askquestion, showinfo, showwarning
from tkinter.filedialog import askopenfilename, asksaveasfilename


def helpfun():
    showinfo(title='IDE', message='IDE : By Dipak Mali')


def runcpp():
    name = os.path.basename(fp).split('.')
    if name[1] != 'cpp':
        showwarning(title='IDE', message='Select the proper Language')
        return
    try:
        a = subprocess.run([f'{v.get()}', fp], stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e)
        showwarning(title='IDE', message='Select the proper Language')
        return

    try:
        b = subprocess.run('a.exe', stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e2:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e2)
        return

    try:
        os.remove(f'{name[0]}.exe')
    except:
        pass

    try:
        os.rename('a.exe', f'{name[0]}.exe')
    except:
        pass

    output_window.delete(1.0, END)
    output_window.insert(1.0, b.stdout.decode())


def runc():
    name = os.path.basename(fp).split('.')
    if name[1] != 'c':
        showwarning(title='IDE', message='Select the proper Language')
        return
    try:
        a = subprocess.run([f'{v.get()}', fp], stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e)
        showwarning(title='IDE', message='Select the proper Language')
        return

    try:
        b = subprocess.run('a.exe', stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e2:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e2)
        return

    try:
        os.remove(f'{name[0]}.exe')
    except:
        pass

    try:
        os.rename('a.exe', f'{name[0]}.exe')
    except:
        pass

    output_window.delete(1.0, END)
    output_window.insert(1.0, b.stdout.decode())


def runjava():
    name = os.path.basename(fp).split('.')
    if name[1] != 'java':
        showwarning(title='IDE', message='Select the proper Language')
        return
    try:
        a = subprocess.run([f'{v.get()}', fp], stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e)
        showwarning(title='IDE', message='Select the proper Language')
        return

    try:
        b = subprocess.run(f'java {name[0]}', stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e2:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e2)
        return

    output_window.delete(1.0, END)
    output_window.insert(1.0, b.stdout.decode())


def runpython():
    name = os.path.basename(fp).split('.')
    if name[1] != 'py':
        showwarning(title='IDE', message='Select the proper Language')
        return

    try:
        a = subprocess.run([f'{v.get()}', fp], stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    except Exception as e:
        output_window.delete(1.0, END)
        output_window.insert(1.0, e)
        showwarning(title='IDE', message='Select the proper Language')
        return

    output_window.delete(1.0, END)
    output_window.insert(1.0, a.stdout.decode())


def runfun():

    global fp

    if fp == None:

        ch = askquestion('IDE', 'Do you want to save changes to Untitled?')

        if ch == 'no':
            return

    savefun()

    l = v.get()

    if l == 'None':
        showinfo(title='IDE', message='Select The Language')
    elif l == 'python':
        runpython()
    elif l == 'gcc':
        runc()
    elif l == 'g++':
        runcpp()
    elif l == 'javac':
        runjava()


def newfun():
    global fp
    root.title("Untitled - IDE")
    fp = None
    textArea.delete(1.0, END)


def openfun():
    global fp
    fp = askopenfilename(defaultextension=".txt", filetype=[
                         ("All Files", "*.*"), ("Text Document", "*.txt")])
    if fp == "":
        fp = None
    else:
        root.title(os.path.basename(fp) + " - IDE")
        textArea.delete(1.0, END)
        n = open(fp, 'r')
        textArea.insert(1.0, n.read())
        n.close()


def savefun():
    global fp
    if fp == None:
        fp = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetype=[
            ("All Files", "*.*"), ("Text Document", "*.txt")])

        if fp == "":
            fp = None
        else:
            # Save as new file
            n = open(fp, "w")
            n.write(textArea.get(1.0, END))
            n.close()
            root.title(os.path.basename(fp) + " - IDE")
    else:
        # Save file
        n = open(fp, "w")
        n.write(textArea.get(1.0, END))
        n.close()


def cutfun():
    textArea.event_generate(("<<Cut>>"))


def copyfun():
    textArea.event_generate(("<<Copy>>"))


def pastefun():
    textArea.event_generate(("<<Paste>>"))


def light():
    textArea.config(bg="white", fg='black')
    output_window.config(bg="white", fg='red')


def dark():
    textArea.config(fg="white", bg="grey")
    output_window.config(fg="white", bg="grey")


if __name__ == '__main__':

    root = Tk()

    fp = None

    root.title("IDE : By Dipak Mali")
    root.iconbitmap('icon.ico')
    root.geometry("500x700")

    # Text Area
    textArea = ScrolledText(root, font=(
        "haveltica 10 bold"), padx=10, pady=10, height=25)
    textArea.pack(fill=BOTH, pady=10, padx=10)

    # Menu Bar
    menuBar = Menu(root)

    file = Menu(menuBar, tearoff=0)
    file.add_command(label="New", command=newfun)
    file.add_command(label="Open", command=openfun)
    file.add_command(label="Save", command=savefun)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)
    menuBar.add_cascade(label='File', menu=file)

    edit = Menu(menuBar, tearoff=0)
    edit.add_command(label="Cut", command=cutfun)
    edit.add_command(label="Copy", command=copyfun)
    edit.add_command(label="Paste", command=pastefun)
    menuBar.add_cascade(label='Edit', menu=edit)

    run = Menu(menuBar, tearoff=0)
    run.add_command(label='Run', command=runfun)
    menuBar.add_cascade(label='Run', menu=run)

    h = Menu(menuBar, tearoff=0)
    h.add_command(label='View Help', command=helpfun)
    menuBar.add_cascade(label='Help', menu=h)

    theme = Menu(menuBar, tearoff=0)
    theme.add_command(label='Dark', command=dark)
    theme.add_command(label='Light', command=light)
    menuBar.add_cascade(label='Theme', menu=theme)

# Language
    v = StringVar()
    v.set('None')
    language = Menu(menuBar, tearoff=0)
    language.add_radiobutton(label='python', variable=v, value='python')
    language.add_radiobutton(label='C', variable=v, value='gcc')
    language.add_radiobutton(label='C++', variable=v, value='g++')
    language.add_radiobutton(label='Java', variable=v, value='javac')
    menuBar.add_cascade(label='Language', menu=language)

    root.config(menu=menuBar)
    # create output window to display output of written code
    output_window = ScrolledText(
        root, height=10, padx=10, pady=10)
    output_window.pack(fill=BOTH, expand=1, padx=10, pady=10)

    root.mainloop()
