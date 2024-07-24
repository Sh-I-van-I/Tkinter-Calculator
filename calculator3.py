import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.entry = tk.Entry(root, font=("Arial", 18), justify="right", bg="white")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0, "lightblue"), ('8', 1, 1, "lightblue"), ('9', 1, 2, "lightblue"), ('/', 1, 3, "orange"),
            ('4', 2, 0, "lightblue"), ('5', 2, 1, "lightblue"), ('6', 2, 2, "lightblue"), ('*', 2, 3, "orange"),
            ('1', 3, 0, "lightblue"), ('2', 3, 1, "lightblue"), ('3', 3, 2, "lightblue"), ('-', 3, 3, "orange"),
            ('0', 4, 0, "lightblue"), ('+', 4, 1, "orange"), ('.', 4 , 2, "orange"), ('//', 4, 3, "orange"),
            ('**', 5, 0, "orange"), ('(', 5, 1, "lightpink"), (')', 5, 2, "lightpink"), ('%', 5, 3, "orange"),
            ('C', 6, 0, "lightcoral"), ('=', 6, 1, "orange")
        ]

        for (text, row, col, color) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 14), bg=color)
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            if text == "=":
                button.config(command=self.calculate)
            elif text == "C":
                button.config(command=self.clear)
            else:
                button.config(command=self.add_to_entry)

    def add_to_entry(self):
        text = self.root.focus_get().cget("text")
        self.entry.insert(tk.END, text)

    def calculate(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def clear(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
