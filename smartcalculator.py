import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(expression))
            screen_var.set(result)
            expression = result
        except Exception:
            screen_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen_var.set("")
    else:
        expression += text
        screen_var.set(expression)

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("300x400")
root.config(bg="#dfe6e9")

expression = ""
screen_var = tk.StringVar()

screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", bg="#ecf0f1")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "C", "+"],
    ["="]
]

for row in buttons:
    frame = tk.Frame(root, bg="#dfe6e9")
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="lucida 15 bold", width=5, height=2, bg="white")
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
