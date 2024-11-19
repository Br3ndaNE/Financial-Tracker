import customtkinter as ctk
from tkinter import ttk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Financial-App")
        self.geometry("1080x720")  # Set a window size
        ctk.set_appearance_mode("dark")

        # Categories for the ComboBox
        category = [
            "Boodschappen",
            "Vervoer",
            "Gezondheid",
            "Entertainment",
            "Kleding",
            "Abonnementen",
            "Sparen",
            "Beleggen"
        ]

        input_frame = ctk.CTkFrame(self, width=800, height=50)
        input_frame.grid_propagate(False)
        input_frame.pack(pady=30)

        # ComboBox for Categories
        self.categoryComboBox = ctk.CTkComboBox(
            input_frame,
            state="readonly",
            values=category
        )
        self.categoryComboBox.set(category[0])  # Set default value
        self.categoryComboBox.grid(row=0, column=0, padx=10, pady=10)

        # Entry for Cost
        self.costBox = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter cost"
        )
        self.costBox.grid(row=0, column=1, padx=10)

        # Entry for Item
        self.itemBox = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter item"
        )
        self.itemBox.grid(row=0, column=2, padx=10)

        # Entry for Notation
        self.notationBox = ctk.CTkEntry(
            input_frame,
            placeholder_text="Enter notation"
        )
        self.notationBox.grid(row=0, column=3, padx=10)

        # Button to Fetch Information
        self.catButton = ctk.CTkButton(
            input_frame,
            text="Fetch Info",
            command=self.CreateInformationLabel
        )
        self.catButton.grid(row=0, column=4, padx=10)


    def GetInformation(self):
        lst = [self.categoryComboBox.get(), self.costBox.get(),self.itemBox.get(),self.notationBox.get()]
        return lst
        

    def CreateInformationLabel(self):
        frame = ctk.CTkFrame(self,width=720, height=30)
        frame.grid_propagate(False)
        frame.pack(pady=3)
        info = self.GetInformation()
        label = ctk.CTkLabel(frame,text="{}".format(info[0]))
        label.grid(row=0, column=0, padx=50, pady=3)
        label1 = ctk.CTkLabel(frame,text="{}".format(info[1]))
        label1.grid(row=0, column=1, padx=3)
        label2 = ctk.CTkLabel(frame,text="{}".format(info[2]))
        label2.grid(row=0, column=2, padx=3)
        label3 = ctk.CTkLabel(frame,text="{}".format(info[3]))
        label3.grid(row=0, column=3, padx=3)

# Create and run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()
