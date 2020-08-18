#!/usr/bin/python3

from tkinter import (
    Tk,
    Grid,
    Frame,
    Entry,
    Button,
    Label,
    END,
    ttk,
    VERTICAL,
    Checkbutton,
    IntVar,
    messagebox,
)

import string as s
import random as r
import secrets as sec
import sys

class PassGen:
    def __init__(self, root):

        self.root = root
        self.root.title("rx-passgen  v0.2")
        self.root.wm_minsize(400, 200)
        self.root.grid_anchor(anchor="c")

        frame = Frame(root)

        self.labelSpecial = Label(frame, text="Specials: ")
        self.labelSpecial.grid(row=1, column=1, sticky="w")
        self.entrySpecial = Entry(frame, justify="center")
        self.entrySpecial.grid(row=1, column=2, sticky="w")

        self.labelNumbers = Label(frame, text="Numbers: ")
        self.labelNumbers.grid(row=2, column=1, sticky="w")
        self.entryNumbers = Entry(frame, justify="center")
        self.entryNumbers.grid(row=2, column=2, sticky="w")

        self.labelLower = Label(frame, text="Lower case: ")
        self.labelLower.grid(row=3, column=1, sticky="w")
        self.entryLower = Entry(frame, justify="center")
        self.entryLower.grid(row=3, column=2, sticky="w")

        self.labelUpper = Label(frame, text="Upper case: ")
        self.labelUpper.grid(row=4, column=1, sticky="w")
        self.entryUpper = Entry(frame, justify="center")
        self.entryUpper.grid(row=4, column=2, sticky="w")

        self.entrySpecial.insert(0, "3")
        self.entryNumbers.insert(0, "3")
        self.entryLower.insert(0, "3")
        self.entryUpper.insert(0, "3")

        self.Gen = Button(frame, text="Generate", width=10)
        self.Gen.grid(row=5, column=1, columnspan=3, pady=3, sticky="NSEW")
        self.Gen.config(command=self.generate)

        self.line = ttk.Separator(frame)
        self.line.grid(
            sticky="EW",
            row=6,
            column=1,
            columnspan=3,
            pady=3,
        )

        self.labelPassword = Label(frame, text="Password: ")
        self.labelPassword.grid(row=7, column=1, sticky="w")
        self.entryPassword = Entry(frame)
        self.entryPassword.grid(row=7, column=2, sticky="w")

        frame.grid()

    def generate(self):
        
        #try:
            self.qtd_special = int(self.entrySpecial.get())
            self.qtd_numbers = int(self.entryNumbers.get())
            self.qtd_lowercase = int(self.entryLower.get())
            self.qtd_uppercase = int(self.entryUpper.get())

            self.special = s.punctuation
            self.numbers = s.digits
            self.lowercase = s.ascii_lowercase
            self.uppercase = s.ascii_uppercase 

            choosen_special = [
                sec.choice(self.special) for char in range(0, self.qtd_special)
            ]
            choosen_numbers = [
                sec.choice(self.numbers) for char in range(0, self.qtd_numbers)
            ]
            choosen_lowercase = [
                sec.choice(self.lowercase) for char in range(0, self.qtd_lowercase)
            ]
            choosen_uppercase = [
                sec.choice(self.uppercase) for char in range(0, self.qtd_uppercase)
            ]
            password = (
                choosen_special + choosen_numbers + choosen_lowercase + choosen_uppercase
            )
            password = "".join(r.sample(password, len(password)))

            self.entryPassword.delete(0, END)
            self.entryPassword.insert(0, password)
            root.clipboard_clear()
            root.clipboard_append(password)

        #except:
        #    self.error("Invalid data, quantities must be integer numbers!")

    def error(self, message):
        messagebox.showerror("Error", message)

    def main(self):
        pass


if __name__ == "__main__":
    root = Tk()
    passgen = PassGen(root)
    passgen.main()
    root.mainloop()

