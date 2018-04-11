from tkinter import *

class Project(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.minsize(width=500, height = 500)

        container = Frame(self)
        container.grid(row = 0, column = 0, sticky = NSEW)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,InfoPage,PrefPage,ResultPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = NSEW)

        self.show_frame(StartPage)

    def show_frame(self, project):
        frame = self.frames[project]
        frame.tkraise()

class StartPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)
        greeting = Label(self,text="Welcome to the UMD Study Abroad Destination Selection GUI",
                         font = ("Times New Roman", 12))
        greeting.pack(side=TOP)

        button_1 = Button(self, text = "Continue", command = lambda: project.show_frame(InfoPage))
        button_1.pack(side=BOTTOM)

class InfoPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        self.grid_rowconfigure(6,weight=1)
        self.grid_columnconfigure(3, weight=1)

        intro = Label(self,text="Please tell us something about you",font = ("Times New Roman", 12))
        intro.grid(row = 0, columnspan = 3,padx = 5, pady = 5)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(StartPage))
        button_1.grid(row = 5, column = 0, padx = 5, pady = 5)

        button_2 = Button(self, text="Continue", command=lambda: project.show_frame(PrefPage))
        button_2.grid(row = 5, column = 2, padx = 5, pady = 5)

        lab_1 = Label(self,text = "Full Name")
        lab_1.grid(row = 1, column = 0, padx = 5, pady = 5)
        en_lab_1 = Entry(self)
        en_lab_1.grid(row = 1, column = 1, columnspan = 2, padx = 5, pady = 5)

        lab_2 = Label(self, text = "Academic Year")
        lab_2.grid(row = 2, column = 0, padx = 5, pady = 5)
        lab_2_option = ["Freshman", "Sophomore", "Junior", "Senior"]
        lab_2_var = StringVar(self); lab_2_var.set("Select...")
        en_lab_2 = OptionMenu(self,lab_2_var,*lab_2_option)
        en_lab_2.grid(row = 2, column = 1, columnspan = 2, padx = 5, pady = 5)

        lab_3 = Label(self,text = "Major(s)")
        lab_3.grid(row = 3, column = 0, padx = 5, pady = 5)
        en_lab_3 = Entry(self)
        en_lab_3.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)

        lab_4 = Label(self,text = "GPA")
        lab_4.grid(row = 4, column = 0, padx = 5, pady = 5)
        en_lab_4 = Entry(self)
        en_lab_4.grid(row = 4, column = 1, columnspan = 2, padx = 5, pady = 5)

class PrefPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Please tell us your preference about the following",font = ("Times New Roman", 12))
        intro.grid(row = 0, columnspan = 7, padx = 5, pady = 5)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(InfoPage))
        button_1.grid(row = 8, column = 0, padx = 5, pady = 5)

        button_2 = Button(self, text="Continue", command=lambda: project.show_frame(ResultPage))
        button_2.grid(row = 8, column = 6, padx = 5, pady = 5)

        lab_1 = Label(self, text="Purpose")
        lab_1.grid(row=1, column=0, padx=5, pady=5)
        en_lab_1_ch_1 = Checkbutton(self, text = "Academic")
        en_lab_1_ch_1.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
        en_lab_1_ch_2 = Checkbutton(self, text= "Internship")
        en_lab_1_ch_2.grid(row=1, column=4, columnspan=3, padx=5, pady=5)

        lab_2 = Label(self, text="Region")
        lab_2.grid(row=2, column=0, padx=5, pady=5)
        lab_2_option = ["Africa - Central", "Africa - East", "Africa - North", "Africa - South", "Africa - West",
                        "America - Central", "America - North", "America - South", "Asia - Central", "Asia - East",
                        "Asia - South", "Asia - SouthEast","Asia - West", "Caribbean", "Europe - East",
                        "Europe - North", "Europe - South", "Europe - West", "Middle East","Oceania"]
        lab_2_var = StringVar(self)
        lab_2_var.set("Select...")
        en_lab_2 = OptionMenu(self, lab_2_var, *lab_2_option)
        en_lab_2.grid(row=2, column=1, columnspan=5, padx=5, pady=5)

        lab_3 = Label(self, text="Second Languages")
        lab_3.grid(row=3, column=0, padx=5, pady=5)
        lab_3_option = ["None","Arabic", "French", "German", "Hindi", "Italian", "Japanese", "Korean", "Mandarin",
                        "Portuguese", "Russian", "Spanish", "Vietnamese"]
        lab_3_var = StringVar(self);
        lab_3_var.set("Select...")
        en_lab_3 = OptionMenu(self, lab_3_var, *lab_3_option);
        en_lab_3.grid(row=3, column=1, columnspan=5, padx=5, pady=5)

        lab_4 = Label(self, text="Cost range")
        lab_4.grid(row=4, column=0, padx=5, pady=5)
        en_lab_4_1 = Entry(self)
        en_lab_4_1.grid(row=4, column=1, columnspan=2, padx=5, pady=5)
        to = Label(self, text="to")
        to.grid(row=4, column=3, columnspan = 2, padx=5, pady=5)
        en_lab_4_2= Entry(self)
        en_lab_4_2.grid(row=4, column=5, columnspan=2, padx=5, pady=5)

        lab_5 = Label(self, text="Accomodation")
        lab_5.grid(row=5, column=0, padx=5, pady=5)
        lab_5_option = ["Apartment", "Campus", "Host"]
        lab_5_var = StringVar(self);
        lab_5_var.set("Select...")
        en_lab_5 = OptionMenu(self, lab_5_var, *lab_5_option);
        en_lab_5.grid(row=5, column=1, columnspan=5, padx=5, pady=5)

        lab_6 = Label(self, text="Trips")
        lab_6.grid(row=6, column=0, padx=5, pady=5)
        en_lab_6_ch_1 = Checkbutton(self, text="City Exploring")
        en_lab_6_ch_1.grid(row=6, column=1, columnspan=2, padx=5, pady=5)
        en_lab_6_ch_2 = Checkbutton(self, text="Sightseeing")
        en_lab_6_ch_2.grid(row=6, column=3, columnspan=2, padx=5, pady=5)
        en_lab_6_ch_3 = Checkbutton(self, text="Nightlife")
        en_lab_6_ch_3.grid(row=6, column=5, columnspan=2, padx=5, pady=5)

        lab_7 = Label(self, text="Program Season")
        lab_7.grid(row=7, column=0, padx=5, pady=5)
        lab_7_option = ["Spring", "Summer", "Fall", "Winter"]
        lab_7_var = StringVar(self);
        lab_7_var.set("Select...")
        en_lab_7 = OptionMenu(self, lab_7_var, *lab_7_option);
        en_lab_7.grid(row=7, column=1, columnspan=5, padx=5, pady=5)

class ResultPage(Frame):
    def __init__(self,parent,project):
        Frame.__init__(self,parent)

        intro = Label(self,text="Here are our suggestions",font = ("Times New Roman", 12))
        intro.pack(side=TOP)

        button_1 = Button(self, text="Back", command=lambda: project.show_frame(PrefPage))
        button_1.pack(side=BOTTOM)

app = Project()
app.mainloop()



