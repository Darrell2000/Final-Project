
import tkinter as tk
from tkinter import messagebox

# Function to open the wellness tools window
def open_wellness_tools():
    wellness_window = tk.Toplevel(root)
    wellness_window.title("Mental Wellness Tools")
    wellness_window.geometry("400x400")
    wellness_window.configure(bg="skyblue")  # Set background color

    # Labels and buttons for wellness tools
    tk.Label(wellness_window, text="Guided Meditation", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Start Meditation", bg="#3498db", fg="white", command=lambda: messagebox.showinfo("Meditation", "Starting guided meditation...")).pack()

    tk.Label(wellness_window, text="Breathing Exercises", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Start Exercise", bg="#2ecc71", fg="white", command=lambda: messagebox.showinfo("Breathing Exercise", "Starting breathing exercises...")).pack()

    tk.Label(wellness_window, text="Habit Tracker", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Open Tracker", bg="#e67e22", fg="white", command=lambda: messagebox.showinfo("Habit Tracker", "Opening habit tracker...")).pack()

# Function to open the professional support window
def open_professional_support():
    support_window = tk.Toplevel(root)
    support_window.title("Professional Support")
    support_window.geometry("400x300")
    support_window.configure(bg="skyblue")  # Set background color

    tk.Label(support_window, text="Live Chat with Licensed Professionals", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="Start Chat", bg="#9b59b6", fg="white", command=lambda: messagebox.showinfo("Live Chat", "Connecting to a mental health professional...")).pack()

    tk.Label(support_window, text="Scheduled Appointments", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="Book Appointment", bg="#f1c40f", fg="black", command=lambda: messagebox.showinfo("Appointment", "Redirecting to appointment scheduling...")).pack()

    tk.Label(support_window, text="Resource Library", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="View Articles", bg="#e74c3c", fg="white", command=lambda: messagebox.showinfo("Resources", "Opening mental health articles and videos...")).pack()

# Function to validate user input
def validate_and_proceed():
    name = name_entry.get().strip()
    if not name:
        messagebox.showerror("Input Error", "Name cannot be empty!")
        return
    
    messagebox.showinfo("Welcome", f"Hello {name}, let's explore mental wellness!")
    open_wellness_tools()

# Main window
root = tk.Tk()
root.title("MindShift Wellness Hub")
root.geometry("500x400")
root.configure(bg="skyblue")  # Set background color

# Labels
tk.Label(root, text="Welcome to MindShift Wellness Hub", font=("Arial", 14, "bold"), bg="skyblue").pack(pady=10)
tk.Label(root, text="Enter your name to begin:", font=("Arial", 12), bg="skyblue").pack(pady=5)

# Entry field
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Buttons with specific colors
tk.Button(root, text="Start Wellness Tools", bg="#3498db", fg="white", command=validate_and_proceed).pack(pady=5)
tk.Button(root, text="Professional Support", bg="#2ecc71", fg="white", command=open_professional_support).pack(pady=5)
tk.Button(root, text="Exit", bg="#e74c3c", fg="white", command=root.quit).pack(pady=5)

# Run the application
root.mainloop()
