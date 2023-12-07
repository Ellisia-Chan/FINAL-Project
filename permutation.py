import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

def generate_table():
    try:
        # Get items in Window Entry
        score = int(ent_item.get())
        base = int(ent_base.get())

        # Constant
        base_value = 100

        # Conditions
        if score > 0:
            base_increment = base / score
        else:
            base_increment = 0

        # Generate Table Header
        result = f"{'Score':<12}|   {'Base':<15}\n"
        result += "-" * 30 + "\n"

        # Generate Score and Base Numbers
        for i in range(score, 0, -1):
            num_score = f"Score {i}"
            f_base = int(base_value)
            num_result = f"{num_score:<12}|  {f_base}%"

            # Subtract the base increment only if the score is greater than 1
            if i > 1:
                base_value -= base_increment

            # Result
            result += num_result + "\n"

        # Calculate the final result based on the total score and base
        final_result = int((base / 100) * score)

        # Update grade_result_lbl with the final result
        grade_result_lbl.config(text=f"Passing Score: Score {final_result}")

        # Clear previous content of the table
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)

        # Insert new content to the table
        result_text.insert(tk.END, result)

        # Disable editing of the table
        result_text.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("ERROR", "Invalid Input")



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
grade_result_lbl = tk.Label(win, text=f"Passing Score:")
grade_result_lbl.place(x=210, y=490)


# Loop Window
win.mainloop()
