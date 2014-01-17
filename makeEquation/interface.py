import tkinter as tk

class GUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create()
        
    def create(self):
        w = tk.Canvas(self,width=600,height=400)
        # w.create_image = (image=vp)
        w.pack()
        
run = GUI()
run.mainloop()
