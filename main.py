import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")

        self.expression = ""

        # Entry field for display
        self.display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            tk.Button(root, text=button, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Clear button
        tk.Button(root, text="C", font=("Arial", 18), command=self.clear).grid(row=row, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
        tk.Button(root, text="CE", font=("Arial", 18), command=self.clear_entry).grid(row=row, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                self.expression = ""
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def clear_entry(self):
        self.expression = ""
        self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()