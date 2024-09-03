import tkinter as tk
from tkinter import filedialog, messagebox
import Ofcom_PDF_to_CSV_Converter  # Import the core functionality script

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_path_var.set(file_path)

def select_csv():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        csv_path_var.set(file_path)

def convert_pdf_to_csv():
    pdf_path = pdf_path_var.get()
    csv_path = csv_path_var.get()
    
    if not pdf_path or not csv_path:
        messagebox.showerror("Error", "Please select both PDF and CSV file paths.")
        return
    
    try:
        Ofcom_PDF_to_CSV_Converter.main(pdf_path, csv_path)  # Call the main conversion function
        messagebox.showinfo("Conversion Complete", 
                            f"Your data has been successfully converted and saved to:\n{csv_path}",
                            icon='info')  # Use 'info' icon
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Initialize the main application window
root = tk.Tk()
root.title("Ofcom PDF to CSV Converter")

# Set the fixed size of the window
root.geometry("800x200")
root.resizable(False, False)  # Disable window resizing

# Create StringVar to hold the file paths
pdf_path_var = tk.StringVar()
csv_path_var = tk.StringVar()

# Create the GUI using grid
tk.Label(root, text="Select the PDF File:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
tk.Entry(root, textvariable=pdf_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_pdf).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select the CSV Save Location:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
tk.Entry(root, textvariable=csv_path_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_csv).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Convert", command=convert_pdf_to_csv).grid(row=2, column=1, padx=10, pady=20)

# Add a label at the bottom for creator information using grid
tk.Label(root, text="Created by Dom Trotta", font=("Arial", 15), fg="red").grid(row=3, column=0, columnspan=3, pady=10, sticky='s')

root.mainloop()