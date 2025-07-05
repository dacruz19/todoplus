import customtkinter as ctk
from PIL import Image

off = ctk.CTkImage(Image.open("off.png"))
on = ctk.CTkImage(Image.open("on.png"))

class main(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300") 
        self.minsize(300, 300)
        self.maxsize(350,350)

        self.title("To-Do++")
        self.topmost = False

        frame = ctk.CTkFrame(master=self,height=10)
        frame.pack(fill=ctk.X,side=ctk.TOP)

        title = ctk.CTkLabel(master=self, text="To-Do ++",height=50,width=30, text_color="white",font=("Arial",23, "bold"))
        title.pack(pady=2,side=ctk.TOP)

        pin_button = ctk.CTkButton(master=frame,command=lambda: self.pin(pin_button),height=20,width=1,image=off,text="")
        pin_button.pack(pady=2,side=ctk.RIGHT)

        create_button = ctk.CTkButton(master=frame,height=15,width=20,text="+",font=("Arial",23, "bold"), command= lambda: self.make_task(task_list))
        create_button.pack(pady=2,side=ctk.LEFT)

        task_list = ctk.CTkScrollableFrame(self,height=120)
        task_list.pack(pady=1,fill=ctk.BOTH,expand=True)

    def pin(self,button):
        if self.topmost == False:
            self.attributes("-topmost", True)
            button.configure(image=on)
            self.topmost = True
        elif self.topmost:
            self.attributes("-topmost", False)
            button.configure(image=off)
            self.topmost = False

    def make_task(self,frame):
        new_task = ctk.CTkFrame(frame)
        new_task.pack(pady=2,side=ctk.TOP,anchor="w",fill=ctk.X)

        checkmark = ctk.CTkCheckBox(new_task,command=lambda:self.complete_task(entry),text="",width=10)
        checkmark.pack(padx=2,side=ctk.LEFT)

        entry = ctk.CTkEntry(new_task,font=("Arial",18))
        entry.pack(padx=5,side=ctk.LEFT,fill=ctk.X,expand=True)

        delete = ctk.CTkButton(new_task,command=lambda:self.delete_task(new_task),text="X",width=10,font=("Arial",23, "bold"))
        delete.pack(padx=2,side=ctk.RIGHT)

    def complete_task(self,entry):
        current = entry.cget("font")

        if "overstrike" in current:
            entry.configure(font=("Arial",20))
        else:
            entry.configure(font=("Arial",20,"overstrike"))

    def delete_task(self,task):
        task.destroy()

app = main()
app.mainloop()
