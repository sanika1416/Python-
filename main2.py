import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import os

# ----------------------------------
PROGRAM_SHORTNAMES = {
    "B.Tech - Computer Science & Engineering": "CSE",
    "B.Tech - Computer Science & Engineering (Data Science)": "CSE (DS)",
    "B.Tech - Electronics & Tele.communication Engineering": "E&TC",
    "B.Tech - Chemical Engineering": "Chem",
    "B.Tech - Mechanical Engineering": "Mech",
    "B.Tech - Civil Engineering": "Civil"
}

# ----------------------------------
def load_data(file_path="data.csv"):
    df = pd.read_csv(file_path)
    df['Program Short'] = df['Program Name'].apply(lambda x: PROGRAM_SHORTNAMES.get(x, x))
    return df

# ----------------------------------
def save_students_by_program(df):
    os.makedirs("program_wise_students", exist_ok=True)
    for program, group in df.groupby("Program Name"):
        # Add Program Short column to saved CSV
        group = group.copy()
        group['Program Short'] = PROGRAM_SHORTNAMES.get(program, program)
        filename = f"program_wise_students/{program}.csv"
        group.to_csv(filename, index=False)
    tk.messagebox.showinfo("Success", "Program-wise CSV files created with short names!")

# ----------------------------------
def plot_number_of_students(df, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    counts = df['Program Short'].value_counts()
    fig, ax = plt.subplots(figsize=(6,5))
    bars = ax.barh(counts.index, counts.values, color='blue')
    for bar in bars:
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{int(bar.get_width())}', va='center')

    ax.set_title("Number of Students by Program")
    ax.set_xlabel("Number of Students")
    ax.set_ylabel("Program")
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ----------------------------------
def plot_average_cgpa(frame):
    folder = "program_wise_students"
    if not os.path.exists(folder):
        tk.messagebox.showerror("Error", "Please create program-wise CSV files first!")
        return

    avg_cgpa = {}
    for file in os.listdir(folder):
        if file.endswith(".csv"):
            df_program = pd.read_csv(os.path.join(folder, file))
            # Use the short name column
            program_short = df_program['Program Short'].iloc[0]
            avg_cgpa[program_short] = df_program["CGPA"].mean()

    # Sort descending
    avg_cgpa = dict(sorted(avg_cgpa.items(), key=lambda x: x[1], reverse=True))

    for widget in frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(6,5))
    bars = ax.bar(avg_cgpa.keys(), avg_cgpa.values(), color='salmon')
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                f'{bar.get_height():.2f}', ha='center')

    ax.set_title("Average CGPA by Program")
    ax.set_ylabel("Average CGPA")
    plt.xticks(rotation=15)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# ----------------------------------
def run_gui():
    df = load_data("data.csv")

    root = tk.Tk()
    root.title("Student Data Analyzer")
    root.geometry("1920x1080")

    # Left frame for buttons
    button_frame = tk.Frame(root,width=500, bg="#f0f0f0")
    button_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Right frame for results
    result_frame = tk.Frame(root, bg="white")
    result_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Buttons (vertical)
    tk.Button(button_frame, text="Save Students by Program", width=20, height=2,
              command=lambda: save_students_by_program(df)).pack(pady=10)
    tk.Button(button_frame, text="Plot Number of Students", width=20, height=2,
              command=lambda: plot_number_of_students(df, result_frame)).pack(pady=10)
    tk.Button(button_frame, text="Plot Average CGPA", width=20, height=2,
              command=lambda: plot_average_cgpa(result_frame)).pack(pady=10)
    tk.Button(button_frame, text="Exit", width=20, height=2,
              command=root.destroy).pack(pady=10)

    root.mainloop()

# ----------------------------
if __name__ == "__main__":
    run_gui()
