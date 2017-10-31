from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showerror
import os
from lxml import etree
import lxml
import cmd


class MyFrame(tk.Frame):

    def __init__(self, master=None):

        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.folder = "Hello"
        self.master.title("Validate Boomi Files")
       # self.master.rowconfigure(5, weight=20)
       # %self.master.columnconfigure(5, weight=5)
        self.master.minsize(width=800, height=400)
        self.master.maxsize(width=800, height=400)
        self.grid(sticky=W )


        self.button = tk.Button(self, text="Boomi Outbound Folder", command=self.load_file, width=25)
        self.button.grid(row=0, column=0, sticky=W)
        self.button2 = tk.Button(self, text="Validate the Files", command=self.validate, width=25)
        self.button2.grid(row=0, column=1, sticky=W)
        self.text = tk.Text(self,  height=30, width=78)
        self.text.grid(row=1, column=0,columnspan=2, sticky=W)





    def load_file(self):

        self.folder = askdirectory(initialdir='C:\\')
        try:
            print(self.folder)
        except:  # <- naked except is a bad idea
            showerror("Open Source File", "Failed to read file\n'%s'" % fname)
        return



    def validate(self):
        theFiles = []
        def validate_xml(xml_path: str, xsd_path: str) -> bool:

            xmlschema_doc = etree.parse(xsd_path)
            xmlschema = etree.XMLSchema(xmlschema_doc)
            xml_doc = etree.parse(xml_path)
            result = xmlschema.validate(xml_doc)
            return result

        cwd = os.getcwd()
        _schema = cwd + '\\Colleague_PeopleData.xsd'

        ## loop in the folder and validate the files one by one
        _schema = _schema.replace("\\", "\\\\")

        for path, subdirs, files in os.walk(self.folder):
            for name in files:
                ##name = os.path.join(path, name)
                name = path + "/" + name
                name = name.replace("/", "\\")
                if validate_xml(name, _schema ):
                   ## print('Valid! File')
                    pass
                else:
                    theFiles.append(name)

        if (len(theFiles) >= 1):
            pass
            self.text.configure(state='normal')
            self.text.insert('end', '\n')
            self.text.insert('end', '>>>>>>>>>>>>>>>     ERRORS DURING MESSAGE VALIDATION!     <<<<<<<<<<<<<<<<<<')
            self.text.insert('end', '\n' )
            self.text.insert('end', '>>>>>>>>>>>>>>>        REVIEW THE ' + str(len(theFiles)) +   ' FILE/S BELOW       <<<<<<<<<<<<<<<<<<' '\n' '\n')
            for n in theFiles:
                self.text.insert('end', n)
                self.text.insert('end', '\n' '\n')
            self.text.configure(state='disabled')
        else:
            pass
            self.text.insert('end', '\n')
            self.text.insert('end', '>>>>>>>>>>>>>>>     ALL THE FILES WHERE VALIDATED!!     <<<<<<<<<<<<<<<<<<')
            self.text.insert('end', '\n' )



if __name__ == "__main__":
    print("Starting Analysis")
    root = tk.Tk()
    app = MyFrame(master=root)
    app.mainloop()

