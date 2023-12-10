# Import necessary modules from the Tkinter library
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# Function to generate and display a grading table
def generate_table():
    try:
        # Get the number of items and base value from user input
        score = int(ent_item.get())
        base = int(ent_base.get())

        # Constants for calculations
        base_value = 100
        base_percent = None

        # Calculate the passing score based on the total score and base
        Passing_Score = int((base / 100) * score)

        # Calculate base increment based on number of Score Items
        if score > 0:
            base_increment = base / score
        else:
            base_increment = 0

        # Generate Table Header
        result = f"{'Score':<12}|   {'Base':<15}\n"
        result += "-" * 30 + "\n"

        # Generate Score and Base Numbers for the table
        for i in range(score, -1, -1):
            num_score = f"Score {i}"
            f_base = int(base_value)
            num_result = f"{num_score:<12}|  {f_base}%"

            # Subtract the base increment only if the score is greater than or equal to 0
            if i >= 0:
                base_value -= base_increment
            
            # Store base percent when i var equals Passing_Score
            if i == Passing_Score:
                base_percent = f_base

            # Append the result to the table
            result += num_result + "\n"        

        # Update the label with the final result
        grade_result_lbl.config(text=f"Passing Score: Score {Passing_Score} | {base_percent}%")

        # Clear and update the scrollable text area with the table content
        result_text_area.config(state=tk.NORMAL)
        result_text_area.delete(1.0, tk.END)
        result_text_area.insert(tk.END, result)

        # Disable editing of the table
        result_text_area.config(state=tk.DISABLED)

    except ValueError:
        # Display an error message if invalid input is provided
        messagebox.showerror("ERROR", "Invalid Input")

# Create the main window
win = tk.Tk()
win.geometry("600x600")
win.title("TkGrader: A User-Friendly Grading Interface for Swift Score Computation")
win.resizable(False, False)

# Set the background color of the window
win.configure(bg="#5FBDFF")

# Labels for the GUI
tk.Label(win, text="Grading System", font=("Helvetica", 10)).place(x=240, y=5)
tk.Label(win, text="Enter Number of Items:", font=("Helvetica", 10)).place(x=120, y=30)
tk.Label(win, text="Enter Base Value:", font=("Helvetica", 10)).place(x=130, y=60)

# Entry fields for user input
ent_item = tk.Entry(win)
ent_base = tk.Entry(win)

# Place entry fields in the window
ent_item.place(x=265, y=30)
ent_base.place(x=265, y=60)

# Button to trigger the calculation and table generation
btn_calcu = tk.Button(win, text="Calculate", command=generate_table, width=10, height=2, font=("Helvetica", 10))
btn_calcu.place(x=240, y=90)

# Scrollable text area for displaying the grading table
result_text_area = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=30, height=20)
result_text_area.place(x=150, y=150)

# Label for displaying the passing score
grade_result_lbl = tk.Label(win, text=f"Passing Score:___________", font=("Helvetica", 12))
grade_result_lbl.place(x=170, y=490)

# Start the Tkinter event loop
win.mainloop()
