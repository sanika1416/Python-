import pandas as pd
import matplotlib.pyplot as plt
import os


#Data Loading use pandas
def load_data(file_path='data.xlsx'):
    """Load Excel file into a DataFrame."""
    try:
        df = pd.read_excel(file_path)
        # Create 'Program Short' as a copy of 'Program Name' for other functions
        df['Program Short'] = df['Program Name'].str.strip()
        print(f"Data successfully loaded from {file_path}. Total records: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print(f"Please make sure '{file_path}' is in the same directory as the script.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None


#Save students department wise in one folder

def save_students_by_program(df):
    """Sort students by program and save each program as a CSV."""
    df_sorted = df.sort_values(by="Program Name")
    output_dir = "program_wise_students"
    os.makedirs(output_dir, exist_ok=True) # Added exist_ok=True to prevent crash if dir exists

    # Groups by the original 'Program Name' (e.g., "CSE", "ETC")
    for program, group in df_sorted.groupby("Program Name"):
        
        # --- Simple filename cleaning logic is now inside this function ---
        safe_name = str(program).replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')
        filename = f"{safe_name}_students.csv"
        # -----------------------------------------------------------------
        
        filepath = os.path.join(output_dir, filename)
        group.to_csv(filepath, index=False)
        print(f"Saved {len(group)} students for '{program}' → {filepath}")
    print("\nAll program-wise student files created successfully!")


#Plot Number of students department wise

def plot_number_of_students(df):
    """Plot the number of students in each program."""
    program_counts = df['Program Short'].value_counts().sort_values(ascending=True)

    print("\nStudent count per program:")
    print(program_counts.to_markdown(numalign="left", stralign="left"), "\n")

    plt.figure(figsize=(12, 7))
    bars = plt.barh(program_counts.index, program_counts.values, color='#3498db', edgecolor='black')

    for bar in bars:
        width = bar.get_width()
        plt.text(width + 1, bar.get_y() + bar.get_height() / 2, f'{int(width)}',
                 ha='left', va='center', fontsize=12, fontweight='bold')

    plt.title("Number of Students by Program", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Number of Students", fontsize=14)
    plt.ylabel("Program", fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xlim(right=program_counts.max() * 1.1)
    plt.tight_layout()
    # plt.savefig("students_by_program_plot.png")
    # print("Plot saved as 'students_by_program_plot.png'")
    plt.show() 

#Plot avg CGPA of students departmentwise
def plot_average_cgpa(df):
    """Plot the average CGPA of each program directly from the DataFrame."""
    
    avg_cgpa_series = df.groupby('Program Short')['CGPA'].mean().sort_values(ascending=False)

    programs = avg_cgpa_series.index.tolist()
    averages = avg_cgpa_series.values.tolist()
    
    print("\nAverage CGPA per program:")
    print(avg_cgpa_series.to_markdown(numalign="left", stralign="left", floatfmt=".2f"), "\n")

    plt.figure(figsize=(10, 8))
    bars = plt.bar(programs, averages, color='#e74c3c', edgecolor='black')

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 0.05, f'{height:.2f}',
                 ha='center', va='bottom', fontsize=12, fontweight='bold')

    plt.title("Average CGPA by Academic Program", fontsize=20, fontweight='bold', pad=20)
    plt.xlabel("Academic Program", fontsize=14)
    plt.ylabel("Average CGPA", fontsize=14)
    plt.ylim(bottom=avg_cgpa_series.min() * 0.9, top=avg_cgpa_series.max() * 1.1)
    plt.xticks(rotation=15, ha='right', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    # plt.savefig("average_cgpa_plot.png")
    # print("Plot saved as 'average_cgpa_plot.png'")
    plt.show()

# ----------------------------
# Menu System
# ----------------------------
def run_menu(df):
    """Run the main interactive menu."""
    if df is None:
        print("Data could not be loaded. Exiting application.")
        return

    while True:
        print("\n==============================================")
        print("  Student Data Analyzer Menu")
        print("==============================================")
        print("1. Sort and Save Students by Program (Creates CSV files)")
        print("2. Plot Number of Students by Program")
        print("3. Plot Average CGPA by Academic Program")
        print("4. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            save_students_by_program(df)
        elif choice == '2':
            plot_number_of_students(df)
        elif choice == '3':
            plot_average_cgpa(df)
        elif choice == '4':
            print("Exiting Analyzer...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    df = load_data("data.xlsx")
    run_menu(df)