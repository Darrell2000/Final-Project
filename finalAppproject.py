
"""Darrell Davis
    02/01/2025
    Final Project Application"""

"""MindShift Wellness Hub - Tkinter GUI Application

This Python application provides a simple graphical user interface (GUI) using Tkinter to help users explore
mental wellness tools and access professional support. The application includes:
- A main window where users enter their name to begin.
- A wellness tools window that provides access to guided meditation, breathing exercises, and a habit tracker.
- A professional support window that allows users to start a live chat, book appointments, and view resources.
- Input validation to ensure users enter a name before proceeding.
- Placeholder labels indicating where images should be displayed.
"""
import tkinter as tk  # Import the tkinter library for GUI development
from tkinter import messagebox  # Import messagebox for displaying alerts

# Function to open the wellness tools window
def open_wellness_tools():
    """Creates a new window with wellness tool options."""
    wellness_window = tk.Toplevel(root)  # Creates a new top-level window
    wellness_window.title("Mental Wellness Tools")  # Sets window title
    wellness_window.geometry("400x400")  # Sets window size
    wellness_window.configure(bg="skyblue")  # Sets background color
    
    # Label placeholder for image
    tk.Label(wellness_window, text="[Image placeholder: Wellness Tools]", font=("Arial", 10), bg="skyblue").pack(pady=5)
    
    # Labels and buttons for wellness tools
    tk.Label(wellness_window, text="Guided Meditation", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Start Meditation", bg="#3498db", fg="white", 
              command=lambda: messagebox.showinfo("Meditation", "Starting guided meditation...")).pack()
    
    tk.Label(wellness_window, text="Breathing Exercises", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Start Exercise", bg="#2ecc71", fg="white", 
              command=lambda: messagebox.showinfo("Breathing Exercise", "Starting breathing exercises...")).pack()
    
    tk.Label(wellness_window, text="Habit Tracker", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(wellness_window, text="Open Tracker", bg="#e67e22", fg="white", 
              command=lambda: messagebox.showinfo("Habit Tracker", "Opening habit tracker...")).pack()

# Function to open the professional support window
def open_professional_support():
    """Creates a new window with professional support options."""
    support_window = tk.Toplevel(root)  # Creates a new top-level window
    support_window.title("Professional Support")  # Sets window title
    support_window.geometry("400x300")  # Sets window size
    support_window.configure(bg="skyblue")  # Sets background color
    
    # Label placeholder for image meditation chair
    #tk.Label(support_window, text="[Image placeholder: Professional Support]", font=("Arial", 10), bg="skyblue").pack(pady=5)
    
    # Labels and buttons for professional support options
    tk.Label(support_window, text="Live Chat with Licensed Professionals", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="Start Chat", bg="#95b9b6", fg="white", 
              command=lambda: messagebox.showinfo("Live Chat", "Connecting to a mental health professional...")).pack()
    
    tk.Label(support_window, text="Scheduled Appointments", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="Book Appointment", bg="#f1c40f", fg="white", 
              command=lambda: messagebox.showinfo("Appointment", "Redirecting to appointment scheduling...")).pack()
    
    tk.Label(support_window, text="Resource Library", font=("Arial", 12), bg="skyblue").pack(pady=5)
    tk.Button(support_window, text="View Articles", bg="#e74c3c", fg="white", 
              command=lambda: messagebox.showinfo("Resources", "Opening mental health articles and videos...")).pack()

# Function to validate user input
def validate_and_proceed():
    """Validates user input and opens the wellness tools window if valid."""
    name = name_entry.get().strip()  # Get user input and remove extra spaces
    if not name:  # Check if name field is empty
        messagebox.showerror("Input Error", "Name cannot be empty!")  # Display error message
        return  # Exit function if validation fails
    messagebox.showinfo("Welcome", f"Hello {name}, let's explore mental wellness!")  # Display welcome message
    open_wellness_tools()  # Open wellness tools window

# Main application window
root = tk.Tk()  # Create main application window
root.title("MindShift Wellness Hub")  # Set window title
root.geometry("500x400")  # Set window size
root.configure(bg="skyblue")  # Set background color

# Label placeholder for image, Person supportive breathing
#tk.Label(root, text="[Image placeholder: Main Window]", font=("Arial", 10), bg="skyblue").pack(pady=5)

# Labels
tk.Label(root, text="Welcome to MindShift Wellness Hub", font=("Arial", 14, "bold"), bg="skyblue").pack(pady=10)  # Title label
tk.Label(root, text="Enter your name to begin:", font=("Arial", 12), bg="skyblue").pack(pady=5)  # Instruction label

# Entry field for user name
name_entry = tk.Entry(root, width=30)  # Create entry field for name input
name_entry.pack(pady=5)  # Add padding to entry field

# Buttons with specific colors
tk.Button(root, text="Start Wellness Tools", bg="#3498db", fg="white", command=validate_and_proceed).pack(pady=5)  # Button to start wellness tools
tk.Button(root, text="Professional Support", bg="#2ecc71", fg="white", command=open_professional_support).pack(pady=5)  # Button for professional support
tk.Button(root, text="Exit", bg="#e74c3c", fg="white", command=root.quit).pack(pady=5)  # Exit button

# Run the application
root.mainloop()  # Start Tkinter event loop
