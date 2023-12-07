import tkinter as tk
from tkinter import scrolledtext

def generate_table():
    # Get items in Window Entry
    score = int(ent_item.get())
    base = int(ent_base.get())

    #constant
    base_value = 100

    # Conditions
    if score > 0:
        base_increment = base / score
    else:
        base_increment = 0

    # Generate Score and Base Numbers
    result = f"{'Score':<12}|   {'Base':<15}\n"
    result += "-" * 30 + "\n"

    for i in range(score, -1, -1):
        num_score = f"Score {i}"
        num_result = f"{num_score:<12}|  {base_value:<15,.2f}"

        # Subtract the base increment only if score is greater than 0
        if i > 0:
            base_value -= base_increment

        # Result
        result += num_result + "\n"

    # Clear previous content of the table
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)

    # Insert new content to the table
    result_text.insert(tk.END, result)

    # Disable editing of the table
    result_text.config(state=tk.DISABLED)


# Window Declaration
win = tk.Tk()
win.geometry("600x600")
win.title("Grading System")
win.resizable(False, False)

# Window Design
win.configure(bg="#5FBDFF")

# Labels
tk.Label(win, text="Grading System").place(x=240, y=5)
tk.Label(win, text="Enter Number of Items:").place(x=130, y=30)
tk.Label(win, text="Enter Base Value:").place(x=130, y=60)

# Entries
ent_item = tk.Entry(win)
ent_base = tk.Entry(win)

# Entry Grid
ent_item.place(x=265, y=30)
ent_base.place(x=265, y=60)

# Button
btn_calcu = tk.Button(win, text="Calculate", command=generate_table, width=10, height=2)
btn_calcu.place(x=240, y=100)

# Scrollable Result Text
result_text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=30, height=20)
result_text.place(x=150, y=150)

# Passing Label
grade_result_lbl = tk.Label(win, text="Result")
grade_result_lbl.place(x=240, y=490)


# Loop Window
win.mainloop()
