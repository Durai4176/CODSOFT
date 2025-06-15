import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Math Error", "Division by zero is undefined.")
                return
        else:
            messagebox.showerror("Invalid Operation", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {round(result, 4)}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

app = tk.Tk()
app.title("Modern Python Calculator")
app.geometry("400x450")
app.config(bg="#1e1e2f")
app.resizable(False, False)

tk.Label(app, text="Python Calculator", font=("Helvetica", 20, "bold"),
         fg="#ffffff", bg="#1e1e2f").pack(pady=20)

frame = tk.Frame(app, bg="#1e1e2f")
frame.pack(pady=10)

tk.Label(frame, text="First Number", fg="#dcdcdc", bg="#1e1e2f", font=("Helvetica", 12)).grid(row=0, column=0, pady=10, sticky='w')
entry1 = tk.Entry(frame, font=("Helvetica", 12), width=25, bg="#2e2e3f", fg="white", insertbackground="white", relief="flat")
entry1.grid(row=1, column=0, padx=10)

tk.Label(frame, text="Second Number", fg="#dcdcdc", bg="#1e1e2f", font=("Helvetica", 12)).grid(row=2, column=0, pady=10, sticky='w')
entry2 = tk.Entry(frame, font=("Helvetica", 12), width=25, bg="#2e2e3f", fg="white", insertbackground="white", relief="flat")
entry2.grid(row=3, column=0, padx=10)

tk.Label(app, text="Select Operation", fg="#dcdcdc", bg="#1e1e2f", font=("Helvetica", 12)).pack(pady=10)
operation_var = tk.StringVar(app)
operation_var.set("+")
dropdown = tk.OptionMenu(app, operation_var, "+", "-", "*", "/")
dropdown.config(bg="#444", fg="white", font=("Helvetica", 12), width=10)
dropdown["menu"].config(bg="#444", fg="white")
dropdown.pack()

tk.Button(app, text="Calculate", command=calculate,
          bg="#4CAF50", fg="white", font=("Helvetica", 14), width=20).pack(pady=20)

result_label = tk.Label(app, text="Result: ", font=("Helvetica", 14, "bold"),
                        fg="#00FFAA", bg="#1e1e2f")
result_label.pack(pady=10)

app.mainloop()
