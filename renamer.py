# Here we go at our first major project
# That failed miserable in C++
# To batch rename our files based on set parameters
import os
from Tkinter import *
import tkFileDialog



class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(side=LEFT)
        self.tex = Text(master)
        self.tex.pack(side=RIGHT)

        self.dirname="blank"

        self.button = Button(frame, text="Browse", command=lambda: self.askdirectory())
        self.button.pack(side=TOP)
        self.button = Button(frame, text="Run", fg="black", command=lambda: self.renamer(self.dirname))
        self.button.pack(side=LEFT)

    def askdirectory(self):
        self.dirname = tkFileDialog.askdirectory()

    def directory(self):
        print self.dirname

    def renamer(self, target):
        os.chdir(target)

        for filename in os.listdir('.'):
            self.tex.insert(END, filename)
            self.tex.see(END)
            filepair = filename.split(".")
            if filepair[-1] in ["avi", "mkv", "mpeg", "mov", "mp4", "mpg", "wmv", "rmvb", "ogg", "ogm", "rm", "vob",
                                "amv",
                                "divx"]:
                extname = filepair.pop()
                if len(filepair) > 1:
                    stringfile = "_".join(filepair)
                else:
                    stringfile = filepair[0]
                fixedstring = self.stringfixer(stringfile)
                completestring = fixedstring + "." + extname
                # print completestring
                self.tex.insert(END, " : " + completestring + "\n")
                self.tex.see(END)
                if filename != completestring:
                    records = open('records.txt', 'a')
                    records.write(filename + ' : ' + completestring + '\n')
                    records.close()
                os.rename(filename, completestring)
            else:
                # print "not the file you want"
                self.tex.insert(END, " : not the file you want\n")

    def stringfixer(self, string):
        m = re.sub(r'\[([^]]+)\]', "", string)
        m = re.sub(r'\(([^\)]+)\)', "", string)
        if m:
            string = m
        string = string.replace('_', ' ')
        string = string.replace('  ', ' ')
        string = string.replace('  ', ' ')
        string = string.replace('_', ' ')
        string = string.strip()
        string = string.replace(' ', '_')
        string = string.title()
        h = re.split(r'(?<=\w)_(?=\d\d)', string)
        if len(h) > 1:
            string = '_-_'.join(h)
        return string


root = Tk()
root.iconbitmap(default='transparent.ico')
root.wm_title("Renamer v1.0")
app = App(root)

root.mainloop()
